import csv

class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = 'Файл item.csv поврежден_'

    def __str__(self):
        return self.message


class Item(InstantiateCSVError):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return other.quantity + self.quantity




    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
       if len(name) > 10:
            raise Exception('Длина товара превышает 10 символов')
       self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        try:
           with open ('..\src\items.csv', newline='') as csvfile:
               reader = csv.DictReader(csvfile)
               for row in reader:
                   try:
                      if len(row) < 3:
                          raise InstantiateCSVError
                      else:
                          cls.all.append(cls(row['name'], row['price'], row['quantity']))
                   except InstantiateCSVError:
                       print('Файл item.csv поврежден_')
                       quit()
           return cls.all
        except FileNotFoundError:
            print('FileNotFoundError: Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(str):
        return int(float(str))



Item.instantiate_from_csv()





