# Noter til funktionsprogrammering 2018 DTU

Bla.

## F# Syntax highlitingtest:

```fsharp
let rec toCount (os: Observation list) : Count<Species> = 
    match os with
    | (s, _, _) :: tail -> insert s (toCount tail)
    | [] -> []
    ;;

toCount os;;
```
