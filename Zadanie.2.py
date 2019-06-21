# -*- coding: utf-8 -*-

# Jesteś administratorem na Katedrze Informatyki AGH i właśnie dostałeś listę nowych studentów.
# Musisz założyć im konta pocztowe, ale oczywiście jako admin nigdy nie masz czasu,
# a już na pewno nie na ręczne generowanie loginów. Dlatego będziesz potrzebował programu, który dla każdego
# imienia i nazwiska studenta wypisze proponowany adres mailowy, na który składać się będą: pierwsze 2 litery imienia,
# pierwsze 3 litery nazwiska oraz adres student.agh.edu.pl.
# Np. dla nazwiska "Budynek Piotr" program powinien wypisać "pibud@student.agh.edu.pl".
#
# Pamiętaj że:
# - dostajesz tekst w formacie "Nazwisko Imię", bez podziału na wyrazy
# - w adresach mailowych nie ma dużych liter
# 
# (*) Zadanie dodatkowe (1pkt):  uwzględnij także konwersję polskich znaków, np. "ó" -> "o", "ł" -> "l".


USERS = [
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

if __name__ == '__main__':

    IMIONA_I_NAZWISKA = []

    adres = "@student.agh.edu.pl"

    for user in USERS:
        user = user.lower()\
         .replace("ń", "n")\
         .replace("ę", "e")\
         .replace("ł", "l")\
         .replace("ą", "a")\
         .split()
        IMIONA_I_NAZWISKA.append(user)

    for x in range(len(IMIONA_I_NAZWISKA)):
        login = IMIONA_I_NAZWISKA[x][1][:2] + IMIONA_I_NAZWISKA[x][0][:3] + adres

        print(login, "\n")

