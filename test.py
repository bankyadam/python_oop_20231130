import unittest

from datetime import date
from classes.egyagyasszoba import EgyagyasSzoba
from classes.szalloda import Szalloda

from classes.foglalaskezelo import Foglalaskezelo


class TestFoglalas(unittest.TestCase):
    def setUp(self):
        self.szalloda = Szalloda("Hotel Imerial")
        self.szoba = EgyagyasSzoba()
        self.szalloda.uj_szoba(self.szoba)
        self.foglalaskezelo = Foglalaskezelo()

    def test_foglalas_sikeres(self):
        self.assertEqual(
            123.99,
            self.foglalaskezelo.foglalas(self.szalloda, self.szoba, date(2024, 12, 6))
        )
        # A FOGLALASOK KEZELESE / ELOFELTOLTES

    def test_foglalas_multbeli_datum(self):
        with self.assertRaises(Exception) as context:
            self.foglalaskezelo.foglalas(self.szalloda, self.szoba, date(2020, 12, 6))

        self.assertTrue('Csak jovobeni datumra lehet foglalni' in str(context.exception))

    def test_foglalas_foglalt_adott_datumon(self):
        self.foglalaskezelo.foglalas(self.szalloda, self.szoba, date(2023, 12, 6))

        with self.assertRaises(Exception) as context:
            self.foglalaskezelo.foglalas(self.szalloda, self.szoba, date(2023, 12, 6))

        self.assertTrue('Ezt a szobat mar lefoglaltak erre a datumra' in str(context.exception))

    def test_lemondas_sikeres(self):
        self.foglalaskezelo.foglalas(self.szalloda, self.szoba, date(2023, 12, 6))
        self.foglalaskezelo.lemondas(self.szalloda, self.szoba, date(2023, 12, 6))

    def test_lemondas_nem_letezik(self):
        with self.assertRaises(Exception) as context:
            self.foglalaskezelo.lemondas(self.szalloda, self.szoba, date(2023, 12, 6))

        self.assertTrue('Nincs ilyen foglalas' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
