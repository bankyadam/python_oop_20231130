from datetime import date
from classes.szoba import Szoba
from classes.szalloda import Szalloda
from classes.foglalas import Foglalas


class Foglalaskezelo:
    __foglalasok = []

    def foglalas(self, szalloda: Szalloda, szoba: Szoba, datum: date):
        if self.keres_foglalas(szalloda, szoba, datum):
            raise Exception("Ezt a szobat mar lefoglaltak erre a datumra")

        if datum <= date.today():
            raise Exception("Csak jovobeni datumra lehet foglalni")


        foglalas = Foglalas(szalloda, szoba, datum)
        self.__foglalasok.append(foglalas)
        return foglalas.ar()

    def lemondas(self, szalloda: Szalloda, szoba: Szoba, datum: date):
        foglalas = self.keres_foglalas(szalloda, szoba, datum)
        if foglalas:
            self.__foglalasok.remove(foglalas)
        else:
            raise Exception("Nincs ilyen foglalas")

    def keres_foglalas(self, szalloda: Szalloda, szoba: Szoba, datum: date):
        for foglalas in self.__foglalasok:
            if foglalas.szalloda == szalloda and foglalas.szoba == szoba and foglalas.datum == datum:
                return foglalas

    def listazas(self):
        for f in self.__foglalasok:
            print("Szalloda: ", f.szalloda.nev, " Szobaszam: ", f.szoba.szobaszam, " ara ", f.szoba.ar, " Datum: ", f.datum)
