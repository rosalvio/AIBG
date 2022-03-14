from abc import ABC, abstractmethod


class Weapon(ABC):

    @property
    @abstractmethod
    def name(self):
        '''
        :return: Nombre del arma.
        '''
        pass

    @property
    @abstractmethod
    def ammo(self):
        '''
        :return: Cantidad de disparos restantes en el arma.
        '''
        pass

    @property
    @abstractmethod
    def range(self):
        '''
        :return: Distancia euclidea a la que el arma puede hacer danyo.
        '''
        pass

    # TODO Anyadir peso del arma


class Sniper(Weapon):
    AMMO = 10
    RANGE = 50

    def __init__(self):
        self._name = "Sniper"
        self._ammo = self.AMMO
        self._range = self.RANGE

    def name(self):
        return self._name

    def ammo(self):
        return self._ammo

    def range(self):
        return self._range


weapons = {'Sniper': Sniper()}
