open Format

(** 3/1 **)

(* Zéro :p *)

(** 3/2 **)

let bien_parenthese mot = 
        let ouvrantes = ref 0 in
        let fermantes = ref 0 in
        let i = ref 0 in
                while !i < (String.length mot) && ouvrantes >=fermantes do
                        match mot.[!i] with
                        | '(' -> (ouvrantes := !ouvrantes + 1)
                        | ')' -> (fermantes := !fermantes + 1)
                        | _ -> ();
                        i := !i + 1;
                        printf "%d" !i;
                done;
                !ouvrantes = !fermantes

let () =
        printf "%B, %B" (bien_parenthese "(()())(") (bien_parenthese "((()))");
                
(** 3/3 **)

(* Mais oui c'est clair :malou: *)
