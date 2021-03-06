open Format
open Fun

let print_list l =
	print_string "[";
	List.iter (function el -> printf "%d " el ) l;
	print_string "]\n"

let print_array a =
	print_string "[|";
	Array.iter (function el -> printf "%d " el ) a;
	print_string "|]\n"

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


let rec longueur l = match l with
	| [] -> 0
	| h::t -> 1 + (longueur t)

let rec mapper l f = match l with
	| [] -> []
	| h::t -> f h :: mapper t f

let rec concatener l1 l2 = match l1 with
	| [] -> l2
	| h1::t1 -> h1 :: concatener t1 l2


(** Exercice 10 **)

let rec recherche_dichotomique needle haystack =
	let rec aux upper_bound lower_bound =
		let midpoint = (lower_bound+upper_bound)/2 in 
		match (upper_bound-lower_bound) with
			| k when k < 0 -> false
			| 0 -> haystack.(lower_bound) = needle
			| _ when haystack.(midpoint) = needle -> true
			| _ when haystack.(midpoint) > needle -> aux lower_bound (midpoint-1)
			| _ when haystack.(midpoint) < needle -> aux (midpoint+1) upper_bound
	in
	aux 0 (Array.length haystack)


(** Exercice 11 **)

(** 11/1 **)
(* a+b = (n-1)+(a-1) = (n-1)+(n-1-1) = 2*n-3 *)

(** 11/2 **)
(* id *)

(** 11/3 **)
(* ça plante, y manque un rec à aux *)
(* sinon, c'est id *)


(** Exemple: récursivité croisée et `and` **)


let rec pair n = match n with
	| 0 -> true
	| _ -> impair (n-1)
and impair n = match n with
	| 0 -> false
	| _ -> pair (n-1)


(** Exercice 12 **)


let () =
	let birth = ref 7 in
	birth := !birth + 16;
	printf "%d\n" !birth


(** Exercice 13 **)


(* let n_adic_valuation n x =
	let count = ref 0 in
	let mut_x = ref n in
	while (!mut_x mod n) = 0 do
		incr count;
		mut_x := !mut_x / n
	done;
	!count *)

let rec n_adic_valuation n x = match x with
	|_ when x mod 2 != 0 -> 0
	|_ -> 1 + n_adic_valuation n (x/n)

let v2 = n_adic_valuation 2


(** Exercice 14 **)


let range start stop = 
	let result = Array.make (stop - start) 0 in
	for i = start to stop do
		print_array result;
		result.(stop-start-i) <- i;
	done;
	result


(** Exercice 15 **)


let factorielle_beurk n =
	let value = ref 1 in
	for i = 1 to n do
		value := !value * i
	done;
	!value


(** Exercice 16 **)


let solve_quadratic a b c =
	if a != 0 then failwith "j'ai dis un polynôme de degré **2** connard!";
	let discriminant = b**2.0 -. 4.0*.a*.c in
	if discriminant > 0.0 then
		let root_of_discriminant = sqrt discriminant in
		[ (-.b -. root_of_discriminant)/.(2.*.a); (-.b +. root_of_discriminant)/.(2.*.a) ] 
	else if discriminant < 0.0 then
		[]
	else
		[ (-.b)/.(2.*.a) ]


(** Exercice 17 **)





(** Exercice 18 **)

(* let euclidian_division a b = if b = 0 then -1, -1 else (a/b), (a mod b) *)

let euclidian_division a b =
	try a/b, a mod b with
		|_ -> -1, -1


(** Exercice 19 **)


let is_prime n =
	try
		for divisior = 2 to int_of_float (sqrt (float_of_int n)) do
			if (n mod divisior) = 0 then failwith "found a divisor"
		done;
		(n > 1)
	with
		| Failure "found a divisor" -> false

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
	
	
	hellowarudo;
	
	
	(** Exercice 9 **)
	
	(* List.length retourne le nombre d'éléments *)

	printf "%d\n" (longueur [1; 2; 3; 4; 0; 6789]);

	(* List.map retourne l'image directe de la liste par la fonction donnée *)

	printf "%f\n" (List.hd (mapper [1.7; 2.; 4.2; 5.1; 10.0] sin));

	(* List.concat retourne une liste comportant les éléments de la première puis ceux de la deuxième *)

	(* List.iter (function x -> printf "%d, " x) (concatener [1; 3; 4] [3; 5; 6]); *)
	print_list (concatener [1; 3; 4] [3; 5; 6]);
	
	
	(** Exercice 10 **)
	
	
	printf "%B\n" (recherche_dichotomique 1 [|0;2;4;6;8;10;12;14;16;20|]);
	printf "%B\n" (recherche_dichotomique 2 [|0;2;4;6;8;10;12;14;16;20|]);
	printf "%B\n" (recherche_dichotomique 18 [|0;2;4;6;8;10;12;14;16;20|]);
	
	
	(** Exercice 12 **)

	
	
	(** Exercice 13 **)
	
	
	(* print_int (v2 2048);
	print_string "\n";
	 *)
	
	(** Exercice 14 **)
	
	
	print_array (range 0 99);
	
	
	(** Exercice 16 **)
	
	
	printf "[";
	List.iter (printf "%f ") (solve_quadratic 1. 0. 0.);
	printf "]\n";
	printf "[";
	List.iter (printf "%f ") (solve_quadratic 1. (-.3.) 2.);
	printf "]\n";

	

	(* end *)
