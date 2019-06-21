# Polecenie:
#
# Po raz kolejny musisz wyręczyć administratora na uczelni i zająć się generowaniem maili z imion i nazwisk studentów.
# Tym razem jednak zmieniono nieco reguły tworzenia loginów.
# Każdy login składa się pierwszego znaku imienia, kropki oraz pełnego nazwiska (małymi literami). Dodatkowo,
# jeśli imię kończy się na "a", adres powinien zostać założony w domenie "@studentka.agh.edu.pl".
# W przeciwnym przypadku domena to "@student.agh.edu.pl".
#
# Ponieważ uczelnia przyjęła wyjątkowo dużo studentów, niektórzy z nich mają te same nazwiska i pierwsze litery imion.
# Twój program powinien obsługiwać takie sytuacje i generować unikalny login w przypadku napotkania duplikatu.
# Unikalny login powstaje przez doklejenie do zwykłego loginu kolejnego, wolnego numeru.
#
# Przykłady:
# "Piotr Budynek" -> "p.budynek@student.agh.edu.pl"
# "Anna Fontanna" -> "a.fontanna@studentka.agh.edu.pl"
# "Przemysław Budynek" -> "p.budynek1@student.agh.edu.pl"
# "Paweł Budynek" -> "p.budynek2@student.agh.edu.pl"
#
# Na potrzeby testów możesz wykorzystać poniższą listę:
# STUDENTS = "Piotr Budynek", "Anna Fontanna", "Przemysław Budynek", "Paweł Budynek", "Anna Manna", "Joanna Fontanna", \
#            "Anastazja Fontanna"


def generuj_login(x):
    x = x.lower()
    x = x.split()
    log = x[0][0] + "." + x[1]
    return log


def generuj_mail(y):
    if y[0] == "a":
        adres = y + "@studentka.agh.edu.pl"
    else:
        adres = y + "@student.agh.edu.pl"
    return adres


if __name__ == '__main__':
    i = 0
    list = ["Piotr Budynek", "Anna Fontanna", "Przemyslaw Budynek", "Pawel Budynek", "Anna Manna", "Joanna Fontanna",
         "Anastazja Fontanna"]
    licznik = {}

    while i < len(list):
        s = list[i]
        login = generuj_login(s)

        if login in licznik:
            licznik[login] += 1
            login += str(licznik[login])
        else:
            licznik[login] = 1

        mail = generuj_mail(login)
        print(mail)

        i += 1
