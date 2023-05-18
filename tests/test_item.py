"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard

def test_calculate_total_price():
      item = Item('samsung', 450, 14)
      assert item.calculate_total_price() == 6300

def test_apply_discount():
      item = Item('nokia', 875, 5)
      Item.pay_rate = 0.6
      item.apply_discount()
      assert item.price == 525

def test_name():
      item1 = Item('readmi', 879, 8)
      item1.name = 'apple'
      assert item1.name == 'apple'

def test_instantiate_from_csv():
      Item.instantiate_from_csv()
      assert len(Item.all) == 5

def test_string_to_number():
      assert Item.string_to_number('5') == 5
      assert Item.string_to_number('5.0') == 5
      assert Item.string_to_number('5.5') == 5

def test_repr():
      item1 = Item("Смартфон", 10000, 20)
      assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
      item1 = Item("Смартфон", 10000, 20)
      assert str(item1) == 'Смартфон'

def test_str_phone():
      phone1 = Phone("iPhone 14", 120000, 5, 2)
      assert str(phone1) == 'iPhone 14'

def test_repr_phone():
      phone1 = Phone("iPhone 14", 120000, 5, 2)
      assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_init_phone():
      phone1 = Phone("iPhone 14", 120000, 5, 2)
      assert phone1.number_of_sim == 2

def test_add():
      phone1 = Phone("iPhone 14", 120000, 5, 2)
      item1 = Item("Смартфон", 10000, 20)
      assert item1 + phone1 == 25
      assert phone1 + phone1 == 10
      assert phone1 + item1 == 25
      assert item1 + item1 == 40


def test_KeyBoard():
      kb = KeyBoard('Dark Project KD87A', 9600, 5)
      assert str(kb) == "Dark Project KD87A"

def test_KeyBoard_TransMixin():
      kb = KeyBoard('Dark Project KD87A', 9600, 5)
      assert str(kb.language) == "EN"

def test_KeyBoard_change_lang():
      kb = KeyBoard('Dark Project KD87A', 9600, 5)
      kb.change_lang()
      assert str(kb.language) == "RU"





