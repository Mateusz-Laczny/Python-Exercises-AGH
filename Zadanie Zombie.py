# -*- coding: utf-8 -*-

import random

# Program generuje (losową) apokalipsę zombie.
# Z grupy ludzi (lista people) wybierane są 3 losowe osoby, które zostają zarażone (funkcja generate_apocalypse).
# Aby przeciwdziałać zagładzie, program stara się znaleźć zarażone osoby (funkcja find_zombies).
# Następnie znalezione zombie zostają usunięte (funkcja kill_zombies).
#
# Rozpoznanie zarażonych to nie taka prosta sprawa. Musisz napisać brakujący fragment programu, żeby ocalić świat.
# Uważaj, żeby nie wypuścić żadnego zombie ani nie skrzywdzić zdrowych ludzi!


def generate_apocalypse(people):
    zombies = random.sample(people, 3)
    zombies_dict = {}
    for p in people:
        if p in zombies:
            zombies_dict[p] = True
        else:
            zombies_dict[p] = False
    return zombies_dict


def find_zombies(people, zombies_dict):
    zombies = []
    for x in people:
        if zombies_dict[x]:
            zombies.append(x)
    return zombies


def kill_zombies(zombies, zombies_dict):
    for z in zombies:
        if zombies_dict[z]:
            print("Good job, you have killed a zombie! : " + z)
            del zombies_dict[z]
        else:
            print("Oh no, you have killed a normal person! : " + z)

    for p in zombies_dict:
        if zombies_dict[p]:
            print("Some zombies are still alive. ZOMBIE APOCALYPSE!")
            return

    print("Congratulations, you saved the world!" '\n' "For the third time..."
          '\n' "... if you know what i mean" )


if __name__ == '__main__':
    people = ["Rick", "Carl", "Daryl", "Glenn", "Maggie", "Andrea", "Michonne"]

    zombies_dict = generate_apocalypse(people)
    zombies_to_kill = find_zombies(people, zombies_dict)

    kill_zombies(zombies_to_kill, zombies_dict)
