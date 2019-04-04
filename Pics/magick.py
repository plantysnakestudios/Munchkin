def doMagick(name, count):
    import os

    name2 = name[:-4]
    if (not os.path.exists(name2)):
        os.mkdir(name2)

    command = "convert -density 2000 -colorspace sRGB " + name + "[" + str(i) + "] -scale 4600x2520 "+ name2 + r"/munchkin" + "0" * (3 - len(str(count))) + str(count) + ".png"
    os.system(command)

def main():
    doMagick ("M1_fantasy.pdf")

if __name__ == "__main__":
    main()#pass
