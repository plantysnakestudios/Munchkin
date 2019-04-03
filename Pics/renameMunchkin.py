import os

def rename(count, path = os.getcwd()):
    listt = os.listdir(path)
    lenm = range(len(listt))
    for j in lenm:
        tmp = listt[j]
        dirr = os.path.join(path, tmp)
        if os.path.isdir (dirr):
            if ((tmp == "Doors") or (tmp == "Treasure")):
                count = 0
            tmpp = os.path.join(path, tmp)
            count = rename(count, path = tmpp)

        else:
            if (not "cardBack" in tmp):
                print (tmp, "->", end = " ")
                tmp2 = tmp [:-7] + "0" * (3 - len(str(count))) + str(count) + ".png"
                print (tmp2, end = "\n")
            try:
                tmp = os.path.join(path, tmp)
                tmp2 = os.path.join(r"..", tmp2)
                tmp2 = os.path.join(path, tmp2)
                count += 1
                os.rename(tmp, tmp2)


            except:
                pass

    return count

def main():
    directory = os.listdir(r"./")
    path = os.getcwd()
    for direct in directory:
        #direct = os.path.join(r"./M1_Fantasy/Doors", direct)
        direct = os.path.join(path, direct)
        if os.path.isdir (direct):
            t = rename(0, path = direct)

if __name__ == "__main__":
    main()
