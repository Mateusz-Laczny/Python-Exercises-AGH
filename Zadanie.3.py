# -*- coding: utf-8 -*-

# Na wyjątkowo długiej ulicy było N budynków o numerach od 0 do N. Pewien skrupulatny listonosz zapisywał numery
# odwiedzanych budynków. Po wielu dniach pracy miał w notesie M wpisów (gdzie M > N). Listonosz był niespełnionym
# analitykiem więc bardzo interesowało go:
#
# a) W jakiej kolejności odwiedził każdy z budynków po raz pierwszy, bez uwzględniania powtórek.
# b) Ile razy odwiedził każdy z budynków ?
#
# W punkcie a) jako rezultat program powinien wypisać listę numerów budynków w takiej kolejności, w jakiej listonosz odwiedzał je po raz pierwszy. Na przykład:
# LOOOONG_STREET_VISITS = [2, 5, 4, 5, 2, 1]
# Rezultat: [2, 5, 4, 1]
#
# W punkcie b) program powinien wypisać zestawienie "Numer budynku : liczba odwiedzin", w dowolnej formie.
#
# Uwaga: Punkt a) zadania przetestuj najpierw dla małych wartości N, M, a potem ustaw N = 10000 , M = 100000 i zmierz czas
# wywołania programu (funkcje start_time, print_time). Porównaj swoje wyniki z kolegami
# i zastanów się czy nie możesz przyspieszyć swojego programu.
#
# Podpowiedź: do rozwiązania zadań przyda się lista, zbiór oraz słownik.

import random
import time


N = 5
M = 10

LOOOONG_STREET_VISITS = [random.randint(0, N) for i in range(M)]


def start_time():
    global t_start
    t_start = time.time()

def print_time():
    print("Czas wywołania: " + str(time.time() - t_start))


if __name__ == '__main__':
    start_time()

    NUMERY_DOMOW = []

    print(LOOOONG_STREET_VISITS, '\n')

    #Podpunkt a
    for x in LOOOONG_STREET_VISITS:
        if x not in NUMERY_DOMOW:
            NUMERY_DOMOW.append(x)

    print(NUMERY_DOMOW, '\n')

    #Można też użyć porad mądrych ludzi ze Stack Overflow
    #i zrobić tak (podobno najlepsza metoda)
    from collections import OrderedDict
    print(list(OrderedDict.fromkeys(LOOOONG_STREET_VISITS)), '\n')

    #Podpunkt b
    #NUMERY_DOMOW.sort()

    for x in range(min(LOOOONG_STREET_VISITS), max(LOOOONG_STREET_VISITS) + 1):
       ilosc = LOOOONG_STREET_VISITS.count(x)
       print("Numer", x , ':' ,ilosc)


    print_time()

