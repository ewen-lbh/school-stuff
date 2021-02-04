open Format


(** Exercice 1/1 **)


let rec append l_1 l_2 = match l_1 with
	| [] -> l_2
	| h::t -> h::(append t l_2)


(** Exercice 1/2 **)


let rec aux l_1 l_2 = match l_1 with 
	| [] -> ()
	| h::t -> (l_2 := h :: (aux (l_1 t)))

let reverse l = 
	let reversed = ref [] in
	aux l reversed;
	!reversed

(** Exercice 1/3 **)


(*
Pour une liste de longueur n:
h_(n-1) :: h_(n-2) :: ··· :: [h_0]
*)


(** Exercice 2/1 **)


let rec binom n k = match (n, k) with
	| (_, 0) -> 1
	| (0, _) -> 1
	| _ -> (binom (n-1) k) + (binom (n-1) (k-1))


(** Exercice 2/2 **)


let binom n k = 
	let values = Array.make_matrix (n+1) (k+1) 0 in
	c.(0).(0) <- ::::::::::::::::::::::::::::::::::
	for i = 0 to n do
	for j = 0 to k do

	done;
	done;

(*** Output ***)

let () =
	print_string "[";
	List.iter (printf "%d ") (append [1; 2; 3] [4]);
	print_string "]\n";
	print_string "[";
	List.iter (printf "%d ") (reverse [1; 2; 3]);
	print_string "]\n";
