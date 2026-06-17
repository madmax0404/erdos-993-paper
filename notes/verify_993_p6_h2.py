"""Exact verification of every step of the P6(h=2) proof
(notes/993_p6_h2_proof.md) for c <= 200, all k, plus the E-core
empirics with general vertex backgrounds."""
import sys, json
from pathlib import Path
from math import comb
from fractions import Fraction
REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
from erdos993.indpoly import mul

def binp(c,b): return tuple(comb(c,k)*b**k for k in range(c+1))
def cf(p,k): return p[k] if 0 <= k < len(p) else 0

ok = {"step1": True, "step2": True, "core": True, "vertices": True}
for c in range(1, 201):
    E = binp(c,2); b = tuple([0]+list(binp(c,1)))
    bE = mul(b,E); bb = mul(b,b); EE = mul(E,E)
    H2 = tuple(cf(E,m)+2*cf(b,m) for m in range(c+2))
    for k in range(0, 2*c+3):
        T = cf(bE,k); Cb = comb(2*c,k-1) if 0 <= k-1 <= 2*c else 0
        if 2*T*T < 2**k * Cb*Cb: ok["step1"] = False
        if k >= 2 and k <= 2*c and comb(2*c,k-1)**2 < comb(2*c,k-2)*comb(2*c,k): ok["step2"] = False
        if cf(bb,k)*cf(EE,k) > 2*T*T: ok["core"] = False
    for X, Y in ((E,E),(E,H2),(H2,H2)):
        XY = mul(X,Y); bX = mul(b,X); bY = mul(b,Y)
        for k in range(0, 2*c+4):
            if cf(bb,k)*cf(XY,k) > 2*cf(bX,k)*cf(bY,k): ok["vertices"] = False
print(ok)
(REPO/"logs"/"993_p6_h2_proof_check.json").write_text(json.dumps(ok, indent=2))
assert all(ok.values())
print("P6(h=2) proof chain verified exactly for c <= 200, all k")
