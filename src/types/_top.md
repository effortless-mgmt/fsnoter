# Types

F# is a strongly types language. It has a bunch of types, but the most used in these assignments are:

* `bool` - boolean
* `int`  - 32 bit integer
* `float` - 64 bit floating point
* `string` - string
* `tuple` - type consisting of multiple parts
* `list` - a list of items
* `'a` - An unknown type - read more in Type section **Declaration and Type Inference**

You can also define custom types:

```fsharp
type Circle = float
type Rectangle = float * float
```

These can then be defined:

```fsharp
let circle1 = Circle 7.4
let rectangle1 = Rectangle(3.8, 2.3)
```

You can define sub types:

```fsharp
type Container =
    | Tank of float * float * foat
    | Ball of float

// Define a tank
let tank = Tank (30.0, 40.0, 50.0)
```

You can define recursive types:

```fsharp
type Tree =
    | Lf
    | Br of Leaf * int * Leaf
// Define a tree
let tree1 = Br(Br(Br(Lf,2,Lf),7,Lf),
9,
Br(Br(Lf,13,Lf),21,Br(Lf,25,Lf)))
```

