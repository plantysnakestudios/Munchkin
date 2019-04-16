
class Dice():
    def __init__(self, ):
        self.change = 0

    def roll(self, ):
        from random import randint as r
        roll = r(1, 6)
        return roll + self.change

class Munchkin():

    def __init__(self, ):
        self.level = 1
        self.name = "" #из профиля
        self.sex = "" #из профиля
        self.headgear = [None, ]
        self.armor = [None, ]
        self.footgear = [None, ]
        self.arm = [None, ]
        self.race = ["Human", ]
        self.abil = [None]
        self.clas = [None, ]
        self.curse = []
        self.helper = [None, ]
        self.steed = []
        self.stuff = []
        self.handcard = []
        self.cheat = []
        self.maxamount = {}
        for i in ("headgear", "armor", "footgear", "race", "clas", "helper", "steed"):
            self.maxamount[i] = 1
        self.maxamount["arm"] = 2
        self.maxamount["handcard"] = 5
        self.optimise()
        self.dice = Dice()
        self.getPower()

    def optimise(self, ):
        while (len(self.headgear) < self.maxamount['headgear']):
            self.headgear.append(None)

        while (len(self.armor) < self.maxamount['armor']):
            self.armor.append(None)

        while (len(self.footgear) < self.maxamount['footgear']):
            self.footgear.append(None)

        while (len(self.race) < self.maxamount['race']):
            self.race.append(None)

        while (len(self.clas) < self.maxamount['clas']):
            self.clas.append(None)

        while (len(self.helper) < self.maxamount['helper']):
            self.helper.append(None)

        while (len(self.steed) < self.maxamount['steed']):
            self.steed.append(None)

        while (len(self.arm) < self.maxamount['arm']):
            self.arm.append(None)

        while (len(self.handcard) < self.maxamount['handcard']):
            self.handcard.append(None)

    def getPower(self, ):
        self.power = self.level
        for i in range(len(self.headgear)):
            if self.headgear[i]:
                self.power += self.headgear[i].on(self)
                self.headgear[i].off(self)
        for i in range(len(self.armor)):
            if self.armor[i]:
                self.power += self.armor[i].on(self)
                self.headgear[i].off(self)
        for i in range(len(self.footgear)):
            if self.footgear[i]:
                self.power += self.footgear[i].on(self)
                self.headgear[i].off(self)
        for i in range(len(self.arm)):
            if self.arm[i]:
                self.power += self.arm[i].on(self)
                self.headgear[i].off(self)
        for i in range(len(self.helper)):
            if self.helper[i]:
                self.power += self.helper[i].on(self)
                self.headgear[i].off(self)
        for i in range(len(self.steed)):
            if self.steed[i]:
                self.power += self.steed[i].on(self)
                self.headgear[i].off(self)
        for i in range(len(self.stuff)):
            self.power += self.stuff[i].on(self)
            self.headgear[i].off(self)
        for i in range(len(self.cheat)):
            self.power += self.cheat[i].on(self)
            self.headgear[i].off(self)

    def set(self, where, what):
        j = 0
        self.optimise()
        for i in where:
            if i == None:
                where[j] = what
                what.on(self)
                return
            j += 1
        #print("not able to can", what.type)
        #print(where)

    def offset(self, where, what):
        j = 0
        for i in where:
            if i == what:
                where.pop(j)
                what.off(self)
                self.optimise()
                return
            j += 1

    def abl(self,):
        for i in self.abil:
            try:
                exec(i)
                func()
            except:
                pass


m1 = Munchkin()
print(m1.power)
from cards import Card
import pickle
with open("example.card", "rb") as cc:
    card = pickle.load(cc)
    cc.close()
m1.set(m1.headgear, card)
m1.abl()
##m1.set(m1.headgear, card)
##m1.maxamount["headgear"] += 1
##m1.set(m1.headgear, card)
##m1.getPower()
##print(m1.power)
m1.offset(m1.headgear, card)
m1.getPower()
print(m1.power)