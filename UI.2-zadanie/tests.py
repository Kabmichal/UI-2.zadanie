from ui import heuristika, solve, succes, konvertuj
from actions import *
import ast
import math
import json
from random import randint


def load_file():
    """Nacitanie a spracovanie textoveho suboru v ktorom su vstupy"""
    list_of_lists = []
    with open('inputs', 'r') as myfile:
        for line in myfile:
            data = []
            numbers = line.split(',')
            for number in numbers:
                if (number != '\n'):
                    data.append(int(number))
            list_of_lists.append(data)
        return list_of_lists


def parse_list():
    """spustenie testov pre kazdu postupnost krokov, ktora bola vyhodnotena ako uspesna"""
    lines = load_file()
    while lines.__len__() != 0:
        array = lines.pop()
        strlen = int(math.sqrt(array.__len__()))
        start_test(array, strlen)


def test_vypis(value, n):
    """ zistujem ci sa kazde cislo nachadza v liste iba raz"""
    for i in range(1, n * n + 1, 1):
        if i not in value:
            return False
    return True


def test_dlzka(value, n):
    """ zistujem ci je dlzka pola == velkosti mapy"""
    if len(value) != n * n:
        return False
    return True


def total_sum(n):
    """ scitavanie cisel od 1 po velkost mapy"""
    return sum(range(n + 1))


def test_sum(value, n):
    """ kontrola ci sa sucet cisel vo vyslednom poli == suctu cisel z velkosti mapy"""
    if (sum(value)) != total_sum(n * n):
        return False
    return True


def test_move(value):
    pom = value.index(value.max)
    print(pom)


def test_konvertuj(pozicia, n):
    """ test ci funkcia spravne konvertuje 1d pole do 2d"""
    x, y = konvertuj(pozicia, n)
    if x * n + y == pozicia:
        return True
    return False


def test_heuri(array, index, x, y, n):
    """ testovanie heuristiky"""
    if heuristika(array, index, x, y, n) <= 7:
        return True
    return False


def check_move(value, n):
    """ testovanie pohybu - ci sa z konca viem dostat na zaciatok"""
    index = value.index(max(value))
    counter = max(value)
    calculator = 0
    moves = [index - n + 2, index + n + 2, index + n - 2, index - n - 2, index + 2 * n - 1, index + 2 * n + 1,
             index - 2 * n - 1, index - 2 * n + 1]
    while 1:
        calculator += 1
        for m in moves:
            if m < n * n and m >= 0:
                if value[m] == counter - 1:
                    counter -= 1
                    index = m
                    calculator = 0
                    moves = [index - n + 2, index + n + 2, index + n - 2, index - n - 2, index + 2 * n - 1,
                             index + 2 * n + 1, index - 2 * n - 1, index - 2 * n + 1]
                    if counter == 1:
                        return True
        if calculator == moves.__len__() + 1:
            return False


def start_test(pom_list, n):
    """ vykonavanie jednotlivych testov"""

    index = randint(0, n)
    x, y = konvertuj(index, n)
    print("test bezi pre pole", pom_list)
    print("velkost mapy je", n)
    print("Kazde cislo sa v liste nachadza len raz: ", test_vypis(pom_list, n))
    print("Dlzka pola je rovna velkosti mapy:       ", test_dlzka(pom_list, n))
    print("Test na sucet cisel:                     ", test_sum(pom_list, n))
    print("Test na prevod suradnic z 2d do 1d:      ", test_konvertuj(pom_list[randint(0, n)], n))
    print("Odtestovanie heuristiky:                 ", test_heuri(pom_list, index, x, y, n))
    print("Skontrolovanie spravnosti pohybov:       ", check_move(pom_list, n))
    print("\n\n\n")


parse_list()
