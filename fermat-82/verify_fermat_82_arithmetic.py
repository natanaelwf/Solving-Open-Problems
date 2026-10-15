#!/usr/bin/env python3
"""Arithmetic certificates for Rational Fourth Powers Summing to 82.

Python standard library only. The field basis is (1, sqrt(41), sqrt(2),
sqrt(82)). Checks the ten Kummer identities of Appendix A, the basis of
E(K)/2E(K) together with the upper bound proved in Section 5, the two
finite-field point counts of Section 9, and logarithms at 64 and 80 bits.
The local reduction and the analytic proof in Section 8 remain necessary.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path
import json
import time

class K:
    """An exact element of Q(r,s), r^2=41, s^2=2."""
    __slots__ = ('v',)
    def __init__(self, value=0):
        if isinstance(value, K):
            self.v = value.v
        elif isinstance(value, (tuple,list)):
            if len(value) != 4:
                raise ValueError('Exactly four field coordinates are required')
            self.v = tuple(map(F, value))
        else:
            self.v = (F(value), F(0), F(0), F(0))
    @classmethod
    def alpha(cls, values, denominator=1):
        """Read [a,b,c,d]/denominator in the manuscript's alpha basis."""
        a,b,c,d = (F(z,denominator) for z in values)
        return cls((a+b/2,b/2,c+d/2,d/2))
    def integral_coordinates(self):
        a,b,c,d=self.v
        return (a-b,2*b,c-d,2*d)
    def __add__(self, other):
        return K(tuple(a+b for a,b in zip(self.v,K(other).v)))
    __radd__=__add__
    def __neg__(self):return K(tuple(-a for a in self.v))
    def __sub__(self,other):return self+-K(other)
    def __rsub__(self,other):return K(other)+-self
    def __mul__(self,other):
        a,b,c,d=self.v;e,f,g,h=K(other).v
        return K((a*e+41*b*f+2*c*g+82*d*h,
                  a*f+b*e+2*c*h+2*d*g,
                  a*g+c*e+41*b*h+41*d*f,
                  a*h+d*e+b*g+c*f))
    __rmul__=__mul__
    def conj(self, r=False, s=False):
        a,b,c,d=self.v
        return K((a,-b if r else b,-c if s else c,
                  -d if r != s else d))
    def inv(self):
        other=self.conj(r=True)*self.conj(s=True)*self.conj(r=True,s=True)
        norm=self*other
        if norm.v[0] == 0:
            raise ZeroDivisionError('Zero field element')
        assert norm.v[1:] == (0,0,0)
        return K(tuple(a/norm.v[0] for a in other.v))
    def __truediv__(self,other):
        if isinstance(other,(int,F)):
            return K(tuple(a/other for a in self.v))
        return self*K(other).inv()
    def __rtruediv__(self,other):return K(other)*self.inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        ans=K(1);base=self
        while n:
            if n&1:ans=ans*base
            base=base*base;n//=2
        return ans
    def __eq__(self,other):return self.v==K(other).v

A=K.alpha
r=K((0,1,0,0));s=K((0,0,1,0));alpha=(1+r)/2
D=A([-68,13,45,-8]);B=A([2624,-656,-2132,533])
e2=D*(1+s);e3=D*(-2-s)
P=(A([164,-41,0,0]),A([-2132,574,-328,82]))
Q=(A([1100827,-297329,-777800,210120],36),
   A([2144893701,-579455603,-1516659202,409733998],216))
R=(A([70882,-16673,-48356,12854],392),
   A([38328084,-10524898,-27190638,7268179],10976))
T0=(K(0),K(0));T2=(e2,K(0))
generators=[K(-1),1+s,27+10*alpha,A([11,4,8,3]),3+alpha,s,r,A([1,1,2,1])]

def span(rows):
    ans={0}
    for row in rows:ans|={a^row for a in ans}
    return ans

def curve_check(point):
    x,y=point
    return y*y==x**3+D*x*x+B*x

def rep(mask):
    ans=K(1)
    for j,g in enumerate(generators):
        if mask>>j&1:ans=ans*g
    return ans

def kummer_certificate():
    data=[
        ('T0',T0,(33,161),(A([22,-3,-23,5]),A([6,-2,-2,1],2))),
        ('T2',T2,(160,2),(A([6,-2,-2,1],2),A([22,-3,-23,5]))),
        ('P',P,(16,166),(A([0,0,24,-7],2),A([63,-17,-26,7]))),
        ('Q',Q,(0,8),(A([575,-155,-396,104],6),A([899,-245,-723,197],6))),
        ('R',R,(14,0),(A([4584,-1242,-2690,729],28),A([176,-74,-110,27],28))),
    ]
    codes=[];out=[]
    for name,pt,masks,witnesses in data:
        assert curve_check(pt)
        x,y=pt
        if x==0:components=(e2*e3,-e2)
        elif x==e2:components=(e2,e2*(e2-e3))
        else:components=(x,x-e2)
        for z,mask,q in zip(components,masks,witnesses):
            assert z==rep(mask)*q*q, (name,mask)
        code=masks[0]+256*masks[1]
        codes.append(code)
        print(f'Exact Kummer identities {name}: masks={masks}, pair code={code}')
        out.append({'point':name,'component_masks':masks,'pair_code':code})
    assert len(span(codes))==32
    assert span(codes)==span([14,672,1425,2048,41249])
    assert 42512^41249^672==1425
    print('Five independent Kummer images span all 32 candidate classes.')
    return out

def rational_mod(q,p):
    q=F(q)
    return q.numerator*pow(q.denominator,-1,p)%p

def reduction_certificate():
    out=[]
    for p,rv,sv,expected in [(23,8,18,28),(31,14,8,40)]:
        assert rv*rv%p==41%p and sv*sv%p==2%p
        def ev(x):
            return sum(rational_mod(a,p)*b for a,b in zip(x.v,[1,rv,sv,rv*sv]))%p
        d,b=ev(D),ev(B)
        discriminant=16*b*b*(d*d-4*b)%p
        assert discriminant!=0
        # Count each affine pair, not just square classes; include infinity.
        counts=[sum((y*y-x*x*x-d*x*x-b*x)%p==0 for y in range(p)) for x in range(p)]
        order=1+sum(counts)
        assert order==expected
        print(f'Good reduction p={p}, r={rv}, s={sv}: D={d}, B={b}, order={order}')
        out.append({'p':p,'r':rv,'s':sv,'D':d,'B':b,'discriminant':discriminant,
                    'point_count':order,'counts_by_x':counts})
    assert gcd(out[0]['point_count'],out[1]['point_count'])==4
    assert out[1]['point_count']%23!=0 and out[0]['point_count']%31!=0
    print('Reduction certificate bounds global torsion order by 4; full 2-torsion attains 4.')
    return out

def double(point):
    x,y=point
    if y==0:raise ValueError('Doubling a 2-torsion point is not used here')
    slope=(3*x*x+2*D*x+B)/(2*y)
    xx=slope*slope-D-2*x
    yy=slope*(x-xx)-y
    assert xx==(x*x-B)**2/(4*y*y)
    assert curve_check((xx,yy))
    return xx,yy

def v2(q):
    q=F(q)
    if not q:return 10**9
    def val(n):
        n=abs(n)
        return (n&-n).bit_length()-1
    return val(q.numerator)-val(q.denominator)

def trunc(x,modulus):
    # Reducing alpha-basis coordinates keeps track of the integral lattice.
    return A([rational_mod(c,modulus) for c in x.integral_coordinates()])

def det3(rows):
    a,b,c=rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def formal_log_certificate(bits=64):
    modulus=2**bits;logs=[]
    for name,point in [('P',P),('Q',Q),('R',R)]:
        z=point
        for _ in range(4):z=double(z)
        t=-z[0]/z[1]
        assert min(v2(c) for c in t.integral_coordinates())>=4
        tt=trunc(t,modulus);tt2=trunc(tt*tt,modulus)
        power=tt;log=K(0)
        # All c_j are integral, and 2j+1 is odd. Thus omitted terms
        # are in 2^bits O whenever 4(2j+1) >= bits.
        j=0
        while 4*(2*j+1)<bits:
            cj=sum((comb(j,2*i)*comb(2*i,i)*D**(j-2*i)*B**i
                    for i in range(j//2+1)),K(0))
            log=trunc(log+trunc(cj,modulus)*power/(2*j+1),modulus)
            power=trunc(power*tt2,modulus);j+=1
        row=[int(a) for a in log.integral_coordinates()]
        logs.append(row)
        print(f'Log(16{name}) mod 2^{bits}: {row}')
    assert [[a%65536 for a in row] for row in logs]==[
        [13664,35968,5760,60416],[38688,64416,2496,35008],[63504,7376,4640,23872]]
    # Retain bits-5 digits in M; cofactor normalization loses one digit.
    normalized_modulus=2**(bits-5)
    matrix=[]
    for row,div in zip(logs,[32,32,16]):
        assert all(a%div==0 for a in row)
        matrix.append([a//div%normalized_modulus for a in row])
    cof=[(-1)**j*det3([[row[k] for k in range(4) if k!=j] for row in matrix]) for j in range(4)]
    assert min(v2(c) for c in cof)==1
    ell=[c//2%(normalized_modulus//2) for c in cof]
    assert [c%256 for c in ell]==[28,10,173,82]
    rp=(r*A(logs[0])).integral_coordinates()
    constant=sum(a*c for a,c in zip(ell,rp))%(normalized_modulus//2)
    assert v2(constant)==7
    assert v2(ell[0])==2 and v2(-ell[0]+2*ell[1])==3
    return {'bits':bits,'logs':logs,'normalized_matrix':matrix,'annihilator':ell,
            'mixed_branch_constant':int(constant),'constant_valuation':v2(constant)}

def run():
    start=time.perf_counter()
    assert r*r==41 and s*s==2 and alpha*alpha==alpha+10
    assert B==D*D*(-4-3*s) and e2+e3==-D and e2*e3==B
    out={'kummer':kummer_certificate(),'reductions':reduction_certificate()}
    lo=formal_log_certificate(64);hi=formal_log_certificate(80)
    assert [[a%(2**64) for a in row] for row in hi['logs']]==lo['logs']
    assert [a%(2**58) for a in hi['annihilator']]==lo['annihilator']
    out['logs_64']=lo;out['logs_80']=hi
    out['elapsed_seconds']=round(time.perf_counter()-start,3)
    output=Path(__file__).with_name('additions_computed.json')
    output.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('ALL ADDITIONAL FINITE CERTIFICATES PASSED.')
    print('The local reduction and analytic proof in Section 8 remain necessary.')
    print(f"Elapsed: {out['elapsed_seconds']} s")
    return out

if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Do not run with -O or -OO: assertions are certificate checks.')
    run()
