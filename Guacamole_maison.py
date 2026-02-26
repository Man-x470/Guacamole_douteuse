class Température:
    def __init__(self, lieu, température, humidité, pression, vent, conseil):
        self.lieu = lieu
        self.température = température
        self.humidité = humidité
        self.pression = pression
        self.vent = vent 
        self.conseil = conseil 

    def Il_fait_combien(self):
        print("À " + self.lieu + ",")
        print("Il fait " + self.température)
        print("Le taux d'humidité est de " + self.température)
        print("La pression atmosphèrique est de " + self.pression)
        print("Les vents vont à " + self.vent)
        print(self.conseil)
        print("-")

température_sherbrooke = Température("Sherbrooke","-4°C","58%", "100.9Kpa", "26Km/h", "Mettez une p'tit laine")
température_sherbrooke.Il_fait_combien()  

température_montréal = Température("Montréal", "-5°C", "68%", "101,1Kpa","26Km/h", "Déneigez vos voiture")
température_montréal.Il_fait_combien()
