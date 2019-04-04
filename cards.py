import enum as e
class Card():

    class typeOfDOOR (e.Enum):

            OTHER = 0
            MONSTER = 1
            MONSTER_ENHANCER = 2
            CURSE = 3
            CLASS = 4
            RACE = 5
            HELPER = 6
            STEED = 7
            CHEAT = 8
            PORTAL = 9


    class typeOfTREASURE (e.Enum):

            OTHER = 0
            ITEM = 1
            ITEM_ENHANCER = 2
            GUAL = 3


    def __init__ (self, name, descript, tyyp):
        self.name = name
        self.description = descript
        ex = "self.type = self.typeOf" + tyyp[0] + "." + tyyp[1]
        exec(ex)
        #self.type = tyyp

    def info (self, *inf):
        if self.type.value == 1:
            self.level = setLevel()



def main():
    cardd = Card("one stuff nobody reads", "some stuff", ("DOOR", "MONSTER"))
    print(cardd.type.value)
    cardd.info()
    for c in Card.typeOfDOOR:
        print(c.name)

if __name__ == "__main__":
    main()