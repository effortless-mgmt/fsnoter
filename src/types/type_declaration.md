## Type Declaration and Type Inference

The types in F# can at times be a bit complex compared to other languages. When defining values and functions, the type is usually inferred unless explicitly stated:

```fsharp
let anInt = 4
val it : int

let aFloat = 13.74
val it : float

let aTupleIntString = (42, "Hello")
val it : int * string

let myString: string = "This is a string, explicitly stated"
val it : string
```

The difficult task can be to determine the type of a function. Functions have arrows `->` separating the intput types and return types. The most basic function is a function which takes an `int` and returns and `int`:

```fsharp
let makeBigger x = x + 10
val : int -> int
```

With multiple arguments, the function would have more arrows:

```fsharp
let add x y = x + y
val : int -> int -> int
```

Tuples are defined as the types separated with `*`. Each value can have a different type on the tuple.

```fsharp
let t1 = (2, 2.3)
val : int * float
```

A tuple can also have a tuple as a type inside.

```fsharp
let t2 ((1, 2), (3, 4))
val : (int * int) * (int * int)
```

Lists use the keyword `list`. The keywork is appended to the type of the values inside it. Each value in the list must be of the same type.

```fsharp
let l1 = [1; 2; 3; 4]
val : int list

let l2 = [(1, 2); (3, 4)]
val : (int * int) list
```

When a function takes a function as a parameter, the type is usually in parenthesis, with the paramters and return types inside.

```fsharp
let f i g = i + g i
val : int -> (int -> int) -> int
```

**NOTE**: When determining the types, make sure to primarily look at the function definition, not the usage. If it helps, then do it, but don't get confused into thinking the type is what it is in the usage. Look at the below example from a previous exam:

```fsharp
let h s k = seq { for a in s do yield k a };;

// Usage
h (seq [1;2;3;4]) (fun i -> i + 10)
```

What is the most general type of `h`? It's `seq<'a> -> ('a -> 'b) -> seq<'b>`. Not `seq<int>` or anything like that. We don't know whether the datatype is of type `int` or whatever, it just is in the above example, so look out for that!
