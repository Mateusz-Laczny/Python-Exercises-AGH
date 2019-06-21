# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = "Podział tekstu na wyrazy to nie takie proste zadanie. " \
        "Najpierw trzeba usunąć z tekstu znaki interpunkcyjne - przecinki, kropki i myślniki. " \
        "Spróbuj to zrobić na tym tekście. "

    print(a)


    b = "Dla wygody często zamienia się też wszystkie duże litery na małe. Wykonaj taką operację na tym tekście. "

    print(b)


    c = "Oczywiście trzeba jeszcze pociąć tekst w miejscach gdzie pojawia się spacja. Najpierw potnij na próbę ten tekst. "

    print(c)


    d = "Ok, masz już wszystko co trzeba. Teraz połącz teksty a-d w jeden i wykonaj na nim wszystkie powyższe operacje. " \
        "Potem napisz program, który wczyta ciąg znaków podany z klawiatury i wypisze te wyrazy, które się od niego zaczynają."


    words = []


    a_bez_znakow = a.replace(",","")\
    .replace("-","")\
    .replace(".","")

    print("\n", a_bez_znakow)

    male_b = b.lower()

    print( "\n",male_b)

    podzielone_c = c.split()

    print ('\n')

    print(podzielone_c)

    pelny_tekst = a + b + c + d

    pelny_tekst = pelny_tekst.replace(",","")\
    .replace(".","")\
    .replace("-","")

    pelny_tekst = pelny_tekst.lower()

    pelny_tekst = pelny_tekst.split()

    ciag_znakow = input("Podaj ciąg znaków:")

    for x in pelny_tekst:
        if x.startswith(ciag_znakow):
            words.append(x)


    print("\n", words)


