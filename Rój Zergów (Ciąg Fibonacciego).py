if __name__ == '__main__':
    ciag = []

    print ("Podaj liczbę")

    liczba = int(input())

    for x in range (1,liczba + 1):
        if x == 1 or x == 2:
            ciag.append(1)
        else:
            ciag.append(ciag[x-3] + ciag[x-2])

    print(ciag[liczba - 1])
