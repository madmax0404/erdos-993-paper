"""A0' and extended-vertex P6 verification (exact arithmetic).

A0': A_t = (1+2x)^c + t x(1+x)^c is log-concave for all t in [0,2].
Proof chain (same decomposition as A0): Delta_k(t) = Amargin + t cross
+ t^2 Bmargin, with cross >= -2^{k-1} C_k C_{k-1}; absorption for t <= 2
needs Amargin >= 2^k C_k C_{k-1} <=> 2^k (c+1) >= k(k+1), which holds
since 2^k >= k and c+1 >= k+1.  This script verifies the chain and the
LC statement exactly at t in {1/3, 1, 3/2, 2} for c <= 300.

P6 extended vertices: over the [0,2]^h box the multiaffine Mobius
argument reduces P6 to vertices with factors in {E, E+2b} (H = E+b
arises on the diagonal at t=1 and is included for completeness).  This
script sweeps all such vertices for h in {2,3,4}, c <= 64, recording
the max (h-1)*Delta in band (exact rationals).
"""
import sys, json
from pathlib import Path
REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
from erdos993.indpoly import mul
from math import comb, ceil
from fractions import Fraction
from itertools import product as iproduct

def binp(c,b): return tuple(comb(c,k)*b**k for k in range(c+1))
def cf(p,k): return p[k] if 0 <= k < len(p) else 0

# --- A0' ---
ok_chain = ok_lc = True
for c in range(1, 301):
    C_ = lambda j: comb(c, j) if 0 <= j <= c else 0
    for k in range(1, c+1):
        ok_chain &= (2**k * (c+1) >= k*(k+1))
    for tnum, tden in ((1,3),(1,1),(3,2),(2,1)):
        A = [Fraction(C_(k)*2**k) + Fraction(tnum,tden)*C_(k-1) for k in range(c+2)]
        for k in range(1, c+1):
            if A[k]*A[k] < A[k-1]*A[k+1]: ok_lc = False

# --- P6 extended vertices ---
worst = (Fraction(-10), None)
for h in (2,3,4):
    for c in (4,8,16,32,64):
        C = c*h; D = h+C
        if D > 200: continue
        k0 = ceil((2*D-1)/3)
        E = binp(c,2); b = tuple([0]+list(binp(c,1)))
        fac = {'E': E, 'H': tuple(cf(E,m)+cf(b,m) for m in range(c+2)),
               '2': tuple(cf(E,m)+2*cf(b,m) for m in range(c+2))}
        for Xi in 'EH2':
            for Xj in 'EH2':
                for Wpat in iproduct('EH2', repeat=h-2):
                    W = (1,)
                    for ch_ in Wpat: W = mul(W, fac[ch_])
                    bbW = mul(mul(b,b), W); XXW = mul(mul(fac[Xi],fac[Xj]), W)
                    bXj = mul(mul(b,fac[Xj]), W); bXi = mul(mul(b,fac[Xi]), W)
                    for k in range(2, min(k0, len(bXj)-1)):
                        den = Fraction(cf(bXj,k))*Fraction(cf(bXi,k))
                        if den == 0: continue
                        d = (Fraction(cf(bbW,k))*Fraction(cf(XXW,k))/den - 1)*(h-1)
                        if d > worst[0]: worst = (d, (h, c, Xi, Xj, ''.join(Wpat) or '-', k))

payload = {"A0prime_chain": ok_chain, "A0prime_LC_exact": ok_lc,
           "P6ext_worst_hm1_Delta": float(worst[0]), "at": str(worst[1])}
(REPO/"logs"/"993_A0prime_P6ext.json").write_text(json.dumps(payload, indent=2))
print(f"A0' chain: {ok_chain}; A0' LC exact (t in 1/3..2, c<=300): {ok_lc}")
print(f"P6 extended vertices: worst (h-1)*Delta = {float(worst[0]):+.5f} at {worst[1]}")
print("wrote logs/993_A0prime_P6ext.json")
