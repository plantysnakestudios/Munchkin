import requests as r
import pickle as p

def main():
    data = open("card.pickle", "rb")
    dat = p.load(data)
    data.close()
    name = ""

    l = range(330, len(dat) - 1)#range(len(dat))
    for i in l:
        try:
            file = r.get(dat[i], stream = True)
            out = open("0" * (3 - len(str(i))) + str(i) + ".jpg", "wb")
            out.write(file.content)
            out.close()
        except r.exceptions.ConnectionError:
            print("No Connection, skipping ", i)

if __name__ == "__main__":
    main()