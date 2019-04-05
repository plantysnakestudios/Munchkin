def doCrop(name, path, count = 0):
    from PIL import Image
    import os
    rows = 7
    cols = 10
    tmp = Image.open(os.path.join(path, name))
    x = 252
    y = 360
    x1 = 0; y1 = 0
    x2 = x; y2 = y
    for j in range(rows):
        for ii in range (cols):
            tmp2 = tmp.crop((x1, y1, x2, y2))
            tmp2.save(path + "/card" + "0" * (3 - len(str(count))) + str(count) + ".png")
            count += 1
            x1 = x2; x2 += x
        x1 = 0; y1 = y * (j + 1)
        x2 = x; y2 = y * (j + 2)
    os.remove(os.path.join(path, name))
    return count

def main():
    doCrop("194.png", "D:\Munchkin\Pics\ALL_ENG\M_Cthulhu\Treasure", count = 0)

if __name__ == "__main__":
    main()#pass
