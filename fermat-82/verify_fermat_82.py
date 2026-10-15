#!/usr/bin/env python3
"""Finite certificates for Rational Fourth Powers Summing to 82.

Uses only the Python 3 standard library. Exact point arithmetic uses
Q(theta), theta^4 - 86*theta^2 + 1521 = 0, theta = sqrt(41) + sqrt(2).
The integral coordinate basis is (1, alpha, s, alpha*s), alpha = (1+r)/2.
Checks the covering identity, field arithmetic, local Kummer images,
all 65536 candidate pairs, and the logarithmic residues in Section 7.
"""
from fractions import Fraction as F
from itertools import product
from functools import cmp_to_key
from math import comb
import time,json
import os as filesystem

ZERO=(F(0),)*4;ONE=(F(1),F(0),F(0),F(0))
def padd(a,b):return tuple(x+y for x,y in zip(a,b))
def pneg(a):return tuple(-x for x in a)
def pscale(a,c):return tuple(x*c for x in a)
def pmul(a,b):
    z=[F(0)]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    for k in range(6,3,-1):z[k-2]+=86*z[k];z[k-4]-=1521*z[k]
    return tuple(z[:4])
def pinv(a):
    cols=[pmul(a,tuple(F(i==j) for i in range(4))) for j in range(4)]
    rows=[[cols[j][i] for j in range(4)]+[F(i==0)] for i in range(4)]
    for j in range(4):
        k=next(k for k in range(j,4) if rows[k][j]);rows[j],rows[k]=rows[k],rows[j]
        c=rows[j][j];rows[j]=[t/c for t in rows[j]]
        for k in range(4):
            if k!=j:
                c=rows[k][j];rows[k]=[x-c*y for x,y in zip(rows[k],rows[j])]
    ans=tuple(rows[i][4] for i in range(4));assert pmul(a,ans)==ONE
    return ans
def pdiv(a,b):return pmul(a,pinv(b))
def to_theta(v):
    a,b,c,d=map(F,v)
    return(a+b/2-43*d/4,125*b/156-47*c/78-47*d/156,d/4,-b/156+c/78+d/156)
def to_integral(v):
    a,b,c,d=v
    return(a-b+43*c-47*d,2*b+94*d,b-2*c+125*d,4*c)

def omul(u,v):
    a,b,c,d=u;A,B,C,D=v
    return(a*A+10*b*B+2*c*C+20*d*D,
           a*B+b*A+b*B+2*c*D+2*d*C+2*d*D,
           a*C+c*A+10*b*D+10*d*B,
           a*D+d*A+b*C+c*B+b*D+d*B)
def oa(u,v):return tuple(a+b for a,b in zip(u,v))
def os(u,c):return tuple(a*c for a in u)
def onorm(u):
    a,b,c,d=u;A=a*a+10*b*b-2*c*c-20*d*d;B=2*a*b+b*b-4*c*d-2*d*d
    return A*A+A*B-10*B*B

def span(vs):
    out={0}
    for v in vs:out|={x^v for x in out}
    return out

def lsign(a,b,sr):
    A=2*a+b;B=sr*b
    sg=lambda x:(x>0)-(x<0)
    if not A:return sg(B)
    if not B:return sg(A)
    if sg(A)==sg(B):return sg(A)
    return sg(A) if A*A>41*B*B else sg(B)
def osign(u,sr,ss):
    a,b,c,d=u;A=lsign(a,b,sr);B=ss*lsign(c,d,sr)
    if not A:return B
    if not B:return A
    if A==B:return A
    na=a*a+10*b*b-2*c*c-20*d*d;nb=2*a*b+b*b-4*c*d-2*d*d
    return A if lsign(na,nb,sr)>0 else B

SG=[(-1,0,0,0),(1,0,1,0),(27,10,0,0),(11,4,8,3),
    (3,1,0,0),(0,0,1,0),(-1,2,0,0),(1,1,2,1)]
D=(-68,13,45,-8);B=(2624,-656,-2132,533)
E2=omul(D,(1,0,1,0));E3=omul(D,(-2,0,-1,0))
P=((164,-41,0,0),(-2132,574,-328,82))
Q=((F(1100827,36),F(-297329,36),F(-194450,9),F(17510,3)),
   (F(714964567,72),F(-579455603,216),F(-758329601,108),F(204866999,108)))
R=((F(5063,28),F(-16673,392),F(-1727,14),F(6427,196)),
   (F(9582021,2744),F(-5262449,5488),F(-13595319,5488),F(7268179,10976)))

# Local rings Q_p(sqrt(p)), separately at the four bad primes.
def lm(x,y,p,m):return((x[0]*y[0]+p*x[1]*y[1])%m,(x[0]*y[1]+x[1]*y[0])%m)
def ls(x,y,m):return((x[0]-y[0])%m,(x[1]-y[1])%m)
def lift(p,N,r0):
    f=(lambda t:t*t-t-10) if p==2 else(lambda t:t*t-2)
    r=r0;m=p
    for n in range(1,N):
        rs=[r+j*m for j in range(p) if f(r+j*m)%(m*p)==0]
        assert len(rs)==1;r=rs[0];m*=p
    return r

def leval(u,p,N,r0):
    m=p**N;rt=lift(p,N,r0);a,b,c,d=u
    if p==2:return((a+b*rt)%m,(c+d*rt)%m)
    inv2=pow(2,-1,m)
    return((a+c*rt+(b+d*rt)*inv2)%m,((b+d*rt)*inv2)%m)

def valp(x,p,N):
    if x==0:return N
    n=0
    while x%p==0:x//=p;n+=1
    return n

def normalized(x,p,N):
    m=p**N;a,b=x[0]%m,x[1]%m
    v=min(2*valp(a,p,N),2*valp(b,p,N)+1)
    assert v<2*N-8
    k=v//2
    if v%2:a,b=b//p**k,a//p**(k+1)
    else:a,b=a//p**k,b//p**k
    return v,(a,b)

def local_code(x,p,N):
    v,(a,b)=normalized(x,p,N)
    if p!=2:
        sq={(t*t)%p for t in range(1,p)}
        return v%2+(0 if a%p in sq else 2)
    # Independently identify the unit class by testing quotients against
    # the two possible unit-square residues modulo (sqrt(2))^5.
    answer=[]
    for bits in range(8):
        rep=(1,0)
        for j,g in enumerate([(-1,0),(1,1),(1,2)]):
            if bits>>j&1:rep=lm(rep,g,2,8)
        norm=(rep[0]*rep[0]-2*rep[1]*rep[1])%8
        inverse=(rep[0]*pow(norm,-1,8)%8,-rep[1]*pow(norm,-1,8)%8)
        q=lm((a,b),inverse,2,8)
        if (q[0]%8,q[1]%4) in [(1,0),(3,2)]:answer.append(bits)
    assert len(answer)==1
    return v%2+2*answer[0]

def local_audit(p,r0):
    N=24 if p==2 else 8;m=p**N;bits=4 if p==2 else 2
    d=leval(D,p,N,r0);v,_=normalized(d,p,N);k=v//2
    dh=leval(D,p,N+k+2,r0)
    assert dh[0]%p**k==dh[1]%p**k==0
    d=(dh[0]//p**k%m,dh[1]//p**k%m)
    roots=[(0,0),lm(d,leval((1,0,1,0),p,N,r0),p,m),lm(d,leval((-2,0,-1,0),p,N,r0),p,m)]
    e2,e3=roots[1:];cl=lambda x:local_code(x,p,N)
    tors=[(lm(e2,e3,p,m),ls((0,0),e2,m)),(e2,lm(e2,ls(e2,e3,m),p,m))]
    images=[cl(a)|(cl(b)<<bits) for a,b in tors]
    xs={(2,0):[(0,4),(1,3)],(2,1):[(0,6),(0,12)],(41,17):[(3,0)],(41,24):[]}
    for x in xs[(p,r0)]:
        cs=[cl(ls(x,e,m)) for e in roots]
        assert cs[0]^cs[1]^cs[2]==0
        images.append(cs[0]|(cs[1]<<bits))
    allimages=span(images);assert len(allimages)==(16 if p==2 else 4)
    codes=[cl(leval(g,p,N,r0)) for g in SG]
    masks=[]
    for j in range(256):
        c=0
        for k in range(8):
            if j>>k&1:c^=codes[k]
        masks.append(c)
    print('Local square classes:',p,r0,'codes',codes,'image basis',images)
    return bits,allimages,masks

def birational_identity():
    """Check the full polynomial identity for G -> E, not sample points."""
    one=(F(1),F(0),F(0),F(0));zero=(F(0),)*4
    ap=(F(3,2),F(1,4),F(0),F(0))
    am=(F(7,4),F(-1,4),F(0),F(0))
    bb=(F(-4),F(1),F(0),F(0));ss=(F(0),F(0),F(1),F(0))
    def polyadd(a,b):
        return [oa(a[i] if i<len(a) else zero,b[i] if i<len(b) else zero)
                for i in range(max(len(a),len(b)))]
    def polymul(a,b):
        c=[zero for _ in range(len(a)+len(b)-1)]
        for i,u in enumerate(a):
            for j,v in enumerate(b):c[i+j]=oa(c[i+j],omul(u,v))
        return c
    def polyscale(a,c):return [omul(v,c) for v in a]
    factors=[[os(a,-1),one] for a in [ap,am,bb,ss]]
    f=[one]
    for fac in factors:f=polymul(f,fac)
    den=[os(bb,-1),one];num=polyscale([os(ss,-1),one],P[0])
    lhs=polyscale(f,omul(P[1],P[1]))
    rhs=polymul(num,num)
    rhs=polyadd(polymul(rhs,num),polyscale(polymul(rhs,den),D))
    rhs=polyadd(rhs,polyscale(polymul(num,polymul(den,den)),B))
    rhs=polymul(rhs,den)
    assert lhs==rhs
    assert P[1]==os(omul(oa(bb,os(ss,-1)),P[0]),2)
    print('Covering identity: birational identity G -> E verified exactly.')

def field_and_descent():
    # Different polynomial representation checks all integral basis products.
    basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    for u in basis:
        for v in basis:assert to_integral(pmul(to_theta(u),to_theta(v)))==omul(u,v)
    unit_signs=[]
    for g in SG[:4]:
        assert abs(onorm(g))==1
        unit_signs.append(sum((osign(g,sr,ss)<0)<<j for j,(sr,ss) in enumerate(product([1,-1],repeat=2))))
    assert len(span(unit_signs))==16
    assert omul(SG[7],SG[7])==omul(SG[4],(13,0,8,0))
    assert onorm(SG[7])==-82
    witnesses=[(-20,-5,-9,-5),(-19,-7,-8,-3),(-19,4,-13,3)]
    assert [onorm(v) for v in witnesses]==[-46,-18,-25]
    print('Field arithmetic: unit signatures',unit_signs,'Minkowski norms',[-46,-18,-25])
    data=[local_audit(p,r) for p,r in [(2,0),(2,1),(41,17),(41,24)]]
    realdata=[]
    for sr,ss in product([1,-1],repeat=2):
        roots=[(0,0,0,0),E2,E3]
        ordered=sorted(roots,key=cmp_to_key(lambda a,b:osign(oa(a,os(b,-1)),sr,ss)))
        t=os(oa(ordered[0],ordered[1]),F(1,2))
        allowed=int(osign(t,sr,ss)<0)|(int(osign(oa(t,os(E2,-1)),sr,ss)<0)<<1)
        codes=[int(osign(g,sr,ss)<0) for g in SG]
        masks=[]
        for j in range(256):
            v=0
            for k in range(8):
                if j>>k&1:v^=codes[k]
            masks.append(v)
        realdata.append((allowed,masks))
    solutions=[]
    for a in range(256):
        for b in range(256):
            if not all((masks[a]|(masks[b]<<bits)) in images for bits,images,masks in data):continue
            if not all((masks[a]|(masks[b]<<1)) in [0,allowed] for allowed,masks in realdata):continue
            solutions.append(a|(b<<8))
    solutions.sort()
    assert len(solutions)==32 and len(span(solutions))==32
    print('Kummer enumeration: exactly',len(solutions),'Kummer candidate classes.')
    return solutions

def pcurve(P0,a,b):
    x,y=P0;return pmul(y,y)==padd(padd(pmul(pmul(x,x),x),pmul(a,pmul(x,x))),pmul(b,x))
def pdouble(P0,a,b):
    x,y=P0;y2=pmul(y,y)
    # Independent closed expression for x(2P).
    numerator=padd(pmul(x,x),pneg(b))
    xx=pdiv(pmul(numerator,numerator),pscale(y2,4))
    slope=pdiv(padd(padd(pscale(pmul(x,x),3),pscale(pmul(a,x),2)),b),pscale(y,2))
    yy=padd(pmul(slope,padd(x,pneg(xx))),pneg(y))
    ans=(xx,yy);assert pcurve(ans,a,b)
    return ans

def fq(q,m):q=F(q);return q.numerator*pow(q.denominator,-1,m)%m
def modmul(a,b,m):return tuple(x%m for x in omul(a,b))
def det3(rows):
    a,b,c=rows
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def logs_and_chabauty():
    a,b=to_theta(D),to_theta(B);logs=[];m=2**16
    for name,point in zip(['P','Q','R'],[P,Q,R]):
        z=(to_theta(point[0]),to_theta(point[1]));assert pcurve(z,a,b)
        for k in range(4):z=pdouble(z,a,b)
        t=to_integral(pneg(pdiv(z[0],z[1])))
        assert all(q.denominator%2==1 and q.numerator%16==0 for q in t)
        tt=tuple(fq(q,m) for q in t)
        # log(t) = t + D*t^3/3 + O(t^5); t is in 16*O_{K,2}.
        # All later coefficients have odd denominators, hence the omitted
        # terms lie in 2^20*O and are zero modulo 2^16.
        t3=modmul(modmul(tt,tt,m),tt,m)
        correction=tuple(x*pow(3,-1,m)%m for x in modmul(D,t3,m))
        log=tuple((x+y)%m for x,y in zip(tt,correction));logs.append(log)
        print('Log16',name,'mod65536:',log)
    shifts=[5,5,4]
    for row,shift in zip(logs,shifts):assert all(x%2**shift==0 for x in row)
    mat=[[(x>>shift)%512 for x in row] for row,shift in zip(logs,shifts)]
    expected=[[427,100,180,352],[185,477,78,70],[385,461,290,468]]
    assert mat==expected
    cofs=[(-1)**j*det3([[row[k] for k in range(4) if k!=j] for row in mat]) for j in range(4)]
    assert all(c%2==0 for c in cofs) and any(c%4!=0 for c in cofs)
    ell=[(c//2)%256 for c in cofs]
    assert ell==[28,10,173,82]
    plog=[x%256 for x in logs[0]]
    rplog=modmul((-1,2,0,0),plog,256)
    constant=sum(a*b for a,b in zip(ell,rplog))%256
    assert constant==128
    assert ell[0]%8==4 and (-ell[0]+2*ell[1])%16==8
    print('Normalized log matrix mod512:',mat)
    print('Primitive annihilator mod256:',ell)
    print('Mixed-branch constant mod256:',constant)
    print('Both analytic inequalities in the proof apply.')
    return {'matrix_mod512':mat,'ell_mod256':ell,'mixed_constant_mod256':constant}

if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Run Python without -O or -OO: assertions are proof checks.')
    t=time.time();birational_identity();selmer=field_and_descent();data=logs_and_chabauty()
    print('ALL FINITE CERTIFICATES VERIFIED. Elapsed:',round(time.time()-t,3),'seconds.')
    data['selmer_candidates']=selmer
    path=filesystem.path.join(filesystem.path.dirname(__file__),'certificate_computed.json')
    with open(path,'w') as f:json.dump(data,f,indent=2)
