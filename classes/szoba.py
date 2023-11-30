from abc import ABC, abstractmethod


class Szoba(ABC):
    @property
    @abstractmethod
    def ar(self):
        pass

    @property
    @abstractmethod
    def szobaszam(self):
        pass
