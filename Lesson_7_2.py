from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fc_calc(self):
        pass


class Coat(Clothes):

    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, v):
        if v < 38:
            self._v = 38
        elif v > 70:
            self._v = 70
        else:
            self._v = v

    @property
    def fc_calc(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        if h < 148:
            self._h = 148
        elif h > 207:
            self._h = 207
        else:
            self._h = h

    @property
    def fc_calc(self):
        return self.h * 2 + 0.3


co1 = Coat('Оптимист', 35)
print(f'Для {co1.name},v= {co1.v} расход ткани на производство = {co1.fc_calc:.2f}')
co2 = Coat("Гигант", 90)
print(f'Для {co2.name},v= {co2.v} расход ткани на производство = {co2.fc_calc:.2f}')

su1 = Suit("веселенький", 176)
print(f'Для {su1.name},h= {su1.h} расход ткани на производство = {su1.fc_calc:.2f}')
su2 = Suit("клеш", 210)
print(f'Для {su2.name},h= {su2.h} расход ткани на производство = {su2.fc_calc:.2f}')
print(f'Общий расход ткани для всей обдежды ={(co1.fc_calc + co2.fc_calc + su1.fc_calc + su2.fc_calc):.2f}')
