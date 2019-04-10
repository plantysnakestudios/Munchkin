import pickle as p
import os

from cards import Card

def TYPE(t):
    typ = []
    ch = " "
    door = "        OTHER = 0\n        МONSTER = 1\n        MONSTER_ENHANCER = 2\n        CURSE = 3\n        CLASS = 4\n        RACE = 5\n        HELPER = 6\n        STEED = 7\n        CHEAT = 8\n        PORTAL = 9"
    item = "        ONETIME = 0\n        HELPER = 1\n        PERMANENT = 2\n        HEADGEAR = 3\n        ARMOR = 4\n        FOOTGEAR = 5\n        ONEHAND = 6\n        TWOHAND = 7\n        BIG = 8\n        RACEONLY = 9\n        ALLRACEONLY = 10\n        ALLCLASSONLY = 11\n        CLASSONLY = 12"
    treasure = "        ITEM_ENHANCER = 0\n        GUAL = 1\n        OTHER = 2"
    while (ch != ""):
        if t == "DOOR":
            print("Какая дверь?\n" + door)
        if t == "TREASURE":
            print("Какое сокровище?\n" + treasure)
            print("Или это ITEM?\n    ITEM = 3")

        else:
            print("Какая шмотка?\n" + item)


descrpition = None
name = None
func = None

listt = [[], []]#, []]

namen = "MFantasy"

n = {"doors" : 96, "treasures" : 74, "dungeons" : 0}

for door in range(n["doors"]):
    listt[0].append(False)

for treasure in range(n["treasures"]):
    listt[1].append(False)

##for dungeon in range(n["dungeons"]):
##    listt[2].append(False)

import os

if n["doors"]:
    try:
        os.makedirs(os.getcwd() + r"/PicObj/Door/")
    except:
        for i in os.listdir(os.getcwd() + r"/PicObj/Door/"):
            for j in range(n["doors"]):
                if os.path.exists(os.getcwd() + r"/PicObj/Door/" + namen + "_D_" + "0" * (3 - len(str(j))) + str(j) + ".card"):
                    listt[0][j] = True

if n["treasures"]:
    try:
        os.makedirs(os.getcwd() + r"/PicObj/Treasure/")
    except:
        for i in os.listdir(os.getcwd() + r"/PicObj/Treasure/"):
            for j in range(n["treasures"]):
                if os.path.exists(os.getcwd() + r"/PicObj/Treasure/" + namen + "_T_" + "0" * (3 - len(str(j))) + str(j) + ".card"):
                    listt[1][j] = True


##if n["dungeons"]:
##    try:
##        os.makedirs(os.getcwd() + r"/PicObj/Dungeon/")
##    except:
##        for i in os.listdir(os.getcwd() + r"/PicObj/Dungeon/"):
##            for j in range(n["dungeon"]):
##                if os.path.exists(os.getcwd() + r"/PicObj/Dungeon/" + namen + "_DD_" + "0" * (3 - len(str(j))) + str(j) + ".card"):
##                    listt[2][j] = True

exitt = 1
print("Создатель карт 0.0.0.0.0.0.0.1\n\nВНИМАНИЕ!ВСЕ ДАННЫЕ ВВОДИТЬ НА АНГЛИЙСКОМ И НОМЕРА КАРТ КАК 001, а не 1")
while exitt:
    while (True):
        print ("Текущий набор - ", namen)
        print("Door(1)/Treasure(2)?")
        typee = input()
        if (typee == "1"):
            TYPEE = "DOOR"
            break
        elif (typee == "2"):
            TYPEE = "TREASURE"
            break
        elif (typee == "0"):
            import sys
            sys.exit()
        else:
            print("Ошибка. Повторите попытку.")
    typee = int(typee) - 1
    for i in range(n[TYPEE.lower() + "s"]):
        print ("0" * (3 - len(str(i))) + str(i) + ".card", "v" if listt[typee][i] else "x")
    print("Введите номер карты, которую создаете:\n")
    #print ("Введите id карты:")
    #print ("""Это набор, тип и номер карты. Например MFantsy_D_001. Или MCthulhu3_T_055. Или MFantsy6.5_DD_005.
    #DD - Dungeon or Seal or smth like this
    #D - Door
    #T - Treasure""")
    num = input()
    idd = namen + "_" + ((TYPEE[0]) if ((TYPEE == "DUNGEON") or (TYPEE == "TREASURE")) else ("DD")) + "_" + str(num)
    ch = 1
    while ch:
        os.system("cls")
        print("Ваша карта - " + str(num) + ".\nЧто хотите сделать?")
        if (not name):
            print ("1 - Добавить Имя.")
        else:
            pass
        if not descrpition:
            print("2 - Добавить Описание.")
        else:
            pass
        print("3 - Уточнить функцию карты.\n4 - Уточнить тип карты.\n5 - SAVE\n6 - Pic\n0 - EXIT")
        ch = input()
        try:
            ch = int(ch)
        except:
            ch = 35
        if (ch == 1):
            print("Введите имя карты.")
            name = input()
        elif(ch == 2):
            print("Введите описание карты карты.")
            descrpition = input()
        elif(ch == 3):
            import f
            func = f.f()
        elif(ch == 4):
            types = [TYPEE]
            types.extend(TYPE(TYPEE))
        elif(ch == 5):
            card = Card(name, descrpition, (TYPEE))
            p.dump()
        else:
            print("Ошибка. Повторите ввод")



    print("Создать еще карту?\t0 - выход.")
    exitt = input()
    if exitt == "0":
        exitt = 0



