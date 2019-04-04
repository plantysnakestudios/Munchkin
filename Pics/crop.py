def doCrop(name, path):
    from PIL import Image
    import os
    count = 0
    rows = 2
    cols = 5
    tmp = Image.open(os.path.join(path, name))
    x1 = 0; y1 = 0
    x2 = 347; y2 = 540
    for j in range(rows):
        for ii in range (cols):
            tmp2 = tmp.crop((x1, y1, x2, y2))
            tmp2.save(path + "/card" + "0" * (4 - len(str(count))) + str(count) + ".png")
            count += 1
            x1 = x2; x2 += 347
        x1 = 0; y1 = 540
        x2 = 347; y2 = 1080
    #os.remove(os.path.join(path, name))

def main():
    doCrop("016.png", "D:\Munchkin\Pics\ALL_ENG\cards")

if __name__ == "__main__":
    main()#pass
