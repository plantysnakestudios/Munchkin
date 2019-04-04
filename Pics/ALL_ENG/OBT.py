import requests as r
import pickle as p

def main():
    data = open("card", "rb")
    dat = p.load(data)

    name = ""
    for i in range(len(dat)):
        out = open(r"ALL_ENG/" + "0" * (3 - len(str(i))) + str(i) + ".jpg", "wb")
        file = r.get(dat[i], stream = True)
        out.write(file.content)
        out.close()

if __name__ == "__main__":
    main()