from abc import ABC, abstractmethod


class Clothes(ABC):

        @abstractmethod
        def calc_cons(self):
            pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calc_cons(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calc_cons(self):
        return 2 * self.h + 0.3


my_coat = Coat(6.5)
my_suit = Suit(2)

print(my_coat.calc_cons)
print(my_suit.calc_cons)
