open System

let find_factorial (num:int64) =
    let rec find_factorial_rec (n: int64) (divisor: int64) (list_primes) =
        
        if n < divisor then
            list_primes
        elif n%divisor = 0L then
            find_factorial_rec (n/divisor) (divisor) (divisor::list_primes) 
        else
            find_factorial_rec n (divisor+1L) list_primes 
    find_factorial_rec num 2L []

let count_occurences (list:List<int64>) =
    let grouped = 
        list
        |> Seq.groupBy(fun x -> x)
        |> List.
    grouped

let ans = count_occurences [1L; 1L; 2L; 3L; 3L];;

let problem5 =
    [2L..20L] 
    |> Seq.map(fun x -> find_factorial(x))
    |> Seq.iter(fun x -> count_occurences x)

Console.WriteLine(problem5)