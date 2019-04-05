def doMagick(name, cc, *numbersofends, numc = 2):
    import os

    count = 0
    name2 = name[:-4]
    if (not os.path.exists(name2)):
        os.mkdir(name2)

    for i in range (cc):
        if (i % 2 == 0):
            command = "convert -density 2000 -colorspace sRGB " + name + "[" + str(i) + "] -scale 1920x1080 "+ name2 + r"/munchkin" + "0" * (3 - len(str(count))) + str(count) + ".png"
            os.system(command)
            count += 1

    if (numbersofends == ()):
        numbersofends = (1, cc - 1)
    c = 0
    for i in numbersofends:
        command = "convert -density 2000 -colorspace sRGB " + name + "[" + str(i) +"] -scale 1920x1080 "+ name2 + r"/munchkinBack" + "0" * (2 - len(str(c))) + str(c) + ".png"
        os.system(command)
        c += 1

def main():
    doMagick ("M1_fantasy.pdf", 0)

if __name__ == "__main__":
    main()#pass