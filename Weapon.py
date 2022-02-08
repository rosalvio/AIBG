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


