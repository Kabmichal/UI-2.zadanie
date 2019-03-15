from ui import heuristika, solve, succes, konvertuj
from actions import *


def test_vypis(value, n):
    #zistujem ci sa kazde cislo nachadza v liste iba raz
    for i in range(1, n * n + 1, 1):
        if i not in value:
            return False
    return True


def test_dlzka(value, n):
    #zistujem ci je dlzka pola == velkosti mapy
    if len(value) != n * n:
        return False
    return True


def total_sum(n):
    #scitavanie cisel od 1 po velkost mapy
    return sum(range(n + 1))


def test_sum(value, n):
    #kontrola ci sa sucet cisel vo vyslednom poli == suctu cisel z velkosti mapy
    if (sum(value)) != total_sum(n * n):
        return False
    return True


def test_move(value):
    pom = value.index(value.max)
    print(pom)


def test_konvertuj(pozicia, n):
    #test ci funkcia spravne konvertuje 1d pole do 2d
    x, y = konvertuj(pozicia, n)
    if x * n + y == pozicia:
        return True
    return False


def test_heuri(array, index, x, y, n):
    #testovanie heuristiky
    if heuristika(array, index, x, y, n) <= 7:
        return True
    return False


def check_move(value, n):
    #testovanie pohybu - ci sa z konca viem dostat na zaciatok
    index = value.index(max(value))
    counter = max(value)
    calculator = 0
    moves = [index - n + 2, index + n + 2, index + n - 2, index - n - 2, index + 2 * n - 1, index + 2 * n + 1,
             index - 2 * n - 1, index - 2 * n + 1]
    maximum = value.index(max(value))
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


def input_params():
    #v tejtto funkcii definujem vstupne parametre ktore chcem testovat
    #hodnoty na testovanie sa nachadzaju v inputs, na tych hodnotach som moj program testoval
    array = [5, 20, 15, 10, 3, 14, 9, 4, 21, 16, 19, 6, 23, 2, 11, 24, 13, 8, 17, 22, 7, 18, 25, 12, 1]
    n = 5  # velkost mapy
    index = 8  # zaciatocny index
    x = 6  # x - suradnica
    y = 2  # y - suradnica
    return array, index, x, y, n


def start_test():
    #vykonavanie jednotlivych testov
    array, index, x, y, n = input_params()
    final = []
    pom_list = []
    p = 11
    poc = 0
    poc, pom_list = succes(array, 0, final, p)
    print("vypis listu ", pom_list,"\n")
    print("Kazde cislo sa v liste nachadza len raz: ", test_vypis(pom_list, n))
    print("Dlzka pola je rovna velkosti mapy:       ", test_dlzka(pom_list, n))
    print("Test na sucet cisel:                     ", test_sum(pom_list, n))
    print("Test na prevod suradnic z 2d do 1d:      ", test_konvertuj(8, 3))
    print("Odtestovanie heuristiky:                 ", test_heuri(array, index, x, y, n))
    print("Skontrolovanie spravnosti pohybov:       ", check_move(pom_list, n))


start_test()
