let factor_integer (n:int64) = 
    let rec find_factor acc (n_p:int64) num =        
        if num < n_p then
            acc
        elif num % n_p = 0L then 
            find_factor (n_p::acc) n_p (num/n_p)
        else 
            find_factor acc (n_p + 1L) num
    find_factor [] 2L n

let euler_3 = Seq.max (factor_integer 600851475143L)
