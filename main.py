import datetime

class MirrorApp:
    def __init__(self):
        self.langue = 'français'  # Langue par défaut

    def _afficher_message(self, message):
        print(f'{message} ({self.langue})')

    def _salutation_selon_heure(self, matin, apres_midi, soir, nuit):
        heure = datetime.datetime.now().hour
        if 5 <= heure < 12:
            self._afficher_message(matin)
        elif 12 <= heure < 18:
            self._afficher_message(apres_midi)
        elif 18 <= heure < 22:
            self._afficher_message(soir)
        else:
            self._afficher_message(nuit)

    def dire_bonjour(self):
        self._salutation_selon_heure("Bonjour!", "Bonne après-midi!", "Bonsoir!", "Bonne nuit!")

    def dire_au_revoir(self):
        self._salutation_selon_heure("Au revoir!", "Au revoir!", "Au revoir!", "Bonne nuit!")

    def verifier_palindrome(self, texte):
        texte = texte.lower().replace(" ", "")
        if texte == texte[::-1]:
            self._afficher_message("Bien dit !")
            return True
        return False

    def lire_entree(self):
        entree = input("Entrez du texte (ou 'quitter' pour arrêter): ")
        return entree.lower()

    def afficher_inverse(self, texte):
        self._afficher_message(texte[::-1])

    def lancer(self):
        self.dire_bonjour()
        while True:
            entree = self.lire_entree()
            if entree == 'quitter':
                break
            if not self.verifier_palindrome(entree):
                self.afficher_inverse(entree)
        self.dire_au_revoir()


if __name__ == "__main__":
    app = MirrorApp()
    app.lancer()