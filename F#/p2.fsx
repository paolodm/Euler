
let rec fibonacci' =
    function
    | 0 -> 0
    | 1 -> 1
    | x -> fibonacci'(x-1) + fibonacci'(x-2)

let ans = 
    Seq.initInfinite fibonacci' 
        |> Seq.takeWhile(fun a -> a <= 4000000)
        |> Seq.filter (fun a -> a%2=0)
        |> Seq.fold (+) 0

ans;;

