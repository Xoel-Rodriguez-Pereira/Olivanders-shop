import pytest
from src.logic import NormalItem

@pytest.mark.updateQuality
def test_normal_item_sell_in_positive():
    # quality should decrease by 1 when sell_in is >= 0
    item = NormalItem("foo", sell_in=5, quality=10)
    item.updateQuality()
    assert item.quality == 9

@pytest.mark.updateQuality
def test_normal_item_sell_in_negative():
    # quality should decrease by 2 when sell_in is < 0
    item = NormalItem("bar", sell_in=-1, quality=10)
    item.updateQuality()
    assert item.quality == 8

@pytest.mark.updateQuality
def test_quality_never_goes_below_zero_when_positive_sell_in():
    item = NormalItem("Normal", sell_in=5, quality=0)

    item.updateQuality()

    assert item.quality == 0

@pytest.mark.updateQuality
def test_quality_never_goes_below_zero():
    item = NormalItem("Normal", sell_in=-1, quality=0)

    item.updateQuality()

    assert item.quality == 0