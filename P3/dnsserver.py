'''
Programming and Language Version: Python3 3.8.6
Testing Environment: 
    OS: Ubuntu 20.10 x86_64
    Command Lines: 
        1. To simulate a running connection: 
            a. Compile dnsclient.py using python3 dnsclient.py 127.0.0.1 9999 host1.student.test
            b. Compile dnsserver.py using python3 dnsserver.py 127.0.0.1 9999
'''

import sys
import socket
import struct

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))

file = open("dns-master.txt", "r")
test = False
print("The server is ready to receive on port:  " + str(serverPort) + "\n")

while True:
    data, address = serverSocket.recvfrom(1024)
    dat1 = str(struct.unpack('hhihh', data[0:12])) #slice up to 12 bytes

    dat = []
    
    for i in dat1:
        if i.isdigit():
            dat.append(int(i))

    question = data[12:].decode()
    qSplit = question.split()
    

    for line in file:
        li=line.strip()
        if not li.startswith("#"):
            words = line.rstrip().split()
            if words:
                if words[0] == qSplit[0]:
                    sendLine = line
                    test = True
                    break
    
    answerLength = len((line.encode('utf-8')))

    val1 = str(dat[2]) + str(dat[3])
    val2 = str(dat[4]) + str(dat[5])
    

    if test:
        codedData = question.encode()
        theData = struct.pack('hhihh',2, 0, int(val1), int(val2), answerLength)
        questionData = question.encode()
        answerData = sendLine.encode()
        returnMessage = theData + questionData + answerData
        serverSocket.sendto(returnMessage,address)
    else:
        codedData = question.encode()
        theData = struct.pack('hhihh',2, 1, int(val1), int(val2), answerLength)
        questionData = question.encode()
        answerData = "".encode()
        returnMessage = theData + questionData + answerData
        serverSocket.sendto(returnMessage,address)
    
