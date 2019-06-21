# -*- coding: utf-8 -*-
# W tych parszywych czasach niełatwo o godziwy zarobek dla wiedźmina. Geralt to twardy gość - z niejednego wychodka
# wodę spijał i w niejednym rowie spał. Problemy z potworami grasującymi po wsiach i lasach to jego specjalność.
# Każdy, nawet Geralt, potrzebuje jednak treningu.
# Sprawdź nowy program szkoleniowy Vesemira i przekonaj się, w jakiej formie jest Geralt - ilu potworom zdoła
# przetrzepać rzyć, zanim opadnie z sił.
#
# Niestety, może i wiedźmini są diabelnie skuteczni w walce, ale programiści z nich słabi. Poniższy program można
# napisać znacznie krócej. Spróbuj go zoptymalizować pod kątem:
# - podziału na funkcje
# - zastosowania list comprehensions
# - zastosowania wyrażeń warunkowych
# - operacji na napisach

import random
import sys

MONSTERS = ["Bandyta", "Utopiec", "Bruxa", "Ekimma", "Południca", "Golem", "Północnica", "Mglak"]
FAMILY = {"Bandyta": "Ludzie", "Utopiec": "Trupojady", "Bruxa": "Wampiry", "Ekimma": "Wampiry", "Południca": "Upiory",
          "Golem": "Magiczne",
          "Północnica": "Upiory", "Mglak": "Trupojady"}
SIGNS = {"Ludzie": "Aard", "Trupojady": "Igni", "Wampiry": "Igni", "Upiory": "Yrden", "Magiczne": "Quen"}

MAX_MONSTERS_NO = 20
MAX_HP = 100
MAX_SWALLOW_NO = 3


def life_checker(health, swallow_no):
    """Funkcja sprawdza czy wymagane i możliwe jest użycie eliksiru. Gdy użycie eliksiru nie jest możliwe, program
    kończy się"""

    if health < 0.3 * MAX_HP and swallow_no > 0:
        health = MAX_HP
        swallow_no -= 1
        print("Poziom życia krytyczny, wiedźmin pije Jaskółkę.")

    elif health < 0:
        print("Wiedźmin poległ w boju :(")
        sys.exit(0)


def fight_function(tier, health, swallows):
    """Funkcja przeprowadza walkę, która polega na odejmowaniu obrażeń określanych przez formułę: losowa liczba * 0.2 *
     maksymalne zdrowie i odejmuje te obrażenia od zdrowia i w razie spełnienia warunku odejmuje jeden eliksir z puli
     eliksirów. Jeżeli warunek zostanie spełniony,a nie będzie eliksirów walka kończy się przegraną. Walka jest
     prowadzona z potworami z podanego argumentu, który jest listą"""

    fight_string = "Wiedźmin walczy z potworem o nazwie {}, używając miecza {} i znaku {}"

    for m in tier:

        sign = SIGNS[FAMILY[m]]

        sword = "Stalowego" if FAMILY[m] == "Ludzie" else "Srebrnego"

        dmg = int(random.random() * 0.2 * MAX_HP)

        health -= dmg

        print(fight_string.format(m, sword, sign, str(dmg)))

        life_checker(health, swallows)


if __name__ == '__main__':

    # Tier 3 - losowe potwory z listy MONSTERS
    tier3 = [random.choice(MONSTERS) for i in range(MAX_MONSTERS_NO)]

    # Tier 2 - Wszystkie potwory z Tier 3 nie nalezace do kategori Magiczne i Wampiry
    tier2 = [monster for monster in tier3 if FAMILY[monster] != "Magiczne" and FAMILY[monster] != "Wampiry" ]

    # Tier 1 - Potwory z Tier 2 należące do kategorii "Ludzie" lub "Trupojady"
    tier1 = [monster for monster in tier2 if FAMILY[monster] == "Ludzie" or FAMILY[monster] == "Trupojady"]

    print("*** ETAP 1 ***")

    fight_function(tier1, 200, MAX_SWALLOW_NO)

    print("*** ETAP 2 ***")

    fight_function(tier2, 200, MAX_SWALLOW_NO)

    print("*** ETAP 3 ***")

    fight_function(tier3, 200, MAX_SWALLOW_NO)
