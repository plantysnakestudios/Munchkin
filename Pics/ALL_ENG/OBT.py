import requests as r
import pickle as p
import os

types = {}

with open ("cardtypes.pickle", "rb") as inn:
    types = p.load(inn)
    inn.close()
del inn

with open("card.pickle", "rb") as dat:
    data = p.load(dat)
    dat.close()
del dat

def arrange():
    from PIL import Image
    global types, data
    print ("Отделы: ")
    if not list(types.keys()) == []:
        for j in types.keys():
            print(j, types[j])
    else:
        print("Пока ничего нет.")
    say = input("Введите номер изображения или Enter для 0 изображения. 0 для выхода. 0 изображение под номером 1\n")
    i = 0 if say == "" else (int(say) - 1)
    lenn = len (data)
    while (say != "0") and (i < lenn):
        count = 0
        for jj in types.values():
            for ii in jj:
                if (i == ii):
                    tmp3 = list(types.keys())
                    print(i, "already in", tmp3[count])
                    print ("Skipping...")
                    i += 1
                    continue
            count += 1
        tmp = open("tmp.jpg", "wb")
        print("OBT изображение", i, data[i])
        file = r.get(data[i], stream = True)
        tmp.write(file.content)
        tmp.close()
        tmpim = open("tmp.jpg", "rb")
        try:
            im = Image.open(tmpim)
        except OSError:
            del data[i]
            lenn = len (data)
            continue
        im.show()
        print ("Отделы: ")
        if not list(types.keys()) == []:
            for j in types.keys():
                print(j, types[j])
        else:
            print("Пока ничего нет.")
        ch = input("Что сделать с ссылкой?\n\t'del' чтобы удалить ненужное\n\t'skip' чтобы пропустить картинку\n\t'addto имя' чтобы добавить в коллекцию 'имя'\n")
        tmpim.close()
        tmp = 1
        while tmp:
            tmp = 0
            if ("del" in ch):
                del data[i]
            elif ("addto" in ch):
                ch = ch [6:]
                if (not ch in types.keys()):
                    types[ch] = []
                types[ch].append(i)
                i += 1
            elif ("skip" in ch):
                i += 1
            else:
                print("Ошибка. Повторите ввод.")
                tmp = 1
                ch = input("Что сделать с ссылкой?\n\t'del' чтобы удалить ненужное\n\t'save' чтобы сохранить типы\n\t'load' чтобы загрузить с предыдущего типа\n\t'addto имя' чтобы добавить в коллекцию 'имя'\n")
        with open ("cardtypes.pickle", "wb") as out:
            p.dump(types, out)
            out.close()
        with open ("card.pickle", "wb") as out:
            p.dump(data, out)
            out.close()
        print ("Saved!")
        say = input("Нажмите Enter для следующего. 0 для выхода.\n")
        print ("Отделы: ")
        lenn = len (data)
        for j in types.keys():
            print(j, types[j])
    os.remove("tmp.jpg")


def download(rang, dirn):
    for i in rang:
        print ("Downloading ", i, data[i], end = "")
        try:
            file = r.get(data[i], stream = True)
            try:
                os.mkdir(dirn)
            except:
                pass
            out = open(dirn + "/" +"0" * (3 - len(str(i))) + str(i) + ".jpg", "wb")
            out.write(file.content)
            print(" Done!")
            out.close()
        except r.exceptions.ConnectionError:
            print("No Connection, skipping ", i, data[i])
        except IndexError:
            print("Check Numbers. No such file", i)
            return

def main():

    tmp = input("РЕЖИМ:\n\t1 - СКАЧАТЬ\n\t2 - РЕДАКТИРОВАТЬ ОТДЕЛЫ\n\t0 - ВЫХОД\n")
    tmp = int(tmp) if (tmp != "") else 35
    while tmp:
        if tmp == 1:
            print ("Выберите Отдел:")
            keys = list(types.keys())
            i = 0
            for j in types.keys():
                print(str(i + 1) +")",j, types[j])
                i += 1
            inn = input()
            try:
                inn = int(inn) - 1
            except:
                inn = -1
            while ((inn < 0) or (inn > i)):
                print ("Выберите Отдел:")
                i = 0
                for j in types.keys():
                    print(str(i + 1) +")",j, types[j])
                    i += 1
                inn = input()
                try:
                    inn = int(inn) - 1
                except:
                    inn = -1
            l = types[keys[inn]]#range(len(dat))
            download(l, keys[inn])
        elif tmp == 2:
            arrange()
        else:
            print("Ошибка. Повторите ввод")

        tmp = input("РЕЖИМ:\n\t1 - СКАЧАТЬ\n\t2 - РЕДАКТИРОВАТЬ ОТДЕЛЫ\n\t0 - ВЫХОД\n")
        tmp = int(tmp) if (tmp != "") else 35


if __name__ == "__main__":
    main()