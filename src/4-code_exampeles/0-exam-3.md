### Problem 3

We shall now consider *containers* that can either have the form of a *tank*, that is characterized by it length, width and height, or the form of a *ball*, that is characterized by its radius. This is captured by the following declaration:

```fsharp
 type Container =
       | Tank of float * float * float // (length, width, height)
       | Ball of float                 // radius
```

#### 3.1 Problem Definition

Declare two F# values of type `Container` for a tank and a ball, respectively.

#### 3.1 Solution

```fsharp
let tank = Tank(3.0, 4.0, 5.0)
let ball = Ball 5.0
```

#### 3.2 Problem Definition

A `Tank` is called *well-formed* when its length, width and height are all positive and a `Ball` is well-formed when its radius is positive. Declare a function `isWF : Container -> bool` that can test whether a container is well-formed.

#### 3.2 Solution

```fsharp
let wf = function 
    Tank(l,w,h) -> l >= 0.0 && w > 0.0 && h > 0.0
    | Ball r      -> r > 0.0
    | Cylinder(r,h) -> r > 0.0 && h > 0.0;;     // Q 3.4  
```

#### 3.3 Problem Definition

Declare a function `volume` $c$ computing the `volume` of a container c. (Note that the volume of ball with radius $r$ is $4 \cdot \pi \cdot r^3$.)

#### 3.3 Solution

```fsharp
let volume = function 
    Tank(l,w,h)   -> l*w*h
    | Ball r        -> 4.0/3.0 *System.Math.PI * r*r*r
    | Cylinder(r,h) -> System.Math.PI * r*r*h;;     // Q 3.4
```

#### 3.4 Problem Definition

A storage consist of a collection of uniquely named containers, each having a certain con- tents, as modelled by the type declarations:

```fsharp
type Name     = string
type Contents = string
type Storage  = Map<Name, Contents*Container>
```

Where the name and contents of containers are given as strings.

Note: You may choose to solve the below questions using a list-based model of a storage `(type Storage = (Name * (Contents*Container)) list)`, but your solutions will, in that case, at most count 75%.

#### 3.4 Solution

See the last line of the solutions of 3.2 and 3.3 (the line that ends with `// Q 3.4`).

#### 3.5 Problem Definition

Declare a value of type `Storage`, containing a `Tank` with name "`tank1`" and contents "`oil`" and a `Ball` with name "`ball1`" and contents "`water`".

#### 3.5 Solution

```fsharp
let stg = Map.ofList [("tank1",("oil",tank)); ("ball1", ("water", ball))]
```

#### 3.6 Problem Definition

Declare a function `find : Name -> Storage -> Contents * float`, where `find n stg` should return the pair `(cnt,vol)` when `cnt` is the contents of a `Container` with name `n` in storage `stg`, and `vol` is the volume of that container. A suitable exception must be raised when no container has name `n` in storage `stg`.

#### 3.6 Solution

```fsharp
let find n st = 
    match Map.tryFind n st with 
    | Some(cnt, c) -> (cnt, volume c)
    | None         -> failwith (n + " is not a name of a container")
```
