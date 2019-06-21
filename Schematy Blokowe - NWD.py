__author__ = 'student34'

liczba_a = int(input())
liczba_b = int(input())

while (liczba_a != liczba_b):

    if (liczba_a > liczba_b):
        liczba_a -= liczba_b

    elif (liczba_a < liczba_b):
        liczba_b -= liczba_a

print(liczba_a)
