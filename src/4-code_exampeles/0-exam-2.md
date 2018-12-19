### Problem 2

Consider the following F# declarations:

```fsharp
let rec f  = function
             | 0          -> [0]
             | i when i>0 -> i::g(i-1)
             | _          -> failwith "Negative argument"
and g = function
        | 0 -> []
        | n -> f(n-1);;
val f : int -> int list
val g : int -> int list

let h s k = seq{for a in s do yield k a };;
val : -> seq<'a> -> ('a -> 'b) -> seq<'b>

let rec sum xs = 
    match xs with
    | []      -> 0
    | x::rest -> x + sum rest;;
val : int list -> int
```

#### 2.1 Problem Definition

Give the values of `f 5` and `h (seq [1;2;3;4]) (fun i -> i+10)`. Furthermore, give the (most general) types for `f` and `h`, and describe what each of these two functions computes. Your description for each function should focus on what it computes, rather than on individual computation steps.

#### 2.1 Solution

```
f 5 = [5; 3; 1] as can by an evaluation
f 5 evaluates to 
5::g 4 evaluates to 
5::f 3 evaluates to 
5::3::g 2 evaluates to
5::3::f 1 evaluates to
5::3::1::g 0 evaluates to
5::3::1::[]
```

The type of `f` is `int -> int list`

If `i` is negative the `f i` raises an exception
if `i` is positive and odd, then `f i = [i; i-2; ....;1]` otherwise `f i = [i; i-2; ....;0]`

```fsharp
h (seq [1;2;3;4]) (fun i -> i+10) = seq [11; 12; 13; 14]
```

`h` has type `seq<'a> -> ('a -> 'b) -> seq<'b>` and `h sq k` is the sequence obtained from `sq` by application of `k` to every element, that is, the value of `h sq k` is the same as the value of `Seq.map k sq`.

#### 2.2 Problem Definition

The function sum is not tail recursive.
* Provide a tail-recursive variant that is based on an accumulating parameter, and
* provide a continuation-based tail-recursive variant of sum.

```fsharp
// Tail recursion
let rec sumT xs acc = 
    match xs with 
    | []       -> acc
    | x::rest -> sumT rest (x+acc)
val : int list -> int -> int

// Continuation-based tail recursion
let rec sumC xs k = 
    match xs with 
    | []      -> k 0
    | x::rest -> sumC rest (fun v -> k(x+v));;
val : int list -> (int -> 'a) -> 'a
```
