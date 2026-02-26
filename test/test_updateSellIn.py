import pytest
from src.logic import *


@pytest.mark.updateSellIn

def test_normal_item_sell_in():
    # sell_in should decrease by 1
    item = NormalItem("foo", sell_in=5, quality=10)
    item.updateSellIn()
    assert item.getSellIn() == 4


@pytest.mark.updateSellIn

def test_conjured_item_sell_in():
    from src.logic import Conjured
    item = Conjured("Conjured Cake", sell_in=3, quality=10)
    item.updateSellIn()
    assert item.getSellIn() == 2


@pytest.mark.updateSellIn

def test_sulfuras_item_sell_in():
    from src.logic import Sulfuras
    item = Sulfuras("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    original = item.getSellIn()
    item.updateSellIn()
    assert item.getSellIn() == original


@pytest.mark.updateSellIn

def test_backstage_item_sell_in():
    from src.logic import Backstage
    item = Backstage("Backstage pass", sell_in=15, quality=20)
    item.updateSellIn()
    assert item.getSellIn() == 14


@pytest.mark.updateSellIn

def test_aged_brie_item_sell_in():
    from src.logic import AgedBrie
    item = AgedBrie("Aged Brie", sell_in=7, quality=10)
    item.updateSellIn()
    assert item.getSellIn() == 6
