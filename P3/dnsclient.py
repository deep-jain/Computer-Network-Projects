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
import random
import struct

ip = sys.argv[1]
port = int(sys.argv[2])
hostName = sys.argv[3]

question = hostName + " A IN"
questionLength = len((question.encode('utf-8')))        

messageID = random.randint(1,100)
# one more

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Default socket timeout
clientsocket.settimeout(1)

sendData = question + " " + str(messageID)

print("Sending Request to " + str(ip) + ", " + str(port) + ":")
print("Message ID: " + str(messageID))
print("Question Length: " + str(questionLength) + " bytes")
print("Answer Length: " + str(0))
print("Question: " + question)

codedData = question.encode()
theData = struct.pack('hhihh',1, 0, messageID, questionLength, 0)

value = theData + codedData

print("Sending Request to " + str(ip) + ", " + str(port) + ":")    

for i in range(3):
    try:
        clientsocket.sendto(value,(ip, port))
        data, address = clientsocket.recvfrom(100)
        print("Received Response from " + str(ip) + ", " + str(port))
        dat1 = str(struct.unpack('hhihh', data[0:12]))
        
        dats = []

        for i in dat1:
            if i.isdigit():
                dats.append(int(i))

        end = 12 + questionLength
        
        answer = data[end:].decode()

        if dats[1] == 0:
            print("Return Code: 0 (No errors)")
            print("Message ID: " + str(dats[2]) + str(dats[3]))
            print("Question Length: " + str(questionLength) + " bytes")
            print("Answer Length: " + str(dats[6]) + str(dats[7]) + " bytes")
            print("Question: " + question)
            print("Answer: " + answer)
        elif dats[1] == 1: 
            print("Return Code: 1 (Name does not exist)")
            print("Question Length: " + str(questionLength) + " bytes")
            print("Answer Length: 0 bytes")
            print("Question: " + question)
        break
    except:
        if i == 2:
            print("Request timed out ... Exiting Program")
        else:
            print("Request timed out ...")
            print("Sending Request to " + str(ip) + ", " + str(port) + ":")

#Close the client socket
clientsocket.close()
            
