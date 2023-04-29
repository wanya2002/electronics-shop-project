"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

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



