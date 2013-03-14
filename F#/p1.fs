module p1

let problem1 =
    [1..999] |> Seq.sumBy (fun x -> if (x%3 = 0 || x%5 = 0) then x else 0) ;;
