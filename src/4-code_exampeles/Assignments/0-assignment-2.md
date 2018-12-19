## Assignments
### Assignment 2

```fsharp
// ##############################
// ##### TYPE DECLARATIONS ######
// ##############################

type Term = | V of string
            | C of int
            | F of string * Term list

// ##############################
// ######  TEST VARIABLES  ######
// ##############################

let term1 = V "x"
let term2 = C 3
let term3 = F("f0",[])
let term4 = F("f1",[term2;term3])
let term5 = F("max",[term1;term2])
let term6 = F("f3",[F("f2",[C 1;C 2]);F("f1",[term1]);term3])
let term7 = F("f3",[F("f2",[C 1;term1]);F("f1",[term1;F("f0",[V "y";term1])]);term1])

// ##############################
// #####  HELPER FUNCTIONS  #####
// ##############################

let rec listHelper (e, s, l) = function
    | [] -> e
    | [t] -> s t
    | t::tail  -> l t tail

// ##############################
// ###### START TASK 2.1 ########
// ##############################

// This version I believe is faster than the one below, as the "List.forall"
// function returns immediately upon an evaluation returning false.
// let rec isGround = function
//     | V _ -> false
//     | C _ -> true
//     | F (_,tl) -> List.forall isGround tl

// This version seems more in line with what I believe to be the intended implementation
// as seen in the book examples.
let rec isGround = function
    | V _ -> false
    | C _ -> true
    | F (_,tl) -> termListIsGround tl
and termListIsGround = function
    | [] -> true
    | [t] -> isGround t
    | t::tail -> isGround t && termListIsGround tail

// I made a version using a helper method declared in the helper functions section.
// I didn't like the way I ended up having to use it, so I commented it out in favour of the above function.
// let rec isGround = 
//     let rec checkList = (fun t tail -> isGround t && listHelper ((true),(isGround),(checkList)) tail)
//     function
//     | V _ -> false
//     | C _ -> true
//     | F (_,tl) -> listHelper ((true),(isGround),(checkList)) tl

let isGroundTest1 = isGround term1
printfn "Is Term1 a ground Term? \nTerm1: %A \nResult: %b \nExpected: false \n" term1 isGroundTest1
let isGroundTest2 = isGround term2
printfn "Is Term2 a ground Term? \nTerm2: %A \nResult: %b \nExpected: true \n" term2 isGroundTest2
let isGroundTest3 = isGround term3
printfn "Is Term3 a ground Term? \nTerm3: %A \nResult: %b \nExpected: true \n" term3 isGroundTest3
let isGroundTest4 = isGround term4
printfn "Is Term4 a ground Term? \nTerm4: %A \nResult: %b \nExpected: true \n" term4 isGroundTest4
let isGroundTest5 = isGround term5
printfn "Is Term5 a ground Term? \nTerm5: %A \nResult: %b \nExpected: false \n" term5 isGroundTest5

// ##############################
// ###### START TASK 2.2 ########
// ##############################

// I tried with a List function first as that seemed like a fun thing to try.
// It isn't as fast as I thought it'd be, so I tried an approach similar to isGround.
// let rec toString = function
//     | V s -> s
//     | C i -> string i
//     | F (s,tl) -> s + "(" + (List.fold (fun x t -> x + if tl.Length = 1 || t = tl.[tl.Length-1] then toString t else (toString t + ",")) "" tl) + ")"

// #time
// let toStringTest = toString term6
// #time
// printfn "Term6: %s" toStringTest

// The function below runs (using #time) 15 times faster than the one above.
// This version is also far easier on the eyes.
let rec toString = function
    | V s -> s
    | C i -> string i
    | F (s,tl) -> s + "(" + termListToString tl + ")"
and termListToString = function
    | [] -> ""
    | [t] -> toString t
    | t::tail -> toString t + "," + termListToString tail

// Same deal as in Task 2.1
// let rec toString = 
//     let rec doListStuff = (fun t tail -> toString t + "," + listHelper ((""),(toString),(doListStuff)) tail)
//     function
//     | V s -> s
//     | C i -> string i
//     | F (s,tl) -> s + "(" + listHelper((")"),(fun t -> toString t + ")"),(doListStuff)) tl

let toStringTest = toString term6
printfn "Term6 to string \nTerm6: %A \nResult: %s \nExpected: f3(f2(1,2),f1(x),f0()) \n" term6 toStringTest

// ##############################
// ###### START TASK 2.3 ########
// ##############################

// Types:
// subst: string -> Term -> Term -> Term
// termListSubst: string -> Term -> Term list -> Term list
let rec subst x t' = function
    | V s -> if s = x then t' else V s
    | C i -> C i
    | F (s,tl) -> F (s,termListSubst x t' tl)
and termListSubst x t' = function
    | [] -> []
    | [t] -> [subst x t' t]
    | t::tail -> (subst x t' t) :: termListSubst x t' tail

let term7Alt = F("f3",[F("f2",[C 1; C 3]); F("f1",[C 3; F("f0",[V "y"; C 3])]); C 3])
let substTest = subst "x" (C 3) term7
printfn "Substitute V \"x\" in Term7 with C 3 \nTerm7: %A \nResult: %A \nExpected: %A \n" term7 substTest term7Alt
```