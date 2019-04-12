import pickle as p
import os

from cards import Card

def tim():
    time = []
    time.append("ANYTIME_BUT_BATTLE")
    time.append("YOUR_TURN")
    time.append("AFTER_BATTLE")
    time.append("BATTLE")
    time.append("ANYTIME")
    print("Когда играть?")
    for i in range(len(time)):
        print(i, "-", time[i])
    tmp = input()
    return tmp

def TYPE(t):
    typ = []
    ch = " "
    door = []
    door.append("OTHER")
    door.append("МONSTER")
    door.append("MONSTER_ENHANCER")
    door.append("CURSE")
    door.append("CLASS")
    door.append("RACE")
    door.append("HELPER")
    door.append("STEED")
    door.append("CHEAT")
    door.append("PORTAL")
    item = []
    item.append("ONETIME")
    item.append("HELPER")
    item.append("PERMANENT")
    item.append("HEADGEAR")
    item.append("ARMOR")
    item.append("FOOTGEAR")
    item.append("ONEHAND")
    item.append("TWOHAND")
    item.append("BIG")
    item.append("RACEONLY")
    item.append("ALLRACEONLY")
    item.append("ALLCLASSONLY")
    item.append("CLASSONLY")
    treasure = []
    treasure.append("ITEM_ENHANCER")
    treasure.append("GUAL")
    treasure.append("OTHER")
    while (ch != "0"):
        if t == "DOOR":
            print("Какая дверь?")
            for i in range(len(door)):
                print("\t" + door[i], "=", i)
            tt = input()
            os.system("cls")
            try:
                tt = int(tt)
                if ((tt > 9) or (tt < 0)):
                    print("Ошибка.")
                    continue
            except:
                print("Ошибка.")
                continue
            typ.append(door[tt])
        elif t == "TREASURE":
            print("Какое сокровище?")
            for i in range(len(treasure)):
                print("\t" + treasure[i], "=", i)
            print("Или это ITEM?\n\tITEM = 3")
            tt = input()
            try:
                tt = int(tt)
                if ((tt > 3) or (tt < 0)):
                    print("Ошибка.")
                    continue
            except:
                print("Ошибка.")
                continue
            if tt == 3:
                t = None
                typ.append("ITEM")
            else:
                typ.append(treasure[tt])
        else:
            print("Какая шмотка?")
            for i in range(len(item)):
                print("\t" + item[i], "=", i)
            tt = input()
            try:
                tt = int(tt)
                if ((tt > 12) or (tt < 0)):
                    print("Ошибка.")
                    continue
            except:
                print("Ошибка.")
                continue
            typ.append(item[tt])
        print("Добавить еще свойств?\n0 - EXIT")
        ch = input()
    return typ

listt = [[], []]#, []]

namen = "MFantasy"

n = {"doors" : 96, "treasures" : 74, "dungeons" : 0}

for door in range(n["doors"]):
    listt[0].append(False)

for treasure in range(n["treasures"]):
    listt[1].append(False)

##for dungeon in range(n["dungeons"]):
##    listt[2].append(False)
def check():
    import os

    if n["doors"]:
        try:
            os.makedirs(os.getcwd() + r"/PicObj/DOOR/")
        except:
            for i in os.listdir(os.getcwd() + r"/PicObj/Door/"):
                for j in range(n["doors"]):
                    if os.path.exists(os.getcwd() + r"/PicObj/Door/" + namen + "_D_" + "0" * (3 - len(str(j))) + str(j) + ".card"):
                        listt[0][j] = True

    if n["treasures"]:
        try:
            os.makedirs(os.getcwd() + r"/PicObj/TREASURE/")
        except:
            for i in os.listdir(os.getcwd() + r"/PicObj/TREASURE/"):
                for j in range(n["treasures"]):
                    if os.path.exists(os.getcwd() + r"/PicObj/TREASURE/" + namen + "_T_" + "0" * (3 - len(str(j))) + str(j) + ".card"):
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
new = 1
print("Создатель карт 0.0.0.0.0.0.0.1\n\nВНИМАНИЕ!ВСЕ ДАННЫЕ ВВОДИТЬ НА АНГЛИЙСКОМ И НОМЕРА КАРТ КАК 001, а не 1")
while exitt:
    while (True):
        print ("Текущий набор - ", namen)
        descrpition = None
        name = None
        func = None
        types = []
        cost = None
        time = ""
        fpath = None
        time = 0
        level = None
        win = (None, None)
        if new:
            bpath = None
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
        else:
            break
    else:
        typee = str(typee + 1)
    typee = int(typee) - 1
    check()
    for i in range(n[TYPEE.lower() + "s"]):
        print ("0" * (3 - len(str(i))) + str(i) + ".card", "v" if listt[typee][i] else "x")
    print("Введите номер карты, которую создаете:\n")
    #print ("Введите id карты:")
    #print ("""Это набор, тип и номер карты. Например MFantsy_D_001. Или MCthulhu3_T_055. Или MFantsy6.5_DD_005.
    #DD - Dungeon or Seal or smth like this
    #D - Door
    #T - Treasure""")
    num = input()
    idd = namen + "_"
    if ((TYPEE == "DOOR") or (TYPEE == "TREASURE")):
        idd += TYPEE[0]
    else:
        idd += "DD"
    idd += "_" + str(num)
    ch = 1
    os.system("cls")
    error = ""
    while ch:
        print(error + "Ваша карта - " + TYPEE + " " + str(num) + ".\nЧто хотите сделать?")
        error = ""
        if (not name):
            print ("1 - Добавить Имя.")
        else:
            pass
        if (not descrpition):
            print("2 - Добавить Описание.")
        else:
            pass
        if (not func):
            print(f"3 - Уточнить {'функцию' if TYPEE == 'TREASURE' else 'BADSTUFF или свойство'} карты.")
        else:
            pass
        if (not types):
            print("4 - Уточнить тип карты.")
        else:
            pass
        print("5 - SAVE")
        if (not fpath):
            print("6 - Pic")
        else:
            pass
        print("7 - Уточнить время использования(default: ANYTIME_BUT_BATTLE).")
        if types[1] == "MONSTER":
            print("8 - Уточнить уровень монстра.\n9 - Уточнить награду за победу над монстром.")
        print("0 - EXIT")
        ch = input()
        try:
            ch = int(ch)
        except:
            ch = 35
        if (ch == 1):
            print("Введите имя карты.")
            name = input()
        elif(ch == 2):
            print("Введите описание карты.")
            descrpition = input()
        elif(ch == 3):
            import f
            func = f.f()
        elif(ch == 4):
            types = [TYPEE]
            types.extend(TYPE(TYPEE))
            types = tuple(types)
        elif(ch == 5):
            if (TYPEE == "TREASURE"):
                if (name) and (descrpition) and (func) and (len(types) >= 2) and (fpath) and (bpath):
                    card = Card(name, descrpition, types, power = func, cost = cost, image = (fpath, bpath), play = time)
                    o = open (os.getcwd() + "/PicObj/" + TYPEE + "/" + idd + ".card", "wb")
                    p.dump(card, o)
                    o.close()
                    ch = 0
                else:
                    error = "Не все данные заполнены.\n"
            elif (TYPEE == "DOOR"):
                if (name) and (descrpition) and (func) and (len(types) >= 2) and (fpath) and (bpath):
                    card = Card(name, descrpition, types, lvl = level, win = win, power = func, image = (fpath, bpath), play = time)
                    o = open (os.getcwd() + "/PicObj/" + TYPEE + "/" + idd + ".card", "wb")
                    p.dump(card, o)
                    o.close()
                    ch = 0
                else:
                    error = "Не все данные заполнены.\n"
            else:
                pass
        elif(ch == 6):
            print("Вставьте отностительный путь до лицевой стороны карты " + str(num))
            fpath = input()
            while (not os.path.exists(os.getcwd() + "/" + fpath)):
                print("Ошибка. Попробуйте еще раз.")
                print("Вставьте отностительный путь до лицевой стороны карты " + str(num))
                fpath = input()
            fpath += r"../../" + fpath
            if new:
                print("Вставьте отностительный путь до задней стороны карты " + str(num))
                bpath = input()
                while (not os.path.exists(os.getcwd() + "/" + bpath)):
                    print("Ошибка. Попробуйте еще раз.")
                    print("Вставьте отностительный путь до задней стороны карты " + str(num))
                    fpath = input()
                bpath += r"../../" + bpath
        elif(ch == 7):
            time = tim()
        elif(ch == 8):
            print("Введите уровень монстра.")
            level = input()
        elif(ch == 9):
            print("Введите кол-во уровней за победу над монстром.")
            win[0] = input()
            print("Введите кол-во сокровищ за победу над монстром.")
            win[1] = input()

        elif(ch == 0):
            pass
        else:
            error = "Ошибка. Повторите ввод.\n"
        os.system("cls")

    print("Создать еще карту?\t0 - выход.")
    exitt = input()
    if exitt == "0":
        exitt = 0
    else:
        exitt = 1
        print("Продолжишь заполнять " + TYPEE + "?\n1 - Y\n2 - N")
        tmp = input()
        while ((tmp != "1") and (tmp != "2")):
            print("ERROR.\nПродолжишь заполнять " + TYPEE + "?\n1 - Y\n2 - N")
            tmp = input()
        tmp = int(tmp)
        if (tmp - 1):
            new = True
        else:
            new = False
