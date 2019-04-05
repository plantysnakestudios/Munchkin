import magick, crop
import os

types = ["Doors", "Treasure"]#, "Dungeon"]

l = []#os.listdir(os.getcwd())#[]
#l.pop()
#l.pop()
l.append("M_Cthulhu")

for i in range (2, 4):
    l.append("M_Cthulhu_" +  str(i))

for ii in l:
    for j in range(len(types)):
        countt = 0
        count = 0
        path = os.path.join(os.getcwd(), ii + "/" + types[j])

        try:
            l = os.listdir(path)
        except:
            l = ""

        while (count < len(l)):
            l = os.listdir(path)
            i = l [count]
            ext = i[i.rfind(".") + 1:]
            if (ext == "png"):
                print (i, count)
                if (not "card" in i):
                    magick.doMagick(i, path)
                    countt = crop.doCrop(i, path, countt)
                else:
                    magick.doMagick(i, path, flag = 0)
                    count += 1
##import pygame
##pygame.mixer.init()
##pygame.mixer.music.load("file.mp3")
##pygame.mixer.music.play()
##input()
##pygame.mixer.music.stop()