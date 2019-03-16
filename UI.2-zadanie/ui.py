from actions import *
import simplejson
import pickle
import json

def konvertuj(pozicia,n):
    """ funkcia konvertuj - prepis jednorozmerneho pola na suradnice dvojrozmerneho pola,
        potrebne pre kontrolu, ci nevystupujem z pola
    """
    x = pozicia // n
    y = pozicia % n
    return x, y



def heuristika(value, index, x, y, n):
    """ funkcia heuristika mi ohodnoti dane policko (hodnotenie spociva v tom,
        ze si pocitam na kolko dalsich policok sa viem z danej pozicie dostat a su volne)
    """
    functions = [right_down, right_up, up_right, down_right, up_left, left_up, down_left, left_down]
    results = [f(value, index, x, y, n) for f in functions]
    return sum(results)



def add(total, value, stack, count):
    """ funkcia na pridavanie dalsich stavov
        (v pripade ze heuristika nenajde riesenie na prvykrat a potrebujem prehladavat dalej do hlbky)
    """
    number = total.__len__() - 1
    for i in range(number, 0, -1):
        value[total[i][1]] = count + 1  # ulozenie pozicie kde sa viem dostat do pola
        pom = value.copy()
        stack.append(pom)  # pridanie pola s aktualnym stavom do listu
        value[total[i][1]] = 0


def body(value, new_index, total, n):
    """tato funkcia mi ohodnoti policka do ktorych sa viem dostat a prida ich do listu"""
    poz1, poz2 = konvertuj(new_index,n)
    count = heuristika(value, new_index, poz2, poz1, n)  # ohodnotenie kazdej pozicie
    total.append([count, new_index])  # pridanie do listu


def check(value, index, total, y, x, n):
    functions=[right_up,right_down,left_down,left_up,down_left,down_right,up_left,up_right]
    moves=[index-n+2,index + n + 2,index + n - 2,index - n - 2,index + 2 * n - 1,index + 2 * n + 1,index - 2 * n - 1,index - 2 * n + 1]
    for f,m in zip(functions,moves):
       if f(value, index, x, y, n):
            new_index=m
            body(value, new_index, total, n)


def pohyb(value, n, stack, count):
    """ funkcia pohyb mi urcuje kde vsade sa viem pohnut"""
    index = value.index(max(value))  # zistenie maxima mi sluzi na najdenie indexu posledneho kroku kde sa nachadzam
    total = []
    y, x = konvertuj(index,n)  # prepis na dvojrozmerne pole pre kontrolu ci nepresahujem hranice mapy
    check(value, index, total, y, x, n)
    total.sort()  # sort listu - sluzi ako queue, 0 prvok beriem do postupnosti (ma najlepsie ohodnotenie podla heuristiky)
    add(total, value, stack, count)  # ostatne prvky z queue pridavam do listu
    if (total == []):  # ak je total prazdna mnozina, riesenie neexistuje
        return -1
    return total[0][1]  # returnem najmensi prvok z queue

def succes(value,pocitadlo,final,p):
    """tato funkcia sa zavola v pripade ze kon vie prejst celu sachovnicu"""
    print("Uspech ", value) #vypis pola
    with open("inputs", "a") as output:
        for val in value:
            output.write(str(val)+',')
        output.write('\n')
    pocitadlo += 1
    final.append(p)
    return pocitadlo,value

def solve(n):
    """funkcia solve vyriesi problem knight tour pre zadanu mapu"""
    pocitadlo = 0
    final = []
    for p in range(0, n * n):  # zistovanie poctu vyskytu prvkov
        stack = []
        value = [0] * n * n  # inicializacia samich 0 v poli
        counter = 0
        count = 1
        value[p] = count
        if n == 1:  # osetrenie ak velkost mapy == 1
            final.append(value)
        while min(value) == 0:  # ak min == 0, tak este niesom vo finalnom stave, final stav ma min 1
            counter += 1
            if counter == 10000:  # pocet pokusov po kolkych je prehladavanie vyhodnotene ako nedosiahnutelny cielovy stav
                print("Vysledny stav z tejto pozicie neexistuje")
                break
            new = pohyb(value, n, stack, count)  # index prvku s najmensim ohodnotenim podla heuristiky
            if new == -1:  # ak uloha nema riesenie
                # print("neuspech ",value)
                if stack == []:  # kontrola ak uz som prehladal vsetko a riesenie neexistuje mozem sa z hladania breaknut
                    break
                value = stack.pop()  # v pripade neuspechu berem najblizsi stav
                count = max(value)  # do countu si ulozim cislo posledneho kroku
            else:
                count+=1
                value[new]=count # poznacenie si pozicie ktora bola vyhodnotena za najlepsiu
                if min(value) != 0:  # ak minimum je 1 tak som dosiahol finalny stav
                    pocitadlo,value=succes(value,pocitadlo,final,p)
        if pocitadlo == 10:
            break
    return final

def main():
    n = (int(input()))  # vstup - velkost mapy
    print("\n\n\npozicie z ktorych sa da dostat:", solve(n),"\n\n\n")  # vypis pozicii z ktorych viem dosiahnut finalny stav

main()