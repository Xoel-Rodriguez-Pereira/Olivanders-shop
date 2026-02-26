from src.logic import *
def main():
    inventory = [
        NormalItem("+5 Dexterity Vest", 10, 20),
        AgedBrie("Aged Brie", 2, 0),
        NormalItem("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
        Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured ("Mana Cake", 3, 6),
    ]

    olivanders = Shop()

    olivanders.setInventory(inventory)

    olivanders.updateInventory()

    olivanders.showInventory()

if __name__ == "__main__":
    main()
