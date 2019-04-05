def doMagick(name, path, flag = 1):
    import os
    scale = "-scale 4600x2520 " if flag else ""
    command = "convert -density 2000 -colorspace sRGB " + os.path.join(path, name) + r" " + scale + path + "/" + name[:-4] + ".png"
    os.system(command)

def main():
    doMagick ("ALL_ENG/tmp.jpg", ".")

if __name__ == "__main__":
    main()#pass
