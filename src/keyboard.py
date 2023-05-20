from src.item import Item

class TransMixin:

    __language = 'EN'

    def __init__(self):
        self.__language = self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language



class KeyBoard(Item, TransMixin):
    """Создаем новый класс KeyBoard"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)











