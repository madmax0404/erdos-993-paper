import Lake
open Lake DSL

package «erdos993-paper» where
  version := v!"0.1.0"

@[default_target]
lean_lib Erdos993Formal where
  srcDir := "formal"
