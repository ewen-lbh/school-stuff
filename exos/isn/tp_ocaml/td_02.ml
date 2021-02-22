open Format

(** Exercice 1/1 **)

let tri tab =
    let maxi t n =
        let max_idx = ref 0 in
        for i = 1 to n do
            if t.(i) > t.(!max_idx) then
                max_idx := i
        done;
        !max_idx
    in
    let n = Array.length tab in
    let temp = ref 0 in
    for i = 1 to n do
        let max_idx = maxi tab (n-i) in
        temp := tab.(n-i);
        tab.(n-i) <- tab.(max_idx);
        tab.(max_idx) <- !temp
    done;
    tab


(** Exercice 1/2 **)


(* 
On a  i  tests pour chaque  i  de  1  à  n  .
On a

    sum_(i=1)^n i = n(n+1)/2 = O(n²)

*)


(** Exercice 1/3 **)


(* 

Dans le pire des cas, le tri est également un O(n²)

*)


(** Exercice 2/1 **)

(* On parcourt la liste, on enlève le max, on le met dans le 
résultat et on recommence jusqu'à ce que la liste initiale soit vide. *)


(** Exercice 2/2 **)


let sort_list l =
    let rec maxi l acc_max acc_list_nomax = match l with
        | [] -> acc_max, acc_list_nomax
        | h::t when h > acc_max -> maxi t h (acc_max::acc_list_nomax)
        | h::t -> maxi t acc_max (h::acc_list_nomax)
    in
    let rec walk l sorted_l = if l = []
        then sorted_l
        else 
            let maximum, list_nomax = maxi (List.tl l) (List.hd l) [] in
            walk list_nomax (maximum::sorted_l);
    in
    walk l []


(** Exercice 3/1 **)
 

let insertion_sort_list l =
    let rec insert element to_sort sorted = match to_sort with
        | [] -> sorted
        | h::t -> if element > h then insert element t (h::sorted)
                                 else insert h (element::sorted) to_sort
    in
    let rec walk to_sort sorted = match to_sort with
        | [] -> sorted;
        | h::t -> walk t (insert h sorted [])
    in
    walk l []

let () = 
    printf "[|";
    Array.iter (printf "%d, ") (tri [|1; 4; 5; 6; 2; 3; 3; 5; 1|]);
    printf "|]\n";

    printf "[";
    List.iter (printf "%d, ") (sort_list [1; 4; 5; 6; 2; 3; 3; 5; 1]);
    printf "]\n";

    printf "[";
    List.iter (printf "%d, ") (insertion_sort_list [1; 4; 5; 6; 2; 3; 3; 5; 1]);
    printf "]\n";
