open System
 
let rec is_palindromic (a:string) =
    let length = a.Length;
    match a with
        | ""  -> true
        | x -> match length with
                 | 1 -> true
                 | _ -> x.[0] = x.[length-1] && 
                       is_palindromic (x.Substring(1,(length - 2)))
                  
let max_palindrome =
    let numbers = seq {
        for i in 100 .. 999 do
            for j in 100 .. 999 do
                if is_palindromic(Convert.ToString(i*j)) then yield (i*j) }
    Seq.max numbers
