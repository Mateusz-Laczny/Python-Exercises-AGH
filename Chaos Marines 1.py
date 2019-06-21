# -*- coding: utf-8 -*-
# Do Inkwizycji wpłynął raport z sektora Calixis, zawierający wysokiej jakości zdjęcie przedstawiające
# wrogie operacje w regionie. Jednakże obrazy tego rozmiaru są zbyt duże nawet dla przepastnych archiwów
# Ordo Hereticus. Twoim obowiązkiem jako młodego skryby jest przygotowanie procedury, która skompresuje
# otrzymaną fotografię przed jej skatalogowaniem.
#
# Użyj modułu gzip. Skompresuj załączony plik do nowego z rozszerzeniem gz. Sprawdź o ile mniejszył się
# jego rozmiar. Spróbuj go rozpakować zewnętrznym programem i zweryfikuj, że zawartość jest poprawna.

import gzip
import shutil


def file_compresor(filepath_in, filepath_out):
    """Funkcja czyta plik i tworzy jego skompresowaną wersję"""

    try:
        with open(filepath_in, 'rb') as in_file:

            with open(filepath_out, 'wb') as out_file:

                shutil.copyfileobj(in_file, out_file)

    except ValueError as err1:
        print(err1)

    except FileNotFoundError as err2:
        print(err2)


if __name__ == '__main__':

    filepath_1 = "C://Users//Mateusz//Desktop//Inne, Tymczasowe//battle_report.bmp"
    filepath_2 = "C://Users//Mateusz//Desktop//Inne, Tymczasowe//Compressed_battle_report.gz"

    file_compresor(filepath_1, filepath_2)
