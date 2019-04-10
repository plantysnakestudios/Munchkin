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

    def __init__ (self, name, descript, tyyp, power = "", cost = None):
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
        self.pcond = power
        self.cost = cost
        #self.power = power

    def power(self, munchkin):
        self.val = []
        pc = self.pcond.split("if")
        pc2 = pc[1].split("else")
        pc.pop()
        pc.extend(pc2)
        ex = ["","","",""]
        if (not "and" in pc[1]) and (not "or" in pc[1]):
            pc[1] = pc[1].split ("==")
            ex = "for i in munchkin." + pc[1][0] + ":\n"
            ex += "    if i == " + pc[1][1] + ":\n"
            ex += "       self.val.append(" + pc[0] + ")\n"
            ex += "    else:\n"
            ex += "       self.val.append(" + pc[2] + ")"
        else:
            if ("or" in pc[1]):
                con = "or"
            elif ("and" in pc[1]):
                con = "and"
            pc[1] = pc[1].split(con)
            for i in range(len(pc[1])):
                pc[1][i] = pc[1][i].split ("==")

            ex = "for i in munchkin." + pc[1][0][0] + ":\n"
            ex += "    if i == " + pc[1][0][1] + ":\n"
            ex += "       self.val.append(" + pc[0] + ")\n"
            ex += "    else:\n"
            ex += "       self.val.append(" + pc[2] + ")\n"

            ex += "for i in munchkin." + pc[1][1][0] + ":\n"
            ex += "    if i == " + pc[1][1][1] + ":\n"
            ex += "       self.val.append(" + pc[0] + ")\n"
            ex += "    else:\n"
            ex += "       self.val.append(" + pc[2] + ")"


        #ex = "\n".join(ex)
        exec(ex, globals(), locals())
        self.val = max(self.val)
        return self.val


def main():
    cardd = Card("one stuff nobody reads", "some stuff", ("TREASURE", "ITEM", "HEADGEAR", "BIG"), "+5 if clas == 'War' or clas == 'Wiz' else +3", 200)
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