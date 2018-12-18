## Tail Recursion and Continuation-based Tail Recursion

Consider the following example:

```fsharp
let rec sum xs = 
    match xs with
    | [] -> 0
    | x::rest -> x + sum rest
val : int list -> int
```

To evaluate `sum [1;2;3]`, you have to go down the recursion tree, and then sum all the way up before you get the result:

```
sum [1; 2; 3]
~> 1 + sum [2; 3]
~> 1 + sum [2; 3] + sum [3]
~> 1 + sum [2; 3] + sum [3] + sum []
~> 1 + sum [2; 3] + sum [3] + 0
~> 1 + sum [2; 3] + 3 + 0
~> 1 + 2 + 3 + 0
~> 6
```

To minimize computations, we can use tail recursion:

```fsharp
let rec sumT xs n =
    match xs with
    | [] -> n
    | x::rest -> sumT rest (x + n)
val : int list -> int -> int
```

In this case the computation would be:

```
sum [1; 2; 3] 0
~> sum [2; 3] (1 + 0)
~> sum [3] (2 + 1)
~> sum [] (3 + 3)
~> 6
```

A tail recursive function is **slower** than a normal recursive function, though the data gets placed on the heap rather than the stack, and can thus hold much more values without throwing a stackoverflow exception. The stack holds 120.000 lines, the heap holds 12.000.000 lines.

The tail recursive function does not though function with recursive types, *trees*. For these you need a **continuation-based tail recursion**. Instead of the `n` in the tail recursion, it takes in a function:

```fsharp
let rec SumC xs f =
    match xs with
    | [] -> f 0
    | x::rest -> sumC rest (fun i -> f(x + i))
val : int list -> (int -> 'a) -> (int -> 'a)
```

Here the computation is:

```
sumC [1;2;3] id
~> sumC [2;3] (fun v -> id(1+v))
~> sumC [3] (fun w -> (fun v -> id(1+v))(2+w))
~> sumC [] (fun u -> (fun w -> (fun v -> id(1+v))(2+w))(3+u))
~> (fun u -> (fun w -> (fun v -> id(1+v))(2+w))(3+u)) 0
~> (fun w -> (fun v -> id(1+v))(2+w)) 3
~> (fun v -> id(1+v)) 5
~> id 6
~> 6
```
