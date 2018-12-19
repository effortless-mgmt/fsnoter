## Previous Exam

### Problem 1

#### 1.1 Problem Definition

Declare a function `repeatList: 'a list -> int -> 'a list`, so that

```
repeatList xs n = xs @ xs @ ... @ xs,   with n occurences of xs
```

For example, `repeatList [1; 2] 3 = [1;2;1;2;1;2]` and `repeatList [1;2] 0 = []`.

#### 1.1 Solution

```fsharp
let rec repeatList lst = function
    | 0 -> []
    | cnt -> repeatList lst (cnt-1) @ lst
val : 'a list -> int -> 'a list
```

#### 1.2 Problem Definition

Declare a function `merge: 'a list * 'a list -> 'a list`, so that

```
merge([x0; x1; ...; xm], [y0; y1; ...; yn])=
    [x0; y0; x1; y1; ...; xm; ym; ym+1; ym+2; ... yn]   when m < n
    [x0; y0; x1; y1; ...; xm; ym]                       when m = n
    [x0; y0; x1; y1; ...; xn; yn; xn+1; xn+2; ... xm]   when m > n
```

That is, the function merge can merge the elements of two lists, where the lists need not have the same size. For example, `merge([1; 2], [3; 4]) = [1; 3; 2; 4]`, `merge([1; 2], [3; 4; 5]) = [1;3;2;4;5]` and `merge([1;2;3;4],[5;6]) = [1;5;2;6;3;4]`.

#### 1.2 Solution

```fsharp
let rec merge (xs, ys) =
    match xs, ys with
    | ([], zs) | (zs, []) -> zs
    | x::xtail, y::ytail -> x::y::merge(xtail, ytail)
val : 'a list * 'a list -> 'a list

// alternative declaration for merge
let rec merge1(xs,ys) = 
    match xs with 
    | []      -> ys
    | x::xrest -> x::merge1(ys,xrest);;  
val : 'a list * 'a list -> 'a list
```
