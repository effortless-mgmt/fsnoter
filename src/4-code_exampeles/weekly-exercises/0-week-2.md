## Weekly Exercises
### Week 2

#### Exercise 2.1 Solution

```fsharp
let f = function
    | x when x%5=0 -> false
    | x when x%2=0 -> true
    | x when x%3=0 -> true
    | _ -> false
val : int -> bool
```

#### Exercise 2.2 Solution

```fsharp
let rec pow s = function
    | n when n = 0 -> ""
    | 1 -> s
    | n -> s + pow s (n-1)
val : string -> int -> string
```

#### Exercise 4.3 Solution

```fsharp
let evenN n = [2..2..n*2]
val : int -> int list
```

#### Exercise 4.8 Solution

```fsharp
let rec split = function
    | [] -> ([],[])
    | [x] -> ([x],[])
    | x::y::xtail ->
        let (xs, ys) = split xtail
        (x::xs,y::ys)
val : 'a list -> 'a list * 'a list
```

#### Exercise 4.9 Solution

```fsharp
let rec zip = function
    | [],[] -> []
    | x,[] -> x
    | [],y -> y
    | x::xtail,y::ytail ->
        let res = zip (xtail, ytail)
        (x::y::res)
val : 'a list * 'a list -> 'a list
```

#### Exercise 4.12 Solution

```fsharp
let rec sum p = function
    | [] -> 0
    | x::xtail when p(x) -> x + sum p xtail
    | x::xtail -> sum p xtail
val : (int -> bool) -> int list -> int
```

#### Exercise 4.16a Solution

```fsharp
let rec f' = function
    | (x, []) -> []
    | (x, y::ys) -> (x+y)::f'(x-1, ys)
val : int * int list -> int list

// f(x,[y0;y1;...;yn-1]),n>=0
```

The value is a list of integers being the result of the formula `x+y` where `x `is decreased by 1 for each recursion

```
[(x+y0);(x-1+y1);...;(x-(n-1)+yn-1)]
```

#### Exercise 4.16b Solution

```fsharp
let rec g = function
    | [] -> []
    | (x,y)::s -> (x,y)::(y,x)::g s
val : ('a * 'a) list -> ('a * 'a) list

// g[(x0,y0);(x1,y1);...;(xn-1,yn-1)],n>=0
```
The value is `a list` of pairs where each pair is followed by the same pair, but reversed

```
[(x0,y0);(y0,x0);(x1,y1);(y1,x1);...;(xn-1,yn-1);(yn-1,xn-1)]
```

#### Exercise 4.16c Solution

```fsharp
let rec h = function
    | [] -> []
    | x::xs -> x::(h xs)@[x]
val : 'a list -> 'a list

// h[x0;x1;...;xn-1],n>=0
```
The value is the `list xs` with a 'mirrored' (reversed) version of `xs` appended 

```
[x0;x1;...;xn-1;xn-1;..;x1;x0]
```

#### Exercise 4.17 Solution

```fsharp
let rec p q = function
    | [] -> []
    | x::xs ->
        let ys = p q xs
        if q x then x::ys else ys@[x]
val : ('a -> bool) -> 'a list -> 'b list

// p q [x0;x1;x2;...;xn-1]
```

The value will be a list containing the elements of xs that satisfies q in the front and elements that don't in the back

#### Exercise 4.11a Solution

```fsharp
let rec count (xs:int list,x:int) =
    match xs with
    | [] -> 0
    | head::tail when head = x -> 1 + count(tail,x)
    | head::tail -> count(tail,x)
val : int list * int -> int
```

#### Exercise 4.11b Solution

```fsharp
let rec insert (xs,x:int) =
    match xs with
    | [] -> []
    | [head] -> head::[x] // maybe not needed?
    | head::tail when x <= head -> x::head::tail
    | head::next::tail when x <= next -> head::x::next::tail
    | head::tail -> head::insert(tail,x)
val : int list * int -> int list
```

#### Exercise 4.11c Solution

```fsharp
let rec intersect (xs: int list,ys: int list) =
    match xs, ys with
    | [],_ -> []
    | _,[] -> []
    | xhead::xtail,yhead::ytail when xhead = yhead -> xhead::intersect(xtail,ytail)
    | xhead::xnext::xtail,yhead::ytail when yhead > xhead && yhead < xnext -> intersect(xnext::xtail,ytail)
    | xhead::xtail,ys -> intersect(xtail, ys)
val : int list * int list -> int list
```

#### Exercise 4.11d Solution

```fsharp
let rec plus (xs: int list,ys: int list) =
    match xs, ys with
    | [],ys -> ys
    | xs,[] -> xs
    | xhead::xtail,yhead::ytail when yhead <= xhead -> yhead::plus(xhead::xtail,ytail)
    | xhead::xnext::xtail,yhead::ytail when yhead <= xnext -> xhead::yhead::plus(xnext::xtail,ytail)
    | xhead::xtail,ys -> xhead::plus(xtail,ys)
val : int list * int list -> int list
```

#### Exercise 4.11e Solution

```fsharp
let rec minus (xs: int list,ys: int list) =
    match xs, ys with
    | [],_ -> []
    | xs,[] -> xs
    | xhead::xtail,yhead::ytail when xhead = yhead -> minus(xtail, ytail)
    | xhead::xtail,yhead::ynext::ytail when xhead >= ynext -> minus(xhead::xtail,ynext::ytail)
    | xhead::xtail,ys -> xhead::minus(xtail, ys)
val : int list * int list -> int list
```
