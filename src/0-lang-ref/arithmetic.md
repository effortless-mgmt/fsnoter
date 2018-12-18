## Operators

This section covers the arithmetic and logic (boolean) operators.

### Binary Arithmetic Operators

The arithmetic operators in F# are as following:

| Operator | Notes |
|---|---|
| `+` | Addition, Plus. `3+ 2 ~> 5`. |
| `-` | Subtraction, Minus. `3 - 2 ~> 1`. |
| `*` | Multiplication. `3 * 2 ~> 6`. |
| `/` | Division. `3 / 2 ~> 1.5`. |
| `%` | Modulus, Remainder. `3 % 2 ~> 1` `4 % 2 ~> 0`. |
| `**` | Exponent, Power of. `2**16 ~> 65535`. |

### Binary Comparison Operators

Binary comparison operators are used to compare values to each other. It returns either `true` or `false`:

| Operator | Notes |
| --- | --- |
| `=` | Equality, Equals. `2 = 2 ~> true` `2 = 3 ~> false` |
| `>` | Greater than. |
| `<` | Less than. |
| `>=` | Greater than or equal to. |
| `<=` | Less than or equal to. |
| `<>` | Not equal, Different from. `2 <> 2 ~> false` `2 <> 3 ~> true` `4 % 2 <> 0 ~> false` |
