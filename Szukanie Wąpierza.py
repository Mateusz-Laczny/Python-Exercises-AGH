# -*- coding: utf-8 -*-

# Znany Rivijski wiedźmak Gewralt wędruje po Królestwach Północy, w poszukiwaniu wampira wyższego
# Nosferata. Dostal cynk, ze w pewnej wiosce pod Wyzimą ukrywa się stwór. Niestety na
# wieśniaków rzucony został urok i nie mogą oni mówić, ani bezpośrednio wskazać plugawca, więc Gewralt słusznie założył
# że wszyscy będą wiedzieć jak wygląda wampir, on natomiast jako aspołeczna szkarada nie będzie znał nikogo.
# Dlatego wiedźmak postanowił zadać każdej osobie w wiosce pytanie "Witaj poczcziwy człowieku! Czy znasz może tamtą osobę?
# i ruszył na poszukiwania wąpierza
#
# Wskazówka 1: funkcja do_you_know(a, b) zawsze pozwala wyeliminować jedną z osób z pary
# jako potencjalnego Nosferata.
# Wskazówka 2: Dla zbioru złożonego z N osób, potrzebnych jest tylko N-1 wywołań funkcji do_you_know.
#
# a) Narysuj schemat blokowy z rozwiązaniem problemu (pamiętaj żeby uwzględnić przygotowane poniżej funkcje!)
# b) Napisz program na podstawie schematu

# UWAGA - czesc zmiennych i funkcji w tym module zaczyna się od "_" - to znaczy, ze nie wolno ich uzywac! ;]


import itertools
import random

_ORDINARY_PEOPLE = [
    "Bogusz Bartłomiej",
    "Chmielowiec Adrian",
    "Cyganek Gabriel",
    "Dziadoń Maks",
    "Fijałkowski Paweł",
    "Filipiak Michał",
    "Janus Mateusz",
    "Kamiński Filip",
    "Kisielewska Gabrysia",
    "Klimek Joanna",
    "Kmiecik Jakub",
    "Magnes Agnes",
    "Novak Ola",
    "Pasek Wiktoria",
    "Pomarański Marcin",
    "Pytlik Arek",
    "Radzik Andrzej",
    "Siekierzyński Krzysztof",
    "Tluszcz Filip",
    "Wolak Bartosz",
    "Węgrzyn Karolina",
    "Węgrzyn Piotr",
    "Łączny Mateusz"
]
_NOSFERAT = "Daroxis"


_ALL_PAIRS = [(x, y) for x, y in itertools.product(_ORDINARY_PEOPLE, _ORDINARY_PEOPLE) if x != y]
_KNOWS = []
for pair in _ALL_PAIRS:
    if random.random() > 0.5:
        _KNOWS.append(pair)
for name in _ORDINARY_PEOPLE:
    _KNOWS.append((name, _NOSFERAT))

_ORDINARY_PEOPLE.insert(3, _NOSFERAT)
PERSONS = _ORDINARY_PEOPLE


# funckcja sprawdzajaca czy dana osoba zna inna osobe
def do_you_know(asked_person, target_person):
    return (asked_person, target_person) in _KNOWS


# funkcja pozwalajaca na przeprowadzenie wywiadu
def interview(person):
    if person == _NOSFERAT:
        print("Wiedżmak znalazł bestię i dostał od Foltesta sakwę pełną orenów!")
    else:
        print("Zaraza! Głupi wiedźmak zasiekł prostego chłopa i musiał uciekać do Keadwen!")


if __name__ == '__main__':

    for iterator in range(0, len(PERSONS) - 1):

        # Warunek sprawdza eliminuje jedną osobę z pary jako potencjalnego Wąpierza
        if do_you_know(PERSONS[0], PERSONS[1]) is True:

            # Warunek jest prawdziwy, usuwana jest pierwsza osoba, bo Wąpierz nie zna nikogo
            del PERSONS[0]
            print("Za stary na to jestem...")
        else:

            # Warunek jest fałszywy, usuwana jest druga osoba, bo wszyscu wiedzą jak wygląda Wąpierz
            del PERSONS[1]
            print("Zaraza!")

    vampyr = PERSONS[0]
    interview(vampyr)
