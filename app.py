import random
import json
import time
import math

from functions.checks import is_monochromatic
from functions.utils import append_one, triplet_generator, refresh_numbers
from functions.misc import to_si

"""
Définition de toutes les couleurs
"""
colors = [
    "\033[31m",  # rouge
    "\033[32m",  # vert
    "\033[34m",  # bleu
    "\033[33m",  # orange
    "\033[35m",  # violet
    "\033[0m",  # blanc
]

"""
Saisie sécurisée sur le terme 'n' (nombre de couleurs) 
(n -> entier >= 2)
"""
n = input("Entrez le nombre de couleur (n >= 2): ")
while (not n.isdigit()) or (int(n) < 2):
    n = input("Entrez le nombre de couleur (n >= 2): ")
n = int(n)

if n <= 5:
    """
    On prend 'n' couleurs au hasard
    """
    outside_chosen_colors = random.sample(colors, n)

    """
    On applique le théorème sous forme de fonction
    """


    def schur(maximum: int, recheck_all: bool, numbers, numbers_colors,
              chosen_colors, number_of_color, start_counter):
        triplets = triplet_generator(maximum)
        passed = 0
        total = len(triplets)

        while passed < total:
            while recheck_all:
                passed = 0
                total = len(triplets)
                for triplet in triplets:
                    test_triplet = [
                        [triplet[0], numbers.get(triplet[0])],
                        [triplet[1], numbers.get(triplet[1])],
                        [triplet[2], numbers.get(triplet[2])],
                    ]
                    """
                    Pour N = 2 au premier tour:
                    test_triplet = [
                        [1, "bleu"],
                        [1, "bleu"],
                        [2, "bleu"],
                    ] 
                    """

                    if is_monochromatic(test_triplet):
                        # condtition pour voir si le tableau contenant les
                        # indices pour les couleurs est plein
                        # cf http://stackoverflow.com/q/3844931/
                        if (not numbers_colors
                            or [numbers_colors[0]] * len(numbers_colors)
                            == numbers_colors) \
                                and numbers_colors[0] == number_of_color - 1:
                            stop = time.perf_counter()
                            maximum -= 1
                            print("\n----------------------------")
                            print(f"{colors[1]}"
                                  f"S({number_of_color})={maximum}"
                                  f"{colors[5]}")
                            print("----------------------------")

                            # on charge la derniere bonne configuration
                            with open("output.json", "r") as f:
                                numbers = json.load(f)

                            row = ""
                            for number, color in numbers.items():
                                row += f"{color}{number} "

                            print(f"{row} {colors[1]} ✔ {colors[5]}")
                            print("----------------------------")
                            delta = stop - start_counter
                            print(f"Temps: {to_si(delta)}s")
                            return
                        else:
                            row = ""
                            for number, color in numbers.items():
                                row += f"{color}{number} "
                            print(f"{row} {colors[0]} ✘ {colors[5]}", end='\r')

                            numbers_colors = append_one(numbers_colors,
                                                        number_of_color, True)
                            numbers = refresh_numbers(numbers, chosen_colors,
                                                      numbers_colors)
                            recheck_all = True
                            break
                    else:
                        recheck_all = False
                        passed += 1
        else:
            with open("output.json", "w") as f:
                f.write(json.dumps(numbers))

            maximum += 1
            numbers_colors.append(0)
            numbers = refresh_numbers(numbers, chosen_colors, numbers_colors)
            recheck_all = True

            """
            On relance la fonction avec les nouvelles configurations
            """
            schur(maximum, recheck_all, numbers, numbers_colors, chosen_colors,
                  number_of_color, start_counter)


    """
    On lance la fonction avec:
    - N = 2 car pour 'n' >= 2, 'N' sera forcement >= 2 (1: bleu, 1: bleu, 2: rouge)
    
    variables préfixées par outside_ pour ne pas interferer avec celles de la 
    fonction: 
    - outside_numbers_colors = [0, 0] configuration des couleurs par défaut
    - outside_numbers -> on applique aux nombres les couleurs définies par 
                            outside_numbers_colors
    """
    N = 2

    outside_numbers_colors = [0 for _ in range(N)]
    outside_numbers = refresh_numbers(
        {},
        outside_chosen_colors,
        outside_numbers_colors
    )  # avec N = 2 -> {1: bleu, 2, bleu}

    """
    On lance le bouzin
    """
    start = time.perf_counter()
    schur(
        N,
        True,
        outside_numbers,
        outside_numbers_colors,
        outside_chosen_colors,
        n,
        start
    )
else:
    minimum_N = ((3 ** n) - 1) / 2
    maximum_N = 3 * math.factorial(n) - 1

    print(f"{minimum_N} <= S({n}) <= {maximum_N}")
