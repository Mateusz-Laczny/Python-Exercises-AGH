# Polecenie:
#
# Skracanie ułamków tak przypadło Ci do gustu, że postanowiłeś/aś napisać program, który będzie przetwarzał setki,
# tysiące, a nawet miliony ułamków! Oczywiście ułamki nie będą podawane ręcznie -
# od teraz znajdują się pliku ulamki.txt
#
# a) 1pkt Zmodyfikuj odpowiednie funkcje programu tak, by ułamki nie były podawane przez użytkownika tylko wczytywane z
# pliku.
# Każda linia pliku reprezentuje jeden ułamek i jest zapisana w formacie "licznik mianownik".
# Skrócone ułamki powinny zostać zapisane w pliku tekstowym wyniki.txt
# b) 1pkt Dodaj obsługę błędów w programie. Zadbaj zarówno o sytuacje wyjątkowe przy operacjach na plikach, jak i o
# błędy danych

# import logging

# TEST
# divider = (euklides_algorithm(25, 5))
# print("Ułamek to ", int(25/divider), '/', int(5/divider))

# Pomocniczy logger
# logging.basicConfig(filename="C://Users//Mateusz//Desktop//Inne, Tymczasowe// logfile - Euklides.log",
#                   level=logging.DEBUG, filemode='w')
# logger = logging.getLogger()


def euklides_algorithm(numerator, denominator):
    """Funkcja oblicza NWD dwóch liczb - numerator(licznik) i denominator(mianownik)"""

    # logger.info("Funkcja zaczyna obliczać NWD")

    # Pętla oblicza NWD za pomocą metody z resztami z dzielenia
    while denominator != 0:
        reminder = numerator % denominator
        numerator = denominator
        denominator = reminder

    # logger.info("Funkcja 'while' zakończyła się")

    # TEST - print(numerator)

    # logger.info("Funkcja 'euklides kończy się i zwraca NWD")

    return numerator


# logger.info("Rozpoczyna się właściwy program, wczytywane są pliki")

# Program wczytuje plik z ułamkami
path_read = "C://Users//Mateusz//Desktop//Inne, Tymczasowe//ulamki.txt"
path_write = "C://Users//Mateusz//Desktop//Inne, Tymczasowe//wyniki.txt"

# logger.info("Pierwszy blok 'try' ")
try:
    open(path_read, 'r')

except FileNotFoundError:
    # logger.error("Błąd - plik nie istnieje")

    # Błąd - plik nie istnieje
    print("FileNotFoundError: O jejku jej! Taki plik nie istnieje!")
else:

    with open(path_read, 'r')as read_file:
        with open(path_write, 'w') as write_file:
            # Pętla przechodzi po liniach w pliku
            for line in read_file:
                # Rozdzielanie wczytanego stringa na licznik i mianownik
                splited_line = line.split()

                # logger.debug("Sprawdzanie czy występują błędy")

                # Sprawdzanie czy podany występują błędy
                try:
                    euklides_algorithm(int(splited_line[0]), int(splited_line[1]))
                except ValueError:
                    print("ValueError: O nie! Któraś z wartości w pliku nie jest liczbą!")

                else:
                    # logger.debug("Brak błędów")
                    # logger.info("Rozpoczyna się pętla 'for")

                    # Divider  = wynik funkcji "euklides"
                    divider = euklides_algorithm(int(splited_line[0]), int(splited_line[1]))

                    # logger.info("Funkcja 'euklides' została wywołana, rozpoczyna się blok 'if")

                    # Warunek sprawdza czy po skróceniu mianownik nie jest równy 1
                    if int(int(splited_line[1]) / divider) == 1:
                        # Obliczanie licznika
                        numenator_in_if = int(int(splited_line[0]) / divider)
                        # Konwersja na string
                        string_numerator = str(numenator_in_if)

                        # logger.info("Linia została zapisana do pliku")

                        # TEST - print(string_numerator)

                        # Zapisywanie wyniku do pliku
                        write_file.write(string_numerator)
                        write_file.write('\n')

                    else:
                        # logger.info("Zaczyna się pętla 'else'")

                        # logger.info("Obliczanie licznika i mianownika po skroceniu")

                        # Obliczanie licznika i mianownika
                        numenator_in_if = int(int(splited_line[0]) / divider)
                        denumerator_in_if = int(int(splited_line[1]) / divider)

                        # logger.info("Konwersja licznika i mianownika na stringi")

                        # Konwersja licznika i mianownika na format string
                        string_numerator = str(numenator_in_if)
                        string_denumerator = str(denumerator_in_if)
                        line_to_write = string_numerator + '/' + string_denumerator

                        # logger.info("Zapisywanie wyniku w pliku")

                        # TEST - print(line_to_write)

                        # Program zapisuje wynik do pliku
                        write_file.write(line_to_write)
                        write_file.write('\n')
