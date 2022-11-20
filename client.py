import socket, threading, time

key = 8194
shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))

        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0
server = ("192.168.56.1", 9090)  # server ip - address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)
alias = input("Name: ")
rT = threading.Thread(target=receving, args=("RecvThred", s))
rT.start()
while shutdown == False:
    if join == False:
        join = True
        s.sendto(("[" + alias + "] => join chat ").encode("utf-8"), server)
    else:
        try:
            message = input("Введите сообщение: ")
            if message != "":
                s.sendto((message).encode("utf-8"), server)
            s.sendto(("[" + alias + "] : " + message).encode("utf-8"), server)
        except:
            s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
