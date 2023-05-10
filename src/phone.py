

class Phone:
    """новый класс Phone"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__number_of_sim = number_of_sim

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if type(number) == int and number > 0:
           self.__number_of_sim = number
        else:
            raise Exception('Число должно быть целым и больше ноля')













