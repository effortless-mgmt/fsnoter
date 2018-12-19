## Weekly Exercises
### Week 1

#### Exercise 1 Solution

```fsharp
let rec sum(n) = 
    match n with
    | 0 -> 0
    | n -> n + sum(n-1)
val : int -> int
```

#### Exercise 2 Solution

```fsharp
let rec sum2(m, n) =
    match m, n with
    | _,0 -> m
    | m,n when m > 0 -> m + n + sum2(m, n-1)
    | _,_ -> failwith "Negative argument"
val : int * int -> int
```

#### Exercise 3 Solution

```fsharp
let rec bin(n, k) =
    match n, k with
    | _,_ when n < 0 || k < 0 -> failwith "Negative argument(s)"
    | _,0 -> 1
    | n,k when k = n -> 1
    | n,k -> bin(n-1, k-1) + bin(n-1, k)
val : int * int -> int
```

#### Exercise 4 Solution

```fsharp
let rec multiplicity(x, ys) = 
    match ys with
    | [] -> 0
    | ys::tail when ys = x -> 1 + multiplicity(x, tail)
    | ys::tail -> multiplicity(x, tail)
val : 'a * 'a list -> int
```

#### Exercise 5 Solution

```fsharp
let rec mulC(x, ys) =
    match ys with
    | head::tail -> x * head :: mulC(x, tail)
    | [] -> []
val : int * int list -> int list
```

#### Exercise 6 Solution

```fsharp
let rec addE(xs, ys) =
    match xs, ys with
    | xshead::xstail, yshead::ystail -> xshead + yshead :: addE(xstail, ystail) 
    | xs,[] -> xs
    | [],ys -> ys
val : int list * int list -> int list
```

#### Exercise 7a Solution

```fsharp
let mulX(xs) = [0] @ xs
val : int list -> int list
```

#### Exercise 7b Solution

```fsharp
let rec mul(xs, ys) =
    match xs, ys with
    | _,[] -> []
    | [],_ -> []
    | xshead::xstail,ys -> addE(mulC(xshead, ys), mulX(mul(xstail, ys)))
val : int list * int list -> int list
```

#### Exercise 7c Solution

```fsharp
let polyToString(poly: int list) =
    let n = poly.Length
    let rec toString(poly) =
        match poly with
        | [] -> ""
        | head::tail when head = 0 -> toString(tail)
        | head::tail -> (if poly.Length=n then string(head) 
                            else (if head=1 then "x^" else string(head) + "*x^")
                            + string(n-tail.Length-1))
                        + (if tail.IsEmpty then "" else " + " + toString(tail))
    (toString(poly));;
val : int list -> string
```