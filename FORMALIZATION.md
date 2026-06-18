# Lean Formalization

This repository includes a Lean 4 project for mechanically checked statements
that support the paper formalization effort.

Run:

```bash
lake build
uv run python scripts/check_formalization.py
```

The project is pinned by `lean-toolchain` and currently uses only Lean core.
The formal files define coefficient sequences, convolution, log-concavity
predicates, binomial coefficients, and the hub-spider coefficient formula used
as the target interface for later analytic lemmas.

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

## Remaining Formalization Work

The manuscript's main theorem and the soundness of the Python certificate
checkers have not yet been translated into Lean. The present Lean project is a
checked foundation and build gate, not a completed formal proof of the paper.

The manuscript also contains conjectural all-parameter certificate statements.
Those cannot be theorem-prover verified as theorems without new mathematics;
the formal target for the published unconditional result is the finite
scope theorem together with a verified certificate checker for the exact
artifact format.
