import magick, crop
import os, re
from PyPDF2 import PdfFileReader

for i in os.listdir(os.getcwd()):

    ext = i[i.rfind(".") + 1:]
    if (ext == "pdf"):
        pdf = open(i, "rb")
        count = PdfFileReader(pdf).getNumPages()
        pdf.close()
        print (i, count)
        magick.doMagick(i, count)
        crop.doCrop(i[:-4], count)
        os.remove(i)