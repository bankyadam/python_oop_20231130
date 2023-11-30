from classes.szoba import Szoba


class EgyagyasSzoba(Szoba):
    @property
    def ar(self):
        return 123.99

    @property
    def szobaszam(self):
        return 1
