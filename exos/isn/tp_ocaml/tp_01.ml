open Format
open Fun

(* let print truc = *)
    (* printf "{ fmt %}\n" truc *)

let a = 4611686018427387903

(** Exercice 4 **)
let python_is_couprie = "Hello, World!"


(** Exercice 5 **)


let ou a b = match a with
    | true -> true
    | false -> b


(** Exercice 6 **)

let compose f g x = f (g x)

(* let rec itere f n x = match n with
    | 0 -> x
    | _ -> f (itere f (n-1) x) *)

let rec itere f n = match n with
    | 0 -> id
    | _ -> compose f (itere f (n-1))



(** Exercice 7 **)

let corrompre () = ()
let juste_un_2 () = 2


(** Exercice 8 **)


let hellowarudo () =
    print_string (python_is_couprie ^ "\n")


(** Exercice 9 **)


let longueur l = match l with
    | [] -> 0
    | _ -> longueur ...?




let () =
    
    
    (** Exercice 1 **)
    
    
    printf "%d et %d et %d\n" (a-1) a (a+1);
    
    
    (** Exercice 2 **)
    
    
    printf "<: %b\n" (4611686018427387902. < 4611686018427387904.);
    printf "=: %b\n" (4611686018427387902. = 4611686018427387904.);
    printf ">: %b\n" (4611686018427387902. > 4611686018427387904.);
    
    
    (** Exercice 3 **)
    
    
    printf "true>false: %b\n" (true<false);
    (* Table de ^ *)
    printf "^     | false | true\nfalse | %B | %B\ntrue  | %B | %B\n\n"
        (false && false)
        (false && true)
        (true && false)
        (true && true);
    (* Table de v *)
    printf "v     | false | true\nfalse | %B | %B\ntrue  | %B  | %B\n\n"
        (false || false)
        (false || true)
        (true || false)
        (true || true);
    (* Short-circuiting *)
    printf "%B\n" ((0=1) && (0=1/0));
    (* printf "%B\n" ((0=1/0) && (0=1)); Throws an error *)
    
    
    (** Exercice 4 **)
    
    
    (* Python is couprie *)
    printf "%c\n" python_is_couprie.[4];
    printf "%s\n" (String.make 1000 'a');
    
    
    (** Exercice 5 **)
    printf "v     | false | true\nfalse | %B | %B\ntrue  | %B  | %B\n\n"
        (ou false false)
        (ou false true)
        (ou true  false)
        (ou true  true);
    
    
    (** Exercice 6 **)
    
    
    for n = 0 to 100 do
        printf "%f, " (itere sin n 1.);
    done;
    printf "\n";
    
    
    (** Exercice 7 **)
    
    (* 7/1: C'est unit. *)
    
    
    (** Exercice 8 **)
    
    
    hellowarudo ()
    
    
    (** Exercice 9 **)
    
    
    (* List.length retourne le nombre d'éléments *)

    (* end *)
