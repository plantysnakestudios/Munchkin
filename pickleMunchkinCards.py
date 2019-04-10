import pickle as p

from cards import Card

descrpition = {None : ""}
listt = [[], []]#, []]

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
                if os.path.exists(os.getcwd() + r"/PicObj/Door/" + "0" * (3 - len(str(j))) + str(j) + ".card"):
                    listt[0][j] = True

if n["treasures"]:
    try:
        os.makedirs(os.getcwd() + r"/PicObj/Treasure/")
    except:
        for i in os.listdir(os.getcwd() + r"/PicObj/Treasure/"):
            for j in range(n["treasures"]):
                if os.path.exists(os.getcwd() + r"/PicObj/Treasure/" + "0" * (3 - len(str(j))) + str(j) + ".card"):
                    listt[1][j] = True


##if n["dungeons"]:
##    try:
##        os.makedirs(os.getcwd() + r"/PicObj/Dungeon/")
##    except:
##        for i in os.listdir(os.getcwd() + r"/PicObj/Dungeon/"):
##            for j in range(n["dungeon"]):
##                if os.path.exists(os.getcwd() + r"/PicObj/Dungeon/" + "0" * (3 - len(str(j))) + str(j) + ".card"):
##                    listt[2][j] = True

exitt = 1
print("Создатель карт 0.0.0.0.0.0.0.1\n\n")
while exitt:
    while (True):
        print("Doors(1)/Treasure(2)?")
        typee = input()
        if (typee == "1"):
            TYPEE = "DOOR"
            break
        elif (typee == "2"):
            TYPEE = "TREASURE"
            break
        else:
            print("Ошибка. Повторите попытку.")
    typee = int(typee) - 1
    print("Введите номер карты, которую создаете:\n")
    for i in range(n[TYPEE.lower() + "s"]):
        print ("0" * (3 - len(str(i))) + str(i) + ".card", "v" if listt[typee][i] else "x")
    print ("Введите id карты:")
    print ()
    input()

    print("Создать еще карту?\t0 - выход.")
    exitt = input()
    if exitt == "0":
        exitt = 0



