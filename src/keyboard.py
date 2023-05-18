from src.item import Item

class TransMixin:

    language = 'EN'

    def __init__(self):
        self.language = self.language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'



class KeyBoard(Item, TransMixin):
    """Создаем новый класс KeyBoard"""
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)








