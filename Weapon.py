from abc import ABC, abstractmethod


class Weapon(ABC):

    @property
    @abstractmethod
    def damage(self):
        '''
        :return: Danyo por disparo del arma.
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


    @property
    @abstractmethod
    def wielding(self):
        '''
        Usar armas a una mano reduce la precision
        :return: Si se necesitan una o dos manos para usar el arma.
        '''
        pass