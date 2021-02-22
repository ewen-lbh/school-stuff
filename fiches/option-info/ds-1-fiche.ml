let rec is_sorted l = match l with
	| [] -> true
	| [a] -> true
	| h1::h2::t -> h1 <= h2 && is_sorted(h2::t)


let bien_parenthese mot = 
	let ouvrantes = ref 0 in
	let fermantes = ref 0 in
	let i = ref 0 in
	while !i < (String.length mot) && (!ouvrantes) >= (!fermantes) do
		incr i;
		match mot.[!i] with
		| '(' -> (incr ouvrantes)
		| ')' -> (incr fermantes)
		| _ -> ()
	done;
	!ouvrantes = !fermantes

let catalan n =
	let c = Array.make (n+1) 0 in
	c.(0) <- 1;
	for i = 1 to n do
		for k = 0 to (i-1) do
			c.(i) <- c.(i) + c.(k) * c.(i-1-k)
		done;
	done;
	c.(n)

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

let solve_quadratic a b c =
	if a = 0 then failwith "given coefficients do not form a second-degree polynomial";
	let discriminant = b**2.0 -. 4.0*.a*.c in
	if discriminant > 0.0 then
		let root_of_discriminant = sqrt discriminant in
		[ (-.b -. root_of_discriminant)/.(2.*.a); (-.b +. root_of_discriminant)/.(2.*.a) ] 
	else if discriminant < 0.0 then
		[]
	else
		[ (-.b)/.(2.*.a) ]

let rec n_adic_valuation n x = match x with
	|_ when x mod 2 != 0 -> 0
	|_ -> 1 + n_adic_valuation n (x/n)

let v2 = n_adic_valuation 2
