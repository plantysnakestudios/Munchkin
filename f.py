ff = "YES"
def f():
    global ff
    ff = "NO"
    import msvcrt, os, pdb
    strr = b''''''
    inp = [b'g', b'l', b'o', b'b', b'a', b'l', b' ', b'f', b'u', b'n', b'c', b'\n', b'd', b'e', b'f', b' ', b'f', b'u', b'n', b'c', b'(', b')', b':', b'\n']
    fl = 1
    print(r"Enter your func below. Remember, that tabs are 4 ' ' and exit is '`'")
    while fl:
        input_char = msvcrt.getch()
        if (not input_char == b"\x08") and (not input_char == b"`") and (not input_char == b"\r") and (not input_char == b"\t") and (not input_char == b"\xe0"):
            inp.append(input_char)
        elif (input_char == b"\x08"):
            try:
                tmp = inp.pop()
            except IndexError:
                pass
        elif (input_char == b"\r"):
            inp.append(b"\n")
            #print(flush = True)
        elif (input_char == b"\t"):
            for i in range(4):
                inp.append(b" ")
        os.system("cls")
        for i in inp:
            print(i.decode(), end = "", flush = True)
            #print("    ", flush = True, end = "", sep = "")
        #print(input_char.decode(), end = "", flush = True)
        if input_char.upper() == b'`':
            print ('OK')
            fl = 0


    strr = b''''''.join(inp)
    #strr += b"\nglobal func\nfunc = func1"
    print (strr)
    strr = strr.decode()
    return strr
##    print(strr)
##    pdb.set_trace()
##    exec (strr, globals(), locals())
##    pdb.set_trace()
##    try:
##        func()
##    except:
##        print("no")

def main():
    f()

if __name__ == "__main__":
    pass#main()

