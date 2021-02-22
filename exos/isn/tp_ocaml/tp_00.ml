open Format

(** Exo 1 *)

let rec u n = match n with
    | 0 -> -2.
    | _ -> sqrt (2. +. (u (n-1)));;

(** Exo 2 *)
let rec pgcd a b = match b with
    | 0 -> abs a
    | _ -> pgcd b (a mod b);;

(** Exo 3 *)
let rec dichomotie f a b epsilon =
    let x = (a+b)/2
    (* while (a < b) (* and (f(a) * f(b)) < 0 *) *)
    while abs(a - b) > epsilon
        if 


let () = 
    printf "%f\n" (u 4);
    printf "%d\n" (pgcd 7 9);;
