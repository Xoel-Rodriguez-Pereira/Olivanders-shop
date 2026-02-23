class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    

class Upgradeable():
    def updateQuality():
        pass

class NormalItem(Item, Upgradeable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.quality > 0:
            if self.sell_in >= 0:
                self.quality -= 1
            if self.sell_in < 0:
                self.quality -= 2
        else:
            self.quality = 0