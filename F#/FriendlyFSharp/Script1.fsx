let rec factorial' =
    function
    | 0 -> 0
    | n -> n + factorial' (n-1)
    
let x = factorial' (3);; 