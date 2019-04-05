def doCrop(name, num):
    from PIL import Image
    import os
    count = 0
    rows = 2
    cols = 5
    index = os.listdir(name)
    for i in range(int(num/2)):
        tmp = Image.open(os.path.join(name, index[i]))
        x1 = 0; y1 = 0
        x2 = 347; y2 = 540
        for j in range(rows):
            for ii in range (cols):
                tmp2 = tmp.crop((x1, y1, x2, y2))
                tmp2.save(name + "/card" + "0" * (3 - len(str(count))) + str(count) + ".png")
                count += 1
                x1 = x2; x2 += 347
            x1 = 0; y1 = 540
            x2 = 347; y2 = 1080
        os.remove(os.path.join(name, index[i]))
    c = 0
    for i in (index):
        if ("munchkinBack" in i):
            tmp = Image.open(name + "/" + i)
            x1 = 0; y1 = 0
            x2 = 347; y2 = 540
            tmp2 = tmp.crop((x1, y1, x2, y2))
            tmp2.save(name + "/" + "cardBack" + "0" * (2 - len(str(c))) + str(c) + ".png")
            os.remove(name + "/" + i)
            c += 1

def main():
    doCrop("M1_fantasy", 0)

if __name__ == "__main__":
    main()#pass