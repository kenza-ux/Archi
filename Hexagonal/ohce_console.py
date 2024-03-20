from OHCE_Archi.src.console_systeme import ConsoleSysteme
from OHCE_Archi.src.horloge_systeme import HorlogeSysteme
from OHCE_Archi.src.locale_systeme import LocaleSysteme


class OhceConsole:
    def __init__(self, horloge, locale, console):
        self.__horloge = horloge
        self.__locale = locale
        self.__console = console

    def inverser(self, string):
        return string[::-1]

    def print(self):
        est_soir = self.__horloge.est_soir()
        langue = self.__locale.choisir_langue()
        console = self.__console

        console.output(langue.saluer(est_soir))
        word = console.collect_input()
        reverse = self.inverser(word)
        console.output(reverse)

        est_palindrome = reverse == word

        if est_palindrome:
            console.output(langue.féliciter())

        console.output(langue.acquitter(est_soir))


if __name__ == '__main__':
    OhceConsole(HorlogeSysteme(), LocaleSysteme(), ConsoleSysteme()).print()