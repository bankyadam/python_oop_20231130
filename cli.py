from datetime import date
from classes.egyagyasszoba import EgyagyasSzoba
from classes.ketagyasszoba import KetagyasSzoba
from classes.szalloda import Szalloda

from classes.foglalaskezelo import Foglalaskezelo


szalloda = Szalloda("Hotel Imerial")
egyagyasszoba1 = EgyagyasSzoba()
szalloda.uj_szoba(egyagyasszoba1)
egyagyasszoba2 = EgyagyasSzoba()
szalloda.uj_szoba(egyagyasszoba2)
ketagyasszoba = KetagyasSzoba()
szalloda.uj_szoba(ketagyasszoba)
foglalaskezelo = Foglalaskezelo()

print("A foglalas ara: ", foglalaskezelo.foglalas(szalloda, egyagyasszoba1, date(2023, 12, 28)))
print("A foglalas ara: ", foglalaskezelo.foglalas(szalloda, ketagyasszoba, date(2023, 12, 30)))
print("A foglalas ara: ", foglalaskezelo.foglalas(szalloda, ketagyasszoba, date(2023, 12, 6)))
print("A foglalas ara: ", foglalaskezelo.foglalas(szalloda, egyagyasszoba1, date(2024, 1, 8)))
print("A foglalas ara: ", foglalaskezelo.foglalas(szalloda, egyagyasszoba2, date(2024, 1, 28)))


foglalaskezelo.listazas()
