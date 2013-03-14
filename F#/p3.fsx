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

let problem3 = Seq.max(find_factorial 600851475143L);;