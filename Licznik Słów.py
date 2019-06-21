import re
from collections import OrderedDict
from operator import itemgetter


def word_searcher(text):
    """Funkcja wyszukuje słowa w danym pliku tekstowym"""

    # Słownik do zapisywania słów
    word_dict = {}

    # Wzór do szukania słów
    pattern = re.compile(r'[a-żA-Ż]\S+[a-żA-Ż]')
    # Wyszukiwanie słów według wzoru
    matches = pattern.finditer(text)

    for match in matches:
        match_to_set = match.group(0)

        # Jeżeli słowa nie ma w słowniku, zostaje dodane do słownika
        if match_to_set not in word_dict:
            word_dict[match_to_set] = 1

        else:
            word_dict[match_to_set] += 1

    return word_dict


def word_ranking_saver(dictionary):
    """Funkcja liczy słowa w słowniku i zapisuje w pliku 50 największych wartości"""

    with open("C://Users//Mateusz//Desktop//Inne, Tymczasowe//Potop - ranking.txt", 'w') as write_file:
        # Słownik zostaje posortowany
        sorted_dict = OrderedDict(sorted(dictionary.items(), key=itemgetter(1)), reverse=True)

        counter = 0

        for value in reversed(sorted_dict):

            # Blok wykonuje się dopóki nie wypisane zostało więcej niż 50 linijek
            if counter <= 50:

                # Konwersja liczby pojawień się na string
                text_to_write = str(sorted_dict[value])

                line_to_write = value + ' - ' + text_to_write + '\n'

                # Zapisywanie wartości w pliku Potop - ranking
                write_file.write(line_to_write)

                counter += 1
            else:
                break


file_path = "C://Users//Mateusz//Desktop//Inne, Tymczasowe//potop.txt"

# word_searcher(file_path)

# Warunek sprawdza czy podany plik istnieje
try:
    open(file_path)

    # Brak błędów - rozpoczyna się właściwy program
    with open(file_path, 'r') as read_file:

        # Read czyta podany plik
        read_text = read_file.read()

        # Funkcja word_searcher zostaje wywołana, znajduje ona słowa w tekście
        # i liczy je
        matching_words = word_searcher(read_text)

        # Dictionary_with_words to słownik ze słowami i ilością ich wystąpień
        dictionary_with_words = matching_words

        # Wywoływana jest funkcja word_ranking_saver
        word_ranking_saver(dictionary_with_words)

except FileNotFoundError as err:

    # Błąd - plik nie istnieje
    print(err)



