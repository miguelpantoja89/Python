#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
from pyfiglet import figlet_format

subprocess.call('cls',shell=True) ###Si quieres hacerlo en linux usa clear

print(figlet_format("Port Scanner MGTech"))
remoteServer = input("Enter a remote host  to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print("-"*60)
print("Please wait, scanning remote host " + remoteServerIP)
print("-"*60)

t_start = datetime.now()
 ###Primeros 1024 puertos son puertos registrados, visita la IANA para saber mas
 ###para ipv4 y conex TCP
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        res = sock.connect_ex((remoteServerIP, port))
        if res == 0:
            print("Port {}: Open ".format(port) )
        sock.close
            
except KeyboardInterrupt:
    print("You pressed Ctrl + C, you killed the process")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be reolved, Exiting!")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()

t_end = datetime.now()
total_time = t_end - t_start
print("Scanning completed in:" , total_time)