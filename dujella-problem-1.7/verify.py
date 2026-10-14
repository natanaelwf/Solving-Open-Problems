#!/usr/bin/env python3
"""Exact-arithmetic audit checks for the accompanying D(n)-quadruple manuscript.

Python 3.10+; SymPy is needed only for --symbolic / --full.
Finite tests are not proofs of asymptotic estimates, uniformity, or novelty.
The code was written for this review; it is not the unavailable original script.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import combinations
import json
from math import gcd, isqrt
from pathlib import Path
import platform
import time


def require(condition: bool, message: object) -> None:
    """Do not lose checks when Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def factors(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError('factorization requires a positive integer')
    result: dict[int, int] = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def divisors(n: int) -> list[int]:
    out = [1]
    for p, e in factors(n).items():
        old = list(out)
        power = 1
        for _ in range(e):
            power *= p
            out.extend(d*power for d in old)
    return out


def icbrt(n: int) -> int:
    if n < 0:
        raise ValueError('cube-root input must be nonnegative')
    lo, hi = 0, 1 << ((n.bit_length()+2)//3)
    while lo < hi:
        mid = (lo+hi+1)//2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid-1
    return lo


def G(p: int, w: int) -> Fraction:
    return Fraction(1) if w <= 0 else Fraction(3, (p+1)*p**(w-1))


def local_factor(p: int, e: int) -> Fraction:
    if e < 0:
        raise ValueError('negative valuation')
    if p == 2:
        return Fraction(1, 2**(e+1)) + sum(
            (Fraction(1, 2**(j+1))*G(2, e-1-(3*j)//2) for j in range(e+1)),
            Fraction(0))
    return Fraction(1, p**e) + sum(
        (Fraction(p-1, p**(j+1))*G(p, e-(3*j)//2) for j in range(e)),
        Fraction(0))


def density(k: int) -> Fraction:
    if k < 1:
        raise ValueError('k must be positive')
    ans = Fraction(1)
    for p, e in factors(k).items():
        ans *= local_factor(p, e)
    return ans


def reduced_parameters(a: int, b: int, r: int, k: int) -> tuple[int, ...]:
    ell = gcd(gcd(a, b), gcd(r-k, r+k))
    s = gcd(a, r-k)//ell
    u, v = a//(ell*s), (r-k)//(ell*s)
    t = (r+k)//(ell*u)
    require((a, r-k, r+k, b) == (ell*u*s, ell*v*s, ell*u*t, ell*v*t),
            ('rank-one factorization', a,b,r,k))
    require(gcd(u,v) == gcd(s,t) == 1, ('primitive vectors', a,b,r,k))
    sigma = 1
    if (u,v) > (s,t):
        u,v,s,t = s,t,u,v
        sigma = -1
    require((u,v) < (s,t), ('lexicographic reduction', a,b,r,k))
    m = 2*sigma*k//ell
    require(ell*(u*t-v*s) == 2*sigma*k and r == ell*v*s+sigma*k,
            ('signed determinant', a,b,r,k))
    return ell,sigma,u,v,s,t,m


def audit_quad(n: int, quad: tuple[int,int,int,int]) -> None:
    a,b,c,d = quad
    M = abs(n)
    require(0 < a < b < c < d and all(square(A*B+n) for A,B in combinations(quad,2)),
            ('invalid quadruple', n,quad))
    for A,B,C in combinations(quad,3):
        r,s,t = isqrt(A*B+n),isqrt(A*C+n),isqrt(B*C+n)
        e = n*(A+B+C)+2*A*B*C-2*r*s*t
        require(A*e+n*n == (A*t-r*s)**2 and
                B*e+n*n == (B*s-r*t)**2 and
                C*e+n*n == (C*r-s*t)**2, ('triple invariant', n,quad))
        require(e*(n*(A+B+C)+2*A*B*C+2*r*s*t) ==
                n*n*((C-A-B)**2-4*(A*B+n)), ('invariant product', n,quad))
        if A*B >= 3*M and C > M*M and C != A+B+2*r:
            require(e >= 1 and e*A*B <= M*M*C and M*M*C >= A*B,
                    ('irregular triple bounds', n,quad))
    x,y,z = isqrt(a*d+n),isqrt(b*d+n),isqrt(c*d+n)
    q = z-x-y
    P = (q*q-n)*(q*q-9*n)
    require(P % d == 0, ('defect divisibility', n,quad))
    r = isqrt(a*b+n)
    if c == a+b+2*r:
        require(q != 0 and q*q*a*b*c <= 25*M*M*d, ('root defect bound', n,quad))
        require(2*(r*x-a*y-q*(a+r))*(x+q) == (n-q*q)*(a+2*r),
                ('defect factorization', n,quad))
        if q*q == n:
            require(q > 0 and d*n == 4*r*(a+r)*(b+r), ('principal family', n,quad))
        if not square(n):
            require(P != 0 and d <= abs(P), ('nonzero defect multiple', n,quad))
            require(d*625*M**4*(M+1)*(9*M+1) >= (a*b*c)**2,
                    ('nonsquare gap', n,quad))
    t = isqrt(b*c+n)
    if d == b+c+2*t:
        require(a*b <= 25*M*M and d < 10**4*M**3, ('largest regular triple', n,quad))
        vv,ww = isqrt(a*c+n),isqrt(a*d+n)
        h = ww-vv
        eta = h*h-a*b
        require(eta != 0 and eta*(4*a*c+4*h*vv+eta) == 4*n*(a*a-h*h),
                ('largest-triple identity', n,quad))


def principal(k: int, N: int, check: bool = True) -> set[tuple[int,int,int,int]]:
    if k < 1 or N < 1:
        raise ValueError('positive k and N required')
    out: set[tuple[int,int,int,int]] = set()
    # d > 4*r^3/k^2 gives a rigorous finite cutoff. No floating-point roots.
    for r in range(k+1, icbrt(k*k*N//4)+1):
        prod = (r-k)*(r+k)
        for a in divisors(prod):
            b = prod//a
            if a >= b:
                continue
            num = 4*r*(a+r)*(b+r)
            if num > k*k*N or num % (k*k):
                continue
            c,d = a+b+2*r,num//(k*k)
            quad = a,b,c,d
            require(quad not in out, ('duplicate principal object', k,N,quad))
            out.add(quad)
            if check:
                audit_quad(k*k,quad)
                ell,sigma,u,v,s,t,m = reduced_parameters(a,b,r,k)
                Z = Fraction(s,u)
                eta1 = Fraction(m,2*u*v)
                eta2 = Fraction(m,2*u*(u+v))
                eta3 = Fraction(m*(2*v+u),2*u*v*(u+v))
                require(Fraction(4*ell**3,k*k)*(u*v*(u+v))**2*
                        (Z+eta1)*(Z+eta2)*(Z+eta3) == d, ('exact height', k,quad))
    return out


def enumerate_quads(n: int, N: int) -> set[tuple[int,int,int,int]]:
    if n == 0 or N < 1:
        raise ValueError('nonzero n and positive N required')
    adj = [set() for _ in range(N+1)]
    for a in range(1,N):
        for b in range(a+1,N+1):
            if square(a*b+n):
                adj[a].add(b)
    out = set()
    for a in range(1,N):
        for b in adj[a]:
            common = adj[a] & adj[b]
            for c in common:
                for d in common & adj[c]:
                    quad = (a,b,c,d)
                    audit_quad(n,quad)
                    out.add(quad)
    return out


def graph_checks(radius: int, height: int) -> dict[str,object]:
    counts = {}
    total = regular_small = regular_large = zero_roots = 0
    for n in range(-radius,radius+1):
        if not n:
            continue
        quads = enumerate_quads(n,height)
        counts[str(n)] = len(quads)
        total += len(quads)
        for a,b,c,d in quads:
            regular_small += c == a+b+2*isqrt(a*b+n)
            regular_large += d == b+c+2*isqrt(b*c+n)
            zero_roots += any(A*B+n == 0 for A,B in combinations((a,b,c,d),2))
        if square(n):
            k = isqrt(n)
            subfamily = {q for q in quads if q[2] == q[0]+q[1]+2*isqrt(q[0]*q[1]+n)
                         and q[3]*n == 4*isqrt(q[0]*q[1]+n)*
                         (q[0]+isqrt(q[0]*q[1]+n))*(q[1]+isqrt(q[0]*q[1]+n))}
            require(subfamily == principal(k,height), ('principal vs graph', k,height))
    return dict(radius=radius,height=height,total=total,regular_small=regular_small,
                regular_large=regular_large,with_zero_root=zero_roots,counts=counts)


def bezout(a: int, b: int) -> tuple[int,int,int]:
    old_r,r,old_s,s,old_t,t = a,b,1,0,0,1
    while r:
        q = old_r//r
        old_r,r = r,old_r-q*r
        old_s,s = s,old_s-q*s
        old_t,t = t,old_t-q*t
    return old_r,old_s,old_t


def residue_density(k: int) -> tuple[Fraction,dict[str,int]]:
    """Direct global-modulus count (6.7), without using local valuation criteria."""
    Q = 2*k*k
    ds = sorted(divisors(2*k))
    counts = {ell:0 for ell in ds}
    for u in range(Q):
        for v in range(Q):
            if gcd(gcd(u,v),Q) != 1:
                continue
            g,alpha,beta = bezout(u,v)
            inv = pow(g,-1,Q)
            alpha,beta = alpha*inv,beta*inv
            for ell in ds:
                m = 2*k//ell
                s,t = (-beta*m)%Q,(alpha*m)%Q
                for _ in range(Q):
                    if gcd(gcd(s,t),m) == 1:
                        A,B,R = ell*u*s,ell*v*t,ell*v*s+k
                        if 4*R*(A+R)*(B+R) % (k*k) == 0:
                            counts[ell] += 1
                    s,t = (s+u)%Q,(t+v)%Q
    norm = Fraction(1,Q**3)
    for p in factors(Q):
        norm *= Fraction(p*p,p*p-1)
    result = norm*sum((Fraction(counts[ell],ell) for ell in ds),Fraction(0))
    return result,{str(ell):count for ell,count in counts.items()}


def symbolic_checks() -> dict[str,object]:
    try:
        import sympy as S
    except ImportError as exc:
        raise RuntimeError('Symbolic checks require SymPy: python -m pip install sympy') from exc
    a,b,c,d,n,r,s,t,x,y,z,q,k,u,v,ell,Z,m = S.symbols('a b c d n r s t x y z q k u v ell Z m')
    names = []
    def zero(name, expression, rules=()):
        expression = S.expand(expression)
        for variable, replacement in rules:
            expression = S.rem(expression,variable**2-replacement,variable)
        require(S.simplify(expression) == 0, ('symbolic',name,expression))
        names.append(name)
    e = n*(a+b+c)+2*a*b*c-2*r*s*t
    rules = [(r,a*b+n),(s,a*c+n),(t,b*c+n)]
    zero('invariant_a',a*e+n*n-(a*t-r*s)**2,rules)
    zero('invariant_b',b*e+n*n-(b*s-r*t)**2,rules)
    zero('invariant_c',c*e+n*n-(c*r-s*t)**2,rules)
    zero('invariant_product',e*(n*(a+b+c)+2*a*b*c+2*r*s*t)-n*n*((c-a-b)**2-4*(a*b+n)),rules)
    ee = S.symbols('ee')
    ceqn = (n*(a+b)+(n+2*a*b)*c-ee)**2-4*(a*b+n)*(a*c+n)*(b*c+n)
    zero('quadratic_coefficient',S.expand(ceqn).coeff(c,2)-n*n)
    W = 2*x*y+2*q*(x+y)+q*q-2*r*d+n
    F = 2*(r*x-a*y-q*(a+r))*(x+q)-(n-q*q)*(a+2*r)
    zero('defect_factorization',F-(2*r*(x*x-a*d-n)-a*W))
    zero('zero_defect_quadratic',(2*r*d-n)**2-4*(a*d+n)*(b*d+n)-
         4*n*(d*d-(a+b+r)*d-3*n/4),[(r,a*b+n)])
    c0 = a+b+2*r
    d0 = 4*r*(a+r)*(b+r)/(k*k)
    for name,entry,root in [
        ('principal_a',a,(2*a*(b+r)+k*k)/k),
        ('principal_b',b,(2*b*(a+r)+k*k)/k),
        ('principal_c',c0,(2*(a+r)*(b+r)+k*k)/k)]:
        zero(name,S.expand(k*k*(root**2-entry*d0-k*k)),[(r,a*b+k*k)])
    A,B,R = ell*u*u*Z,ell*v*v*Z+ell*v*m/u,ell*u*v*Z+ell*m/2
    eta1,eta2,eta3 = m/(2*u*v),m/(2*u*(u+v)),m*(2*v+u)/(2*u*v*(u+v))
    zero('height_factorization',4*R*(A+R)*(B+R)-4*ell**3*(u*v*(u+v))**2*(Z+eta1)*(Z+eta2)*(Z+eta3))
    qq = z-x-y
    zero('defect_divisibility',(qq**2-n)*(qq**2-9*n),[(x,n),(y,n),(z,n)])
    h,V,T = S.symbols('h V T')
    eta = h*h-a*b
    expr = eta*(4*a*c+4*h*V+eta)-4*n*(a*a-h*h)
    expr = S.rem(S.expand(expr),h*h+2*h*V-a*(b+2*T),h)
    zero('largest_regular_triple_identity',expr,[(V,a*c+n),(T,b*c+n)])
    # Existing Dujella--Petricevic (2019) family: check every square and
    # upper-regularity. These checks support the comparison in Appendix A.
    H = S.symbols('H')
    B = 256*H**4-128*H**3-48*H**2+16*H
    C = 4096*H**6-4096*H**5-512*H**4+1152*H**3+16*H**2-88*H-7
    D = 4096*H**6-2048*H**5-1792*H**4+640*H**3+288*H**2-48*H-15
    nn = -64*H**2+16*H+16
    roots = [
        (1,B,4*(4*H**2-H-1)),
        (1,C,64*H**3-32*H**2-12*H+3),
        (1,D,64*H**3-16*H**2-16*H+1),
        (B,C,4*(4*H**2-H-1)*(64*H**3-32*H**2-4*H+1)),
        (B,D,4*(4*H**2-H-1)*(64*H**3-16*H**2-8*H+1)),
        (C,D,4096*H**6-3072*H**5-1280*H**4+960*H**3+176*H**2-76*H-11)]
    for idx,(AA,BB,root) in enumerate(roots,1):
        zero(f'existing_family_square_{idx}',AA*BB+nn-root**2)
    zero('existing_family_upper_regular',D-B-C-2*roots[3][2])
    zero('existing_family_regular_identity',((D-B-C)/2)**2-B*C-nn)
    return {'sympy_version':S.__version__,'identities':names,'count':len(names)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full',action='store_true',help='all reported checks, including k<=9 global residues')
    parser.add_argument('--symbolic',action='store_true',help='run exact symbolic identities')
    parser.add_argument('--graphs',action='store_true',help='enumerate all n in [-100,100] except zero, height 500')
    parser.add_argument('--principal',action='store_true',help='check six principal-family counts at height 10^9')
    parser.add_argument('--residue-max',type=int,default=0,help='direct global residue tests for 1<=k<=this number')
    parser.add_argument('--output',type=Path,default=Path('verification_results.json'))
    args = parser.parse_args()
    if args.residue_max < 0:
        parser.error('--residue-max must be nonnegative')
    if not (args.full or args.symbolic or args.graphs or args.principal or args.residue_max):
        parser.error('choose --full or one or more test groups')
    start=time.perf_counter()
    result:dict[str,object] = {'python_version':platform.python_version(),
        'notice':'Finite exact tests, not a proof or a certification of novelty.'}
    if args.full or args.symbolic:
        result['symbolic'] = symbolic_checks()
        print('Symbolic identities: PASS',flush=True)
    if args.full or args.graphs:
        result['graphs'] = graph_checks(100,500)
        require(result['graphs']['total'] == 613, 'original reported total differs')
        print('Graph enumeration: 613 quadruples, PASS',flush=True)
    if args.full or args.principal:
        expected={1:3620,2:6178,3:6368,4:10652,5:6140,8:12448}
        rows=[]
        for k,expect in expected.items():
            count=len(principal(k,10**9))
            require(count == expect, ('principal count differs', k,count,expect))
            rows.append({'k':k,'N':10**9,'delta':str(density(k)),'count':count})
            print(f'Principal k={k}: {count}, PASS',flush=True)
        result['principal']=rows
    maxk = max(args.residue_max,9 if args.full else 0)
    if maxk:
        rows=[]
        for k in range(1,maxk+1):
            value,counts = residue_density(k)
            require(value == density(k), ('residue/local mismatch',k,value,density(k)))
            rows.append({'k':k,'Q':2*k*k,'global_density':str(value),'T':counts})
            print(f'Global residue k={k}: {value}, PASS',flush=True)
        result['global_residues']=rows
    result['local_factor_table']={str(p):[str(local_factor(p,e)) for e in range(5)] for p in (2,3,5,7)}
    result['elapsed_seconds']=round(time.perf_counter()-start,3)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'All requested checks passed. Results: {args.output}',flush=True)

if __name__ == '__main__':
    main()
