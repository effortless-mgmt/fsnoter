### Assignment 3

```fsharp
// ##############################
// ##### TYPE DECLARATIONS ######
// ##############################

type Title = string

type Document = Title * Element list
and Element = Par of string | Sec of Document

type Prefix = int list

type ToC = (Prefix * Title) list

// ##############################
// ######  TEST VARIABLES  ######
// ##############################

let s1 = ("Background", [Par "Bla"])
let s21 = ("Expressions", [Sec("Arithmetical Expressions", [Par "Bla"]);
Sec("Boolean Expressions", [Par "Bla"])])
let s222 = ("Switch statements", [Par "Bla"])
let s223 = ("Repeat statements", [Par "Bla"])
let s22 = ("Statements",[Sec("Basics", [Par "Bla"]); Sec s222; Sec s223])
let s23 = ("Programs", [Par "Bla"])
let s2 = ("The Programming Language", [Sec s21; Sec s22; Sec s23])
let s3 = ("Tasks", [Sec("Frontend", [Par "Bla"]); Sec("Backend", [Par "Bla"])])
let doc = ("Compiler project", [Par "Bla"; Sec s1; Sec s2; Sec s3])

// ##############################
// ###### START TASK 1.1 ########
// ##############################

let rec noOfSecs = function
    | (_,[]) -> 0
    | (t,head::tail) -> noOfSecs (t,tail) + isSec head
and isSec = function
    | Par _ -> 0
    | Sec doc -> 1 + noOfSecs doc

let noOfSecsTest1 = noOfSecs doc
printfn "no of Secs in doc: %i" noOfSecsTest1

// ##############################
// ###### START TASK 1.2 ########
// ##############################

let rec sizeOfDoc = function
    | (t:Title,[]) -> t.Length
    | (t,head::tail) -> sizeOfDoc (t,tail) + sizeOfElement head
and sizeOfElement = function
    | Par t -> t.Length
    | Sec doc -> sizeOfDoc doc

let sizeOfDocTest1 = sizeOfDoc doc
printfn "size of doc (total amount of characters) in doc: %i" sizeOfDocTest1

// ##############################
// ###### START TASK 1.3 ########
// ##############################

let rec titlesInDoc = function
    | (t,[]) -> []
    | (t,head::tail) -> titlesInElement head @ titlesInDoc (t,tail)
and titlesInElement = function
    | Par _ -> []
    | Sec (t,lst) -> t :: titlesInDoc (t,lst)

let titlesInDocTest1 = titlesInDoc doc
printfn "List of titles in doc: %A" titlesInDocTest1

// ##############################
// ###### START TASK 1.4 ########
// ##############################

// This has the correct type, but the static typechecker
// doesn't seem to realize the types have been named
let toc =
    let rec goThruDoc acc pref = function
        | (_,[]) -> []
        // go through sections/subsections, increment acc when new section
        | (t, head::tail) -> goThruElement acc pref head @ goThruDoc (acc+1) pref (t,tail)
    and goThruElement acc pref = function
        // We don't care about Par
        | Par _ -> []
        // Add section to ToC, reset acc to 1 and go through subsections
        | Sec (t,lst) -> (pref@[acc],t) :: goThruDoc 1 (pref@[acc]) (t,lst)
    function
    // deal with the containing Document
    | (t,lst) -> ([],t) :: goThruDoc 0 [] (t,lst)

// Copied from the Assignment sheet to ensure maximum correctness
let expected = [([], "Compiler project");
    ([1], "Background");
    ([2], "The Programming Language");
    ([2;1], "Expressions");
    ([2;1;1], "Arithmetical Expressions");
    ([2;1;2], "Boolean Expressions");
    ([2;2], "Statements");
    ([2;2;1], "Basics");
    ([2;2;2], "Switch statements");
    ([2;2;3], "Repeat statements");
    ([2;3], "Programs");
    ([3], "Tasks");
    ([3;1], "Frontend");
    ([3;2], "Backend")]
let tocTest1 = toc doc
let isIdentical = (expected = tocTest1)

printfn "Creating ToC of doc: %A \nIs it as expected? %b" tocTest1 isIdentical
```