import pytest
from src.logic import NormalItem, Conjured, Sulfuras, AgedBrie, Backstage


@pytest.mark.updateState

def test_normal_item_update_state():
    item = NormalItem("foo", sell_in=5, quality=10)
    item.updateState()

    assert item.getSellIn() == 4
    assert item.getQuality() == 9


@pytest.mark.updateState

def test_conjured_item_update_state():
    item = Conjured("Conjured Cake", sell_in=3, quality=10)
    item.updateState()

    assert item.getSellIn() == 2
    assert item.getQuality() == 8


@pytest.mark.updateState

def test_sulfuras_item_update_state():
    item = Sulfuras("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    item.updateState()
    # sell_in should still decrease but quality remains constant
    assert item.getSellIn() == 0
    assert item.getQuality() == 80


@pytest.mark.updateState

def test_aged_brie_item_update_state():
    item = AgedBrie("Aged Brie", sell_in=1, quality=10)
    item.updateState()

    assert item.getSellIn() == 0
    assert item.getQuality() == 11


@pytest.mark.updateState

def test_backstage_item_update_state_before_expiry():
    item = Backstage("Backstage pass", sell_in=11, quality=20)
    item.updateState()

    assert item.getSellIn() == 10
    assert item.getQuality() == 22


@pytest.mark.updateState

def test_backstage_item_update_state_on_expiry():
    item = Backstage("Backstage pass", sell_in=0, quality=0)
    item.updateState()

    assert item.getSellIn() == -1
    assert item.getQuality() == 0


@pytest.mark.updateState

def test_normal_item_after_expiry():
    item = NormalItem("foo", sell_in=0, quality=5)
    item.updateState()

    assert item.getSellIn() == -1
    assert item.getQuality() == 3  # quality drops by 2 after expiry


@pytest.mark.updateState

def test_conjured_item_after_expiry():
    item = Conjured("Conjured Cake", sell_in=0, quality=5)
    item.updateState()

    assert item.getSellIn() == -1
    assert item.getQuality() == 1  # double degradation after expiry


@pytest.mark.updateState

def test_aged_brie_item_after_expiry():
    item = AgedBrie("Aged Brie", sell_in=0, quality=7)
    item.updateState()

    assert item.getSellIn() == -1
    assert item.getQuality() == 9  # increases by 2 after expiry


@pytest.mark.updateState

def test_backstage_item_in_mid_range():
    item = Backstage("Backstage pass", sell_in=5, quality=10)
    item.updateState()

    assert item.getSellIn() == 4
    assert item.getQuality() == 13  # increases by 3 when 1-5 days


@pytest.mark.updateState

def test_backstage_item_sellin_negative_after():
    item = Backstage("Backstage pass", sell_in=-1, quality=10)
    item.updateState()

    assert item.getSellIn() == -2
    assert item.getQuality() == 0  # quality drops to zero once expired


# boundary tests for updateState quality limits

@pytest.mark.updateState

def test_updateState_quality_never_exceeds_50():
    # normal item
    item = NormalItem("foo", sell_in=5, quality=55)
    item.updateState()
    assert item.getQuality() == 49

    # aged brie
    item = AgedBrie("Aged Brie", sell_in=5, quality=50)
    item.updateState()
    assert item.getQuality() == 50

    # conjured
    item = Conjured("Conjured Cake", sell_in=3, quality=51)
    item.updateState()
    assert item.getQuality() == 48

    # backstage
    item = Backstage("Backstage pass", sell_in=11, quality=50)
    item.updateState()
    assert item.getQuality() == 50

@pytest.mark.updateState

def test_updateState_quality_never_negative():
    item = NormalItem("foo", sell_in=5, quality=0)
    item.updateState()
    assert item.getQuality() == 0
    item = Conjured("Conjured Cake", sell_in=-1, quality=0)
    item.updateState()
    assert item.getQuality() == 0
    # backlog for backstage
    item = Backstage("Backstage pass", sell_in=5, quality=0)
    item.updateState()
    assert item.getQuality() == 0
