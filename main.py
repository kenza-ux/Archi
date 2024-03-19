import datetime

class MirrorApp:
    def __init__(self):
        self.langue = 'français'  # Langue par défaut

    def dire_bonjour(self):
        heure = datetime.datetime.now().hour
        if 5 <= heure < 12:
            print(f'Bonjour! ({self.langue})')
        elif 12 <= heure < 18:
            print(f'Bonne après-midi! ({self.langue})')
        elif 18 <= heure < 22:
            print(f'Bonsoir! ({self.langue})')
        else:
            print(f'Bonne nuit! ({self.langue})')

    def dire_au_revoir(self):
        heure = datetime.datetime.now().hour
        if 5 <= heure < 12:
            print(f'Au revoir! ({self.langue})')
        elif 12 <= heure < 18:
            print(f'Au revoir! ({self.langue})')
        elif 18 <= heure < 22:
            print(f'Au revoir! ({self.langue})')
        else:
            print(f'Bonne nuit! ({self.langue})')

    def verifier_palindrome(self, texte):
        texte = texte.lower().replace(" ", "")
        if texte == texte[::-1]:
            print("Bien dit !")
            return True
        return False

    def lancer(self):
        self.dire_bonjour()
        while True:
            entree = input("Entrez du texte (ou 'quitter' pour arrêter): ")
            if entree.lower() == 'quitter':
                break
            if self.verifier_palindrome(entree):
                continue
            print(entree[::-1])
        self.dire_au_revoir()


if __name__ == "__main__":
    app = MirrorApp()
    app.lancer()
