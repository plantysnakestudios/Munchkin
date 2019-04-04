import magick, crop
import os

count = 0

path = os.path.join(os.getcwd(), r"ALL_ENG/")

for i in os.listdir(path):

    ext = i[i.rfind(".") + 1:]
    if (ext == "jpg"):
        print (i, count)
        magick.doMagick(i, count, path)
        #crop.doCrop(i, path)
        count += 1