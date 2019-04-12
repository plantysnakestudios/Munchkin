from enum import Enum as e
class Card():

    class typeOfDOOR (e):
        OTHER = 0
        МONSTER = 1
        MONSTER_ENHANCER = 2
        CURSE = 3
        CLASS = 4
        RACE = 5
        HELPER = 6
        STEED = 7
        CHEAT = 8
        PORTAL = 9


    class typeOfTREASURE (e):
        ITEM_ENHANCER = 0
        GUAL = 1
        OTHER = 2

    class item (e):
        ONETIME = 0
        HELPER = 1
        PERMANENT = 2
        HEADGEAR = 3
        ARMOR = 4
        FOOTGEAR = 5
        ONEHAND = 6
        TWOHAND = 7
        BIG = 8
        RACEONLY = 9
        ALLRACEONLY = 10
        ALLCLASSONLY = 11
        CLASSONLY = 12

    class playTime(e):
        ANYTIME_BUT_BATTLE = 0
        YOUR_TURN = 1
        AFTER_BATTLE = 2
        BATTLE = 3
        ANYTIME = 4

    def __init__ (self, name, descript, tyyp, lvl = None, win = (None, None), power = ("", ), cost = None, image = (None, None), play = 0):
        self.name = name
        self.description = descript
        if (tyyp[1] == "ITEM"):
            ex = "self.type = (self.item." + tyyp[2] + ","
            for i in range(3, len(tyyp)):
                ex += " self.item." + tyyp[i] + ","
            ex += ")"
        else:
            ex = "self.type = (self.typeOf" + tyyp[0]
            ex += "." + tyyp[1] + ", )"


        exec(ex)
        self.level = lvl
        self.win = win
        self.function = power
        self.cost = cost
        self.front = image[0]
        self.back = image[1]
        self.play = self.playTime(play)

    def func(self, munchkin):
        exec(self.function[0], globals(), locals())
        func(self, munchkin)
        return self.returnn

    def func0(self, munchkin):
        exec(self.function[1], globals(), locals())
        func(self, munchkin)
        return self.returnn

    def func1(self, munchkin):
        exec(self.function[2], globals(), locals())
        func(self, munchkin)
        return self.returnn


def main():
    cardd = Card("one stuff nobody reads", "some stuff", ("TREASURE", "ITEM", "HEADGEAR", "BIG"), power = ('global func\ndef func(self, munchkin):\n    print("kek")\nself.returnn = 999', ), cost = 200, image = (r"Pics\ALL_ENG\M_Fantasy\Treasure\card000.png",""))#"+5 if clas == 'War' or clas == 'Wiz' else +3", 200)
    cardd1 = Card("one stuff nobody reads", "some stuff", ("DOOR", "HELPER"))
    cardd2 = Card("one stuff nobody reads", "some stuff", ("TREASURE", "ITEM", "HELPER"))

    for i in range (len(cardd.type)):
        print(cardd.type[i].name, cardd.type[i].value)
    print()

    for i in range (len(cardd1.type)):
        print(cardd1.type[i].name, cardd1.type[i].value)
    print()

    for i in range (len(cardd2.type)):
        print(cardd2.type[i].name, cardd2.type[i].value)
    print()

    for c in Card.item:
        print(c.name, c.value)

    with open("example.card", "wb") as cc:
        import pickle
        pickle.dump(cardd, cc)
        cc.close()
        del pickle


if __name__ == "__main__":
    main()