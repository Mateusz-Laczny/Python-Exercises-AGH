#    Polecenie:
#    Napisz program, który wczytuje ułamki zwykłe i skraca je do najprostszej postaci.
#    Na wejściu program powinien wczytać dwie liczby: licznik i mianownik.
#    Jako rezultat program powinien wypisać licznik i mianownik w skróconej formie lub pojedynczą wartość,
#    gdy ułamek reprezentuje liczbę całkowitą.
#    Przykłady:
#    Wejście:	Wyjście:
#    16	4
#    36	9
#
#    Wejście:	Wyjście:
#    20	10
#    2


def NWD(licznik, mianownik):
    while licznik != mianownik:
        if licznik > mianownik:
            licznik = licznik - mianownik
        else:
            mianownik = mianownik - licznik
    return licznik


if __name__ == '__main__':
    print("Podaj licznik i mianownik")
    a = int(input())
    b = int(input())
    dzielnik = NWD(a, b)

    if dzielnik == min(a, b):
        print("Skrocony ulamek to:", a / b)
    else:
        print("Skrocony ulamek to: ", a / dzielnik, "/", b / dzielnik)
