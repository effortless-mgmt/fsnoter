### Problem 4

Consider the following F# declarations of a type `T<’a>` for binary trees having values of type `’a` in nodes, three functions `f`, `h` and `g`, and a binary tree `t`:

```fsharp
type T<’a> = L | N of T<’a> * ’a * T<’a>

let rec f g t1 t2 =
      match (t1,t2) with
      | (L,L) -> L
      | (N(ta1,va,ta2), N(tb1,vb,tb2))
                  -> N(f g ta1 tb1, g(va,vb), f g ta2 tb2);;

let rec h t = match t with
      | L            -> L
      | N(t1, v, t2) -> N(h t2, v, h t1);;


let rec g = function
      | (_,L)                    -> None
      | (p, N(t1,a,t2)) when p a -> Some(t1,t2)
      | (p, N(t1,a,t2))          -> match g(p,t1) with
                                    | None -> g(p,t2)
                                    | res  -> res;;


let t = N(N(L, 1, N(N(L, 2, L), 1, L)), 3, L);;
```

#### 4.1 Problem Definition

Give the type of `t`. Furthermore, provide three values of type `T<bool list>`.

#### 4.1 Solution

The type of `t` is `T<int>`, i.e. `t: T<int>`.

Three values of type `T<bool list>`:

```fsharp
let ta = L
let tb = N(ta, [false],ta);;
let tc = N(tb, [true;false],tb);;
```

#### 4.2 Problem Definition

Give the (most general) types of `f`, `h` and `g` and describe what each of these three func- tions computes. Your description for each function should focus on *what* it computes, rather than on individual computation steps.

#### 4.2 Solution

The most general type of `f is ('a * 'b -> 'c) -> T<'a> -> T<'b> -> T<'c>`

For a justification of this consider the expression `f g t1 t2`. 

The type of `f` has the form: `tg -> type2 -> type3 -> type3`, where
the type of `g` is `tg`, i.e. `g: type1, t1: type1, t2: type2 and (f g t1 t2): type3`

1. From on the `match (t1,t2)`, we observe that `t1` and `t2` are two trees with types, say `type1=T<'a>` and `type2=T'b>`.
2. from `g(va,vb)` we see that `va`: `'a, vb: 'b`  and hence the type of `g` has the form:
   `tg = 'a * 'b -> 'c`, where `'` is a new type variable
3. From expression in the second clause we see that the value of the expression must have the type `type3 = T<'c>`.

Since there are no further type constraints so `f: ('a * 'b -> 'c) -> T<'a> -> T<'b> -> T<'c>`

The value of `(f g t1 t2)` is defined when `t1` and `t2` are two trees of the same shape and the value of the expression is a tree `t` with the same shape as that of `t1` and `t2`. The value in a node `n` of `t` is `g(v1,v2)`, there `vi` is the value in node of `ti` appearing in the same position as `n, for i = 1, 2`. For example 

If `t1` has the form: 

```
             N
      _______|______        
      |      x     |
      N            N
  ____|___      ___|___
  .   y  .      .  z   .
  .      .      .      .
```

and `t2` has the form: 
```
             N
      _______|______        
      |      o     |
      N            N
  ____|___      ___|___
 .    p  .      .  q    .
 .       .      .       .
```

then `t` has the form: 
```
             N
      _______|______        
      |     v1     |
      N            N
  ____|___      ___|___
 .   v2  .      .  v3   .
 .       .      .       .
```

where `v1 = g(x, o)`, `v2 = g(y, p)` and `v3 = g(z, q)`.

`h` has the `type T<'a> -> T<'a>` and the value of `h(t)` is the mirror image of `t`, in other words `h t` makes a reflection of `t` -- it is natural to supply a suitable drawing as done for `f`.

`g` has type `('a -> bool) * T<'a> -> (T<'a>*T<'a>) option`

`g (p,t)` makes a depth-first (left to right) traversal of `t` searching for a node `N(left,a,right)` where the value `a` in the node satiefies predicate `p`, that is, `p a = true`. 

If such node exists, then the value is `Some(left,right)`; otherwise the value is `None`. -- it is natural to supply a suitable drawing as done for `f`.

#### 4.3 Problem Definition

Declare a function `count a t` that can count the number of occurrences of `a` in the binary tree `t`. For example, the number of occurrences of 1 in the tree `t` is 2.

#### 4.3 Solution

```fsharp
let rec count a = function 
      | L  -> 0
      | N(t1,v,t2) when v=a -> 1 + count a t1 + count a t2
      | N(t1,_,t2)          -> count a t1 + count a t2;;
```

#### 4.4 Problem Definition

Declare a function replace, so that replace abt is the tree obtained from `t` by replacement of every occurrence of `a` by `b`. For example, `replace 1 0 t` gives the tree `N(N(L, 0, N(N(L, 2, L), 0, L)), 3, L)`.

#### 4.4 Solution

```fsharp
let rec replace a b = function 
      | L  -> L
      | N(t1,v,t2) when a=v -> N(replace a b t1, b, replace a b t2)
      | N(t1,v,t2)          -> N(replace a b t1, v, replace a b t2);; 
```