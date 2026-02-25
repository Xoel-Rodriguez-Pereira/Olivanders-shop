import pytest
from src.logic import *


@pytest.mark.updateQualityNormalItem

def test_normal_item_sell_in_positive():
    # quality should decrease by 1 when sell_in is >= 0
    item = NormalItem("foo", sell_in=5, quality=10)
    item.updateQuality()
    assert item.quality == 9


@pytest.mark.updateQualityNormalItem

def test_normal_item_sell_in_negative():
    # quality should decrease by 2 when sell_in is < 0
    item = NormalItem("bar", sell_in=-1, quality=10)
    item.updateQuality()
    assert item.quality == 8


@pytest.mark.updateQualityNormalItem

def test_quality_never_goes_below_zero_when_positive_sell_in():
    item = NormalItem("Normal", sell_in=5, quality=0)

    item.updateQuality()

    assert item.quality == 0


@pytest.mark.updateQualityNormalItem

def test_quality_never_goes_below_zero():
    item = NormalItem("Normal", sell_in=-1, quality=0)

    item.updateQuality()

    assert item.quality == 0


@pytest.mark.updateQualitySulfuras

def test_sulfuras_quality_constant():
    # quality should remain constant (always 80) regardless of sell_in or initial quality
    item = Sulfuras("Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
    original_quality = item.quality

    item.updateQuality()

    assert item.quality == original_quality

    
@pytest.mark.updateQualityAgedBrie

def test_aged_brie_sell_in_positive():
    # quality should increase by 1 when sell_in is >= 0
    item = AgedBrie("Aged Brie", sell_in=5, quality=10)

    item.updateQuality()

    assert item.quality == 11


@pytest.mark.updateQualityAgedBrie

def test_aged_brie_sell_in_negative():
    # quality should increase by 2 when sell_in is < 0
    item = AgedBrie("Aged Brie", sell_in=-1, quality=10)

    item.updateQuality()

    assert item.quality == 12


@pytest.mark.updateQualityConjured

def test_conjured_sell_in_positive():
    # quality should decrease by 2 when sell_in is >= 0 (double normal rate)
    item = Conjured("Conjured Mana Cake", sell_in=5, quality=10)

    item.updateQuality()

    assert item.quality == 8


@pytest.mark.updateQualityConjured

def test_conjured_sell_in_negative():
    # quality should decrease by 4 when sell_in is < 0 (double normal rate after expiration)
    item = Conjured("Conjured Mana Cake", sell_in=-1, quality=10)

    item.updateQuality()

    assert item.quality == 6


@pytest.mark.updateQualityConjured

def test_conjured_quality_never_goes_below_zero_positive_sell_in():
    item = Conjured("Conjured", sell_in=5, quality=1)

    item.updateQuality()

    assert item.quality == 0


@pytest.mark.updateQualityConjured

def test_conjured_quality_never_goes_below_zero():
    item = Conjured("Conjured", sell_in=-1, quality=1)

    item.updateQuality()

    assert item.quality == 0


@pytest.mark.updateQualityBackstage

def test_backstage_sell_in_above_ten():
    # quality should increase by 1 when sell_in > 10
    item = Backstage("Backstage pass", sell_in=11, quality=10)

    item.updateQuality()

    assert item.quality == 11


@pytest.mark.updateQualityBackstage

def test_backstage_sell_in_between_five_and_ten():
    # quality should increase by 2 when 5 < sell_in <= 10
    item = Backstage("Backstage pass", sell_in=10, quality=10)

    item.updateQuality()

    assert item.quality == 12


@pytest.mark.updateQualityBackstage

def test_backstage_sell_in_between_zero_and_five():
    # quality should increase by 3 when 0 < sell_in <= 5
    item = Backstage("Backstage pass", sell_in=5, quality=10)

    item.updateQuality()

    assert item.quality == 13


@pytest.mark.updateQualityBackstage

def test_backstage_sell_in_zero_or_negative():
    # quality should drop to 0 when sell_in <= 0
    item = Backstage("Backstage pass", sell_in=0, quality=10)

    item.updateQuality()

    assert item.quality == 0


