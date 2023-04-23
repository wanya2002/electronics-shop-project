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




