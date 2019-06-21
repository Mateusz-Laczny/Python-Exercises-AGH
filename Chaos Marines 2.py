# -*- coding: utf-8 -*-
# Stworzone archiwum jest kompaktowe, ale wymaga wygodnego mechanizmu korzystania z niego
# by móc z łatwością śledzić plugawe sługi chaosu. Musisz przygotować jeszcze procedurę
# pozyskiwania z niego informacji.
#
# Przygotuj odwrotny program. Powinien otwierać plik gz i zapisywać rozpakowaną zawartość.

import gzip


if __name__ == '__main__':

    # Ścieżki do plików
    file_path = "C://Users//Mateusz//Desktop//compressed_battle_report.gz"
    file_path_2 = "C://Users//Mateusz//Desktop//uncompressed_battle_report.bmp"

    # Obsługa błędów
    try:

        # Otwarty zostaje skompresowany plik
        with gzip.open(file_path, 'rb') as read_file:

            # Stworzony zostaje plik, w którym zapisana zostanie
            # rozpakowana zawartość
            with open(file_path_2, 'wb') as save_file:

                # Wczytanie zawartości skompresowanego pliku
                file_content = read_file.read()

                # Zapisanie zawartości do pliku
                save_file.write(file_content)

    # Błąd - plik nie istnieje
    except FileNotFoundError as err:
        print(err)
