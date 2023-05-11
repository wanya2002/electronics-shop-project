from src.item import Item

class Phone(Item):
    """новый класс Phone"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__name = name
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if type(number) == int and number > 0:
           self.__number_of_sim = number
        else:
            raise Exception('Число должно быть целым и больше ноля')










