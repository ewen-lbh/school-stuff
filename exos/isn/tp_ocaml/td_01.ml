open Format

(** 3/1 **)

(* Zéro :p *)

(** 3/2 **)

let bien_parenthese mot = 
	let ouvrantes = ref 0 in
	let fermantes = ref 0 in
	let i = ref 0 in
		while !i < (String.length mot) && (!ouvrantes) >=(!fermantes) do
			i := !i + 1;
			match mot.[!i] with
			| '(' -> (ouvrantes := !ouvrantes + 1)
			| ')' -> (fermantes := !fermantes + 1)
			| _ -> ();
		done;
		!ouvrantes = !fermantes

		
(** 3/3 **)

(* Soit  n  le 1er moment où  "fermantes" = "ouvrantes"
 * On a alors
 *      
 *      w = (u)v
 *
 * Soit  n  la longueur de  u  .
 * Sachant que  w  est bien parenthésé on a  v  bien parenthésé.
 *   u'  bien parenthésé de longueur positive non nulle.
 * Il commence donc par ouvrir une parenthèse et se termine en fermat la parenthèse et u est bien parenthésé.
 *)


let decompose mot = 
	let ouvrantes = ref 1 in
	let fermantes = ref 0 in
	let n = String.length mot in
	let i = ref 1 in
		while !i < n && (!ouvrantes) > (!fermantes) do
			i := !i + 1;
			match mot.[!i] with
			| '(' -> (ouvrantes := !ouvrantes + 1)
			| ')' -> (fermantes := !fermantes + 1)
			| _ -> ();
		done;
		printf "%d\n" !i;
		if !i < n then
			String.sub mot 1 (!i-2), String.sub mot !i (n - !i)
		else
			String.sub mot 1 (n-2), ""



(** 3/5 **)

(* sum from 0 to n-1 of c_k * c_(n-1-k) *)

(* let catalan n = 
	let values = Array.make (n+1) 1 in
	printf "%d\n" values.(0);
	for i = 2 to n do
		(* printf "c_%d = %d\n" i (values.(i)); *)
		let c = ref 0 in
		for k = 0 to (i-1) do
			(* printf "\tc_%d, c_%d = %d, %d\n" k (i-1-k) values.(k) values.(i-1-k); *)
			c := !c + values.(k) * values.(i-1-k);
		done;
		values.(i) <- !c;
	done;
	values.(n) *)

(* CORRECTION *)

let catalan n =
	let c = Array.make (n+1) 0 in
	c.(0) <- 1;
	for i = 1 to n do
		for k = 0 to (i-1) do
			c.(i) <- c.(i) + c.(k) * c.(i-1-k)
		done;
	done;
	c.(n)



(** Exercice 4/1 **)


let rec f x = f x


(** Exercice 4/2 **)

(*

La fonction s'appelle si elle termine et renvoie True sinon.

Si elle se termine, alors elle ne se termine pas, sinon elle se termine.
imp.

*)


(** Exercice 4/3 **)


(* :sad: il est impossible de coder une fonction déterminant si une autre termine ou pas. *)

let () =
	printf "%B, %B\n" (bien_parenthese "(()())(") (bien_parenthese "(((fzefez))fefz)");
	let u, v = decompose "(()()())((()))()" in
	printf "%s\t%s\n" u v;
	print_int (catalan 20);
	(* f 3; *)
