let rec isPalindromic (str:string) =
    let length = str.Length

    match str with
    | "" -> true
    | x -> match length with
            | 1 -> true
            | _ -> x.[0] = x.[length - 1] && isPalindromic(x.Substring(1, length - 2))


let answers = seq {
    for i in 100 .. 999 do
        for j in 100 .. 999 do
            let prod = i*j
            if isPalindromic(prod.ToString()) then yield i*j
}

let problem4 = Seq.max(answers);;