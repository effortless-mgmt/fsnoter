### Problem 3

#### 3.1 Problem Definition

We shall now consider *containers* that can either have the form of a *tank*, that is characterized by it length, width and height, or the form of a *ball*, that is characterized by its radius. This is captured by the following declaration:

```fsharp
 type Container =
       | Tank of float * float * float // (length, width, height)
       | Ball of float                 // radius
```

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
let wf = function Tank(l,w,h) -> l>=0.0 && w>0.0 && h>0.0
                | Ball r      -> r>0.0
                | Cylinder(r,h) -> r>0.0 && h>0.0;;                         // Q 3.4  
```
