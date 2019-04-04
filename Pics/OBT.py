import requests as r

def main():
    data = open("cards", "rb")
    data = data.read()
    data = data.decode("ANSI")
    n = 0
    dat = []
    while (n != -1):
        n = data.find(r"http://cloud-3.steamusercontent.com/ugc/", n + 1)
        bit = data.find("\x00", n)
        strr = data[n : bit]
        if (not strr in dat):
            dat.append(strr)
    #print(len(dat))
    name = ""
    for i in range(len(dat)):
        out = open(r"tmp/" + "0" * (3 - len(str(i))) + str(i) + ".jpg", "wb")
        file = r.get(dat[i], stream = True)
        out.write(file.content)
        out.close()

if __name__ == "__main__":
    main()