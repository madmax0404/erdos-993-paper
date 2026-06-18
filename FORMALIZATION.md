# Lean Formalization

This repository includes a Lean 4 project for mechanically checked statements
that support the paper formalization effort.

Run:

```bash
lake build
uv run python scripts/check_formalization.py
```

The project is pinned by `lean-toolchain` and `lake-manifest.json`.  The formal
files define coefficient sequences, convolution, log-concavity predicates,
binomial coefficients, and the hub-spider coefficient formula used as the
target interface for later analytic lemmas.

The guard script rejects `sorry`, `admit`, and `axiom` in `formal/**/*.lean`.
That keeps the checked Lean surface honest: every theorem currently in the
formal directory is kernel-checked without placeholders.

## Current Mechanized Surface

| Lean artifact | Checked content |
| --- | --- |
| `formal/Erdos993Formal/Basic.lean` | coefficient sequences, addition, `x` multiplication, finite convolution |
| `formal/Erdos993Formal/Basic.lean` | log-concavity and one-step monotonicity predicates |
| `formal/Erdos993Formal/Basic.lean` | recursive binomial coefficients and the `E`, `b`, `H` hub-arm coefficient sequences |
| `formal/Erdos993Formal/Basic.lean` | the hub-spider product-plus-root coefficient formula |
| `formal/Erdos993Formal/CertificateAlgebra.lean` | the `t`-cancellation determinant identity |
| `formal/Erdos993Formal/CertificateAlgebra.lean` | monotonicity of cross-bracket products under nonnegative flow |
| `formal/Erdos993Formal/PolynomialCertificate.lean` | soundness of Taylor-shift polynomial nonnegativity certificates |
| `formal/Erdos993Formal/Generated/Ecore.lean` | 996 Lean-checked vertex-background E-core Taylor-shift certificate instances, generated from the committed E-core certificate logs |

## Remaining Formalization Work

The manuscript's main theorem and all Python certificate checkers have not yet
been fully translated into Lean. The present Lean project now checks the
generic polynomial-certificate soundness theorem and the 996 generated
vertex-background E-core certificate instances, but it is not yet a completed
formal proof of every manuscript reduction and certificate family.

The manuscript also contains conjectural all-parameter certificate statements.
Those cannot be theorem-prover verified as theorems without new mathematics;
the formal target for the published unconditional result is the finite scope
theorem together with exported Lean certificate data for the exact artifact
format.

Use `scripts/export_ecore_poly_certificate.py` to export one vertex-background
E-core polynomial certificate in the Taylor-shift format checked by
`PolynomialCertificate.lean`.
Use `scripts/generate_ecore_lean_certificates.py` to regenerate the committed
Lean vertex-background E-core certificate instances.
