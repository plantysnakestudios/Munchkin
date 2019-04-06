import magick, crop
import os

types = [""]#"Doors", "Treasure", ""]#, "Dungeon"]

l = []#os.listdir(os.getcwd())#[]
#l.pop()
#l.pop()
l.append("M_Fantasy")

for i in range (2, 5):
    l.append("M_Cthulhu_" +  str(i))

for ii in l:
    for j in range(len(types)):
        countt = 0
        count = 0
        path = os.path.join(os.getcwd(), ii + "/" + types[j])

        try:
            lis = os.listdir(path)
        except:
            lis = ""
        jj = 0
        while (count < len(lis)):
            i = lis [count]
            ext = i[i.rfind(".") + 1:]
            if (ext == "png"):
                print (i, jj)
                if (not "card" in i) and (not "Cover" in i):
                    magick.doMagick(i, path)
                    countt = crop.doCrop(i, path, countt)
                    count -= 1
                else:
                    magick.doMagick(i, path, flag = 0)
                jj += 1
            count += 1
            lis = os.listdir(path)
##import pygame
##pygame.mixer.init()
##pygame.mixer.music.load("file.mp3")
##pygame.mixer.music.play()
##input()
##pygame.mixer.music.stop()