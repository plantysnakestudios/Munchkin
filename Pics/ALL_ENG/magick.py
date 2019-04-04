def doMagick(name, count, path):
    import os

    command = "convert -density 2000 -colorspace sRGB " + os.path.join(path, name) + r" -scale 4600x2520 " + os.path.join(path, "cards/") + "0" * (3 - len(str(count))) + str(count) + ".png"
    os.system(command)

def main():
    doMagick ("ALL_ENG/tmp.jpg", 0)

if __name__ == "__main__":
    main()#pass
