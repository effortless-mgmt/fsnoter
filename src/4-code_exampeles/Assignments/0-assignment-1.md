## Assignments
### Assignment 1

```fsharp
// ##############################
// ##### TYPE DECLARATIONS ######
// ##############################

type Species     = string
type Location    = string
type Time        = int
type Observation = Species * Location * Time
type Count<'a when 'a:equality> = ('a*int) list
type Interval = Time*Time
let os = [("Owl","L1",3); ("Sparrow","L2",4); ("Eagle","L3",5); 
    ("Falcon","L2",7); ("Sparrow","L1",9);  ("Eagle","L1",14)]

// ##############################
// ###### START TASK 2.1 ########
// ##############################

// Gives the list of locations from observations of species s in os.
let rec locationsOf s = function
    | ([] : Observation list) -> []
    | (sx,lx,_)::tail when sx = s -> lx::locationsOf s tail
    | _::tail -> locationsOf s tail

// Testing 1 species with 1 location.
// Expected: val it : Location list = ["L2"]
let locTest1 = locationsOf "Falcon" os
printfn "LocTest1 expected result: [\"L2\"]"
printfn "LocTest1: %A" locTest1

// Testing 1 species with 2 locations.
// Expected: val it : Location list = ["L3"; "L1"]
let locTest2 = locationsOf "Eagle" os
printfn "LocTest2 expected result: [\"L3\"; \"L1\"]"
printfn "LocTest2: %A" locTest2

// Testing 1 species not found in observation list.
// Expected: val it : Location list = []
let locTest3 = locationsOf "Tit" os
printfn "LocTest3 expected result: []"
printfn "LocTest3: %A" locTest3

// Testing 1 species and an empty observation list.
// Expected: val it : Location list = []
let locTest4 = locationsOf "Sparrow" []
printfn "LocTest4 expected result: []"
printfn "LocTest4: %A" locTest4

// ##############################
// ###### START TASK 2.2 ########
// ##############################

// Gives the occurrence count obtained from occ by incrementing the count of a with 1.
// Type: Species -> Count<Species> -> Count<Species>
let rec insert a = function
    | ([] : Count<Species>) -> ([(a,1)] : Count<Species>)
    | (ax,c)::tail when ax = a -> (ax,c+1)::tail
    | (ax,c)::tail -> (ax,c)::insert a tail

// Type: a' -> ('a * int) list -> ('a * int) list
// let rec insert2 a = function
//     | [] -> [(a,1)]
//     | (ax,c)::tail when ax = a -> (ax,c+1)::tail
//     | (ax,c)::tail -> (ax,c)::insert2 a tail

// Testing "Sparrow" and a Count containing 2 counts of "Sparrow".
// Expected: val it : Count<Species> = [("Eagle", 2); ("Owl", 1); ("Falcon", 1); ("Sparrow", 3)]
let insTest1 = insert "Sparrow" [("Eagle",2);("Owl",1);("Falcon",1);("Sparrow",2)]
printfn "InsTest1 expected result: [(\"Eagle\", 2); (\"Owl\", 1); (\"Falcon\", 1); (\"Sparrow\", 3)]"
printfn "InsTest1: %A" insTest1

// Testing "Sparrow" and a Count containing no counts of "Sparrow".
// Expected: val it : Count<Species> = [("Eagle", 2); ("Owl", 1); ("Falcon", 1); ("Sparrow", 1)]
let insTest2 = insert "Sparrow" [("Eagle",2);("Owl",1);("Falcon",1)]
printfn "InsTest2 expected result: [(\"Eagle\", 2); (\"Owl\", 1); (\"Falcon\", 1); (\"Sparrow\", 1)]"
printfn "InsTest2: %A" insTest2

// ##############################
// ###### START TASK 2.3 ########
// ##############################

// Gives the occurrence count of species in a list of observations.
// Type: Observation list -> Count<Species>
let rec toCount = function
    | ([] : Observation list) -> ([] : Count<Species>)
    | (s,_,_)::tail -> (insert s (toCount tail))

// ##############################
// ###### START TASK 2.4 ########
// ##############################

// Gives a list of functions (evaluations) applied to the elements of observation list os
// that has a time t within the limits of the time interval intv.
let rec select f (intv : Interval) =
    let (t1, t2) = intv
    function
    | ([] : Observation list) -> []
    | (s,l,t)::tail when t >= t1 && t <= t2 -> f((s,l,t) : Observation)::select f intv tail
    | _::tail -> select f intv tail

// ##############################
// ###### START TASK 2.5 ########
// ##############################

// Gives a list of pairs consisting of a species and it's observation location
// that were observed in the time interval between 4-9 inclusive.
let selectTest = select (fun (s,l,t) -> (s,l)) (4,9) os
printfn "SelectTest expected result: [(\"Sparrow\", \"L2\"); (\"Eagle\", \"L3\"); (\"Falcon\", \"L2\"); (\"Sparrow\", \"L1\")]"
printfn "SelectTest: %A" selectTest

// ##############################
// ###### START TASK 3.1 ########
// ##############################

// I Chose the "List.choose" function as it allows 
// filterings and transformation of the list elements in one go.
let locationsOfNew s (os : Observation list) = 
    List.choose (function
        | (sx,lx,_) when sx = s -> Some(lx)
        | _ -> None 
        ) os

let locNewTest = locationsOfNew "Sparrow" os
printfn "LocNewTest expected result: [\"L2\"; \"L1\"]"
printfn "LocNewTest: %A" locNewTest

// ##############################
// ###### START TASK 3.3 ########
// ##############################

// List.fold allows traversal of a given list,
// applying a function to each element and the given accumulator.
// The accumulator is then returned as the result and passed onto the
// next iteration of List.fold.
let toCountNew (os : Observation list) = 
    List.fold (fun count (sx,_,_) -> insert sx count) [] os

let toCNewTest = toCountNew os
printfn "ToCNewTest expected result: [(\"Owl\", 1); (\"Sparrow\", 2); (\"Eagle\", 2); (\"Falcon\", 1)]"
printfn "ToCNewTest: %A" toCNewTest

// I wondered if the challenge was to use only List functions.
// The idea is to create a list of destict Species,
// then use that list to count the occurences of each Species.
// This is achieved by using List.choose to extract the Species from os,
// then apply List.distinct on the resulting list to filter duplicate Species.
// Next List.countBy is applied to os running through each element,
// finally elements are counted by checking the Species element of the 3-tuple
// with the species list using List.find.
let toCountNewNew (os : Observation list) : Count<Species> =
    let speciesList = List.distinct (List.choose (fun (s,_,_) -> Some(s)) os )
    List.countBy (fun (s,_,_) -> List.find (fun sx -> s = sx) speciesList ) os

let toCNewNewTest = toCountNewNew os
printfn "toCNewNewTest expected result: [(\"Owl\", 1); (\"Sparrow\", 2); (\"Eagle\", 2); (\"Falcon\", 1)]"
printfn "toCNewNewTest: %A" toCNewNewTest
```