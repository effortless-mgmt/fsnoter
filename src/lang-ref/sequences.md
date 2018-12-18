## Sequences (seq)

A _sequence expression_ is an expression that evaluates to a sequence. It can be used to create lists. The following code creates a list which ranges from 0 to 10.

```fsharp
// Creates a list from 0 to 10.
seq { 0 .. 10 }
val it: seq<int> = seq [ 0; 1; 2; 3; ... ]
```

You can make a sequence with a specific increment as well.

```fsharp
// Creates  a list from 0 to 100 incremented by 10.
seq { 0 .. 10 .. 100 }
val it: seq<int> = seq [ 0; 10; 20; 30; ... ]
```

You can also do an operation for each number in the sequence.

```fsharp
// Creates a list from 0 to 10, and multiplies each value with itself
seq { for i in 0 .. 10 do yield i * i }
val it: seq<int> = seq [ 1; 4; 9; 16; ... ]
```

You can use `->` operator instead of `yield`, in whch case you can omit the `do` keywork, as shown in the following example.

```fsharp
seq { for i in 1 .. 10 -> i * i }
```

You can also use `if`-statements. Given a function `isprime` of type `int -> bool`

```fsharp
let isprime n =
    let rec check i =
        i > n/2 || (n % i <> 0 && check (i + 1))
    check 2
val isprime : n:int -> bool
```

You can make a sequence only consisting of prime numbers.

```fsharp
seq { for n in 1 .. 100 do if isprime n then yield n}
val it : seq<int> = seq[1; 2; 3; 5; 7; 11; ...]
```
