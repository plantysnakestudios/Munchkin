import socket, threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print ("[+] New thread started for "+ip+":"+str(port))


    def run(self):
        print ("Connection from : "+ip+":"+str(port))

        self.socket.send(bytes("\nWelcome to the server\n\n", encoding='UTF-8'))

        data = "dummydata"

        while len(data):
            data = self.socket.recv(2048)
            print ("Client sent : " + str(data))
            self.socket.send(bytes("You sent me : " + str(data), encoding='UTF-8'))

        print ("Client disconnected...")

host = "localhost"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))
threads = []


while True:
    tcpsock.listen(4)
    print ("\nListening for incoming connections...\n")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()