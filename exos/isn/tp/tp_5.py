from rich import print
from rich.rule import Rule
from rich.traceback import install

install()

## Convenience


def header(exo: int, subexo: int, text: str):
    print()
    print(Rule(f"[bold black]{exo}.{subexo}[/][dim])[/] {text}", align="left"))


## Exercice 0


def créerTableau(n: int) -> list[int]:
    return n * [0]


## Exercice 1.1


def créerTabVide(n: int) -> list[int]:
    return créerTableau(n + 1)


## Exercice 1.2


def estDansTab(tab: list[int], x: int) -> bool:
    if tab[0] == 0:
        return False
    for elem in tab[1 : tab[0] + 1]:
        if elem == x:
            return True
    return False


"""
Complexité:

O(1 + n(1)) = O(n)
"""

## Exercice 1.3


def ajouteDansTab(tab: list[int], x: int) -> None:
    if not estDansTab(tab, x):
        tab[0] += 1
        tab[tab[0]] = x


"""
Comportement si tab pleine:
On obtient un IndexError

Complexité:
O(1 + 1 + 1) = O(1)
"""

## Exercice 2.1

### Plan 1

plan_1 = [
    [5, 7],
    [2, 2, 3, 0, 0],
    [3, 1, 3, 5, 0],
    [4, 1, 2, 5, 4],
    [2, 3, 5, 0, 0],
    [3, 2, 3, 4, 0],
]

### Plan 2

plan_2 = [
    [5, 4],
    [1, 2, 0, 0, 0],
    [3, 1, 3, 4, 0],
    [1, 2, 0, 0, 0],
    [2, 2, 5, 0, 0],
    [1, 4, 0, 0, 0],
]

## Exercice 2.2

Plan = list[list[int]]


def creerPlanSansRoute(n: int) -> Plan:
    return [n, 0] + [[0] * n] * n


## Exercice 2.3


def estVoisine(plan: Plan, x: int, y: int) -> bool:
    x_neighbors = plan[x]
    y_neighbors = plan[y]
    return estDansTab(x_neighbors, y) and estDansTab(y_neighbors, x)


## Exercice 2.4


def ajouteRoute(plan: Plan, x: int, y: int) -> None:
    ajouteDansTab(plan[x], y)
    ajouteDansTab(plan[y], x)


"""
Il n'y a aucun risque de dépassement des listes grâce à l'utilisation de ajouteDansTab,
qui:

1. Ne rajoute pas l'élément s'il existe déjà
2. Ne dépasse jamais la capacité

De plus, une ville ne pouvant avoir plus de voisins qu'il n'y a de villes dans le plan,
le seul cas où 2. pourra se produire est si la ville x ou y n'existe pas dans le plan
(i.e. son numéro est supérieur au nombre de villes dans le plan)
"""

## Exercice 2.5


def compute_routes(plan: Plan) -> list[list[int]]:
    routes: Plan = plan[0][1] * créerTabVide(2)
    for city, city_neighbors in enumerate(plan[1 : plan[0][0] + 1]):
        city += 1
        if not city_neighbors[0]:
            # la ville n'a pas de voisins, hello darkness my old friend
            continue
        for neighbor in city_neighbors[1 : city_neighbors[0] + 1]:
            if (
                neighbor != 0
                and neighbor != city
                and not estDansTab(routes, [neighbor, city])
            ):
                ajouteDansTab(routes, [city, neighbor])
    return routes


def afficheToutesLesRoutes(plan: Plan) -> None:
    routes = compute_routes(plan)
    assert routes[0] == plan[0][1]
    print(routes[1 : routes[0] + 1])


"""
Complexité:
O(n · ( 1 + 1 + (n-1) · (1 + 1 + O(m) · (O(1)) )) = O(n² · m)
"""

header(2, 5, "Plan 1")
afficheToutesLesRoutes(plan_1)
header(2, 5, "Plan 2")
afficheToutesLesRoutes(plan_2)
header(2, 5, "Figure 2")

## Exercice 3.1

## Exercice 3.O
fig_2 = [
    [11, 13],
    [2, 2, 6] + 9 * [0],
    [2, 1, 7] + 9 * [0],
    [2, 8, 4] + 9 * [0],
    [2, 3, 8] + 9 * [0],
    [2, 6, 10] + 9 * [0],
    [3, 1, 5, 7] + 8 * [0],
    [3, 6, 2, 8] + 8 * [0],
    [4, 7, 3, 4, 9] + 7 * [0],
    [2, 8, 11] + 9 * [0],
    [2, 5, 11] + 9 * [0],
    [2, 10, 9] + 9 * [0],
]
afficheToutesLesRoutes(fig_2)

import random

entierAléatoire = lambda k: random.randint(1, k)

## 3.1


def coloriageAléatoire(
    plan: Plan, couleur: list[int], k: int, start: int, end: int
) -> None:
    for city, _ in enumerate(plan[1 : plan[0][0] + 1]):
        if city + 1 == start:
            # ajouteDansTab(couleur, 0)
            couleur.append(0)
        elif city + 1 == end:
            # ajouteDansTab(couleur, k + 1)
            couleur.append(k + 1)
        else:
            c = entierAléatoire(k)
            # ajouteDansTab(couleur, c)
            couleur.append(c)


header(3, 1, "Figure 2, couleurs")
# fig_2_colors = créerTableau(len(fig_2))
fig_2_colors = [None]
coloriageAléatoire(fig_2, fig_2_colors, 3, 6, 4)
fig_2_colors = [None, 1, 2, 3, 4, 1, 0, 1, 2, 3, 3, 1]
print(fig_2_colors)
# assert fig_2_colors[0] == fig_2[0][0]

## 3.2


def voisinesDeCouleur(
    plan: Plan, couleur: list[int], target_city: int, target_color: int
) -> list[int]:
    neighbors = créerTabVide(plan[target_city][0])
    for neighbor in plan[target_city][1 : plan[target_city][0] + 1]:
        print(neighbor, couleur[neighbor])
        if couleur[neighbor] == target_color:
            ajouteDansTab(neighbors, neighbor)
    return neighbors


header(3, 2, "Voisines de 1 ayant la couleur 2")
print(voisinesDeCouleur(fig_2, fig_2_colors, 1, 2))

## 3.3


def voisinesDeLaListeDeCouleur(
    plan: Plan, couleur: list[int], liste: list[int], c: int
):
    neighbors = créerTabVide(sum(plan[city][0] for city in liste))
    for city in liste:
        for neighbor in voisinesDeCouleur(plan, couleur, city, c)[1:]:
            ajouteDansTab(neighbors, neighbor)
    return neighbors


header(3, 3, "Voisines de 1, 5, 7 ayant la couleur 2")
print(voisinesDeLaListeDeCouleur(fig_2, fig_2_colors, [1, 5, 7], 2))


## 3.4

header(3, 4, "Existance d'un chemin en arc-en-ciel ?")


def existeCheminArcEnCiel(
    plan: Plan, couleur: list[int], k: int, s: int, t: int
) -> bool:
    current_path = []
    start, end = [None]*2
    print(compute_routes(plan))
    for route in compute_routes(plan)[1:plan[0]+1]:
        # Check if this route forms a path with the preceding
        if route[0] != end:
            continue
        start,end = route
        current_path += route
        print(current_path)

existeCheminArcEnCiel(fig_2, fig_2_colors, 3, 6, 4)
