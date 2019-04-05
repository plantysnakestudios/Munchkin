import requests as r
import pickle as p

def main():
    data = open("card.pickle", "rb")
    dat = p.load(data)
    data.close()
    name = ""

    l = (209,211)#range(len(dat))
    for i in l:
        out = open("0" * (3 - len(str(i))) + str(i) + ".jpg", "wb")
        file = r.get(dat[i], stream = True)
        out.write(file.content)
        out.close()

if __name__ == "__main__":
    main()