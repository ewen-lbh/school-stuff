open Format

(** 3/1 **)

(* Zéro :p *)

(** 3/2 **)

let bien_parenthese mot = 
        let ouvrantes = ref 0 in
        let fermantes = ref 0 in
        let i = ref 0 in
                while !i < (String.length mot) && ouvrantes >= fermantes do
                        i := !i + 1;
                        match mot.[!i-1] with
                        | '(' -> (ouvrantes := !ouvrantes + 1)
                        | ')' -> (fermantes := !fermantes + 1)
                        | _ -> ();
                done;
                !ouvrantes = !fermantes

                
(** 3/3 **)

(*

Soient  u, v  des mots bien parenthésés

## <==

Traitons deux cas.

### 1er cas (  mot = ε  )

Alors mot est bien parenthésé par définition.

### 2e cas (  mot = (u)v  )

- u  a autant de parentheses ouvrantes que fermantes et  v  aussi, on rajoute une ouvrante et une fermante, donc il y a autant d'ouvrantes que de fermantes

- tout préfixe de  mot  

## ==>

# Contre-exemple:

Le mot  (uv)  est bien parenthésé, pourtant, il n'est ni égal à  ε  , ni de la forme  (u)v  .
Un autre exemple:  u(v)  (et _heuresement_ que celui-là marche, c'est un peu la syntaxe pour appeler une fonction quoi.)

"Question sur le forum" (http://mpsi.daudet.free.fr/forum/viewtopic.php?f=45&t=74)

*)

(** 3/4 **)

let rec decompose mot = match (String.length mot) with
        | 0 -> failwith "mot vide"
        | _ when not (bien_parenthese mot) -> failwith "poubelle, ton mot!"
        | _ -> (String.sub mot 1 )

let () =
        printf "(()())(: %B, ((())): %B\n" (bien_parenthese "(()())(") (bien_parenthese "((()))");