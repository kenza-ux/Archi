import locale

from langue_anglaise import LangueAnglaise
from langue_francaise import LangueFrançaise


class LocaleSysteme:
    def recuperer_code_langue(self):
        lang, _ = locale.getlocale()
        return lang.split("_")[0]

    def choisir_langue(self):
        code_langue = self.recuperer_code_langue()
        return LangueFrançaise() if code_langue == 'fr' else LangueAnglaise()