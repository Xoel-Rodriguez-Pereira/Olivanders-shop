class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "{0}, {1}, {2}".format(self.name, self.sell_in, self.quality)
    


class Upgradeable():
    def updateQuality():
        pass
    
    def updateSellIn():
        pass

    def updateState(self):
        self.updateSellIn() # The order has to be 1st updateSellIn 2º updateQuality
        self.updateQuality()
        


class NormalItem(Item, Upgradeable):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.quality >= 50:
            self.quality = 50

        if self.quality > 0:
            if self.sell_in >= 0:
                self.quality -= 1
            elif self.sell_in < 0:
                self.quality -= 2
        else:
            self.quality = 0

    def updateSellIn(self):
        self.sell_in -= 1

    def getSellIn(self):
        return self.sell_in
    
    def getQuality(self):
        return self.quality


class Sulfuras(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        self.quality = 80


class AgedBrie(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.sell_in >= 0:
            self.quality += 1
        elif self.sell_in < 0:
            self.quality += 2
        
        if self.quality >= 50:
            self.quality = 50
            


class Conjured(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.quality >= 50:
            self.quality = 50
            
        if self.quality > 1:
            if self.sell_in >= 0:
                self.quality -= 2
            elif self.sell_in < 0:
                self.quality -= 4
        else:
            self.quality = 0


class Backstage(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.quality > 0:
            if self.sell_in > 10:
                self.quality += 1
            elif self.sell_in > 5:
                self.quality += 2
            elif self.sell_in > 0:
                self.quality += 3
            elif self.sell_in <= 0:
                self.quality = 0
        else:
            self.quality = 0

        if self.quality >= 50:
            self.quality = 50
            

class Shop():
    def __init__(self):
        self._inventory = []

    def updateInventory(self):
        updatedInventory = []
        for item in self._inventory:
            item.updateState()
            updatedInventory.append(item)

        self._inventory = updatedInventory


    def setInventory(self, newItems):
        for item in newItems:
            self._inventory.append(item)

    def showInventory(self):
        for item in self._inventory:
            print(item)