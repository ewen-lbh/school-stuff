let rec is_sorted l = match l with
    | [] -> true
    | [a] -> true
    | h1::h2::t -> h1 <= h2 && is_sorted (h2::t)

let bien_parenthese mot =
    let o = ref 0 in
    let f = ref 0 in
    let i = ref 0 in
    while !i < (String.length mot) && !o >= !f do
        incr i;
        match mot.[!i] with 
        | '(' -> (incr o)
        | ')' -> (incr f)
        | _ -> ()
    done;
    !o = !f
