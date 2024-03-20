from datetime import datetime


class HorlogeSysteme:
    def recuperer_heure(self):
        return int(datetime.now().strftime("%H"))

    def est_soir(self):
        heure = self.recuperer_heure()
        return heure >= 18 or heure < 7