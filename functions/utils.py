from typing import List


def append_one(custom_list: list, offset: int,
               exclusive: bool = False) -> list:
    """
    :Example:

    >>> append_one([0, 0, 2], 3)
    [0, 0, 3]
    >>> append_one([0, 3, 3], 4)
    [0, 3, 4]
    >>> append_one([0, 3, 3], 4, True)
    [1, 0, 0]

    :param custom_list: liste en entré
    :param offset: valeur a ne pas dépasser
    :param exclusive: si True : equivalent a strictement inférieur
    :return: liste une fois les additions faites
    """
    for k, value in enumerate(reversed(custom_list)):
        if value < offset - (1 if exclusive else 0):
            custom_list[~k] = value + 1
            return custom_list
        else:
            custom_list[~k] = 0
    return custom_list


def get_color(chosen_colors: list, p: int) -> str:
    """

    :param chosen_colors:
    :param p: indice
    :return: chosen_colors a l'indice "p modulo len(chosen_colors)" pour
    boucler sur chosen_colors
    """
    return chosen_colors[
        p % len(chosen_colors)
    ]


def triplet_generator(limit: int) -> list:
    """

    :param limit: Limite a ne pas dépasser dans la génération des triplets
    :return: liste des triplets possibles tels que (a, b, a+b) avec a+b <= N
    """
    triplets: List[List[int]] = []
    for a in range(1, limit):
        for b in range(a, (limit - a) + 1):
            c = a + b
            triplets.append([a, b, c])
    return triplets


def refresh_numbers(numbers: dict, chosen_colors, new_indexes: list) -> dict:
    """

    :param numbers: anciennes valeurs de numbers
    :param chosen_colors: liste des couleurs
    :param new_indexes: nouveaux indices pour les couleurs
    :return: numbers avec les nouveaux indices
    """
    for number, new_index in enumerate(new_indexes, start=1):
        numbers[number] = get_color(chosen_colors, new_index)
    return numbers
