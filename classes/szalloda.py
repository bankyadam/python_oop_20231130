from classes.szoba import Szoba


class Szalloda:
    __szobak = []

    def __init__(self, nev):
        self.__nev = nev

    def get_nev(self):
        return self.__nev

    nev = property(get_nev)

    def uj_szoba(self, szoba: Szoba):
        self.__szobak.append(szoba)
