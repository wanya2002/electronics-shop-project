

class Phone:
    """новый класс Phone"""
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

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







