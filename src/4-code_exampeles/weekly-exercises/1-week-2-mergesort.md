### Week 2 - Mergesort

#### Merge

```fsharp
let rec merge (xs:int list,ys:int list) =
    match xs, ys with
    | [],ys -> ys
    | xs,[] -> xs
    | xhead::xtail,yhead::ytail when yhead <= xhead -> yhead::merge(xhead::xtail,ytail)
    | xhead::xnext::xtail,yhead::ytail when yhead <= xnext -> xhead::yhead::merge(xnext::xtail,ytail)
    | xhead::xtail,ys -> xhead::merge(xtail,ys)
val : int list * int list -> int list
```

#### Split

```fsharp
let rec split = function
    | [] -> ([],[])
    | [x] -> ([x],[])
    | x::y::xtail ->
        let (xs, ys) = split xtail
        (x::xs,y::ys)
val : 'a list -> 'a list * 'a list
```

#### Sort

```fsharp
let rec sort (xs:int list) =
    match xs with
    | [] -> []
    | [x] -> [x]
    | xs -> let (xs1:int list,xs2:int list) = split xs
            let xs1sorted = sort xs1
            let xs2sorted = sort xs2
            merge(xs1sorted,xs2sorted)
val : int list -> int list
```