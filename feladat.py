from abc import ABC, abstractmethod


class Szoba(ABC):
    @property
    @abstractmethod
    def ar(self) -> float:
        pass

    @property
    @abstractmethod
    def szobaszam(self) -> int:
        pass


class EgyagyasSzoba(Szoba):
    def ar(self):
        return 123.99

    def szobaszam(self):
        return 1


class KetagyasSzoba(Szoba):
    def ar(self):
        return 210.99

    def szobaszam(self):
        return 2


class Szalloda:
    __szobak = []

    def __init(self, nev):
        self.__nev = nev

    def get_nev(self):
        return self.__nev

    nev = property(get_nev)

    def add_szoba(self, szoba):
        self.__szobak.append(szoba)


class Foglalas:
    def __init__(self, szalloda, szoba, datum):
        self.szalloda = szalloda
        self.szoba = szoba
        self.datum = datum

    def ar(self):
        return self.__szoba.ar


class Foglalasok:
    __foglalasok = []

    def foglalas(self, foglalas):
        self.__foglalasok.append(foglalas)
        return foglalas.ar()

    def lemondas(self, szalloda, szoba, datum):
        for i in self.__foglalasok:
            foglalas = self.__foglalasok[i]
            if foglalas.szalloda == szalloda and foglalas.szoba == szoba and foglalas.datum == datum:
                self.__foglalasok.remove(i)
                return

