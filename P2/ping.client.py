'''
Programming and Language Version: Python3 3.8.6
Testing Environment: 
    OS: Ubuntu 20.10 x86_64
    Command Lines: 
        1. To simulate a running connection: 
            a. Compile server.py using python3 server.py 127.0.0.1 12000
            b. Compile client.py using python3 server.py 127.0.0.1 12000
'''
import sys
import socket
import time
import struct

# Get the server hostname, port and data length as command line arguments
pingCount = 0
totalTime = 0
timeList = []
host = sys.argv[1]
port = int(sys.argv[2])

# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Default socket timeout
clientsocket.settimeout(1)

# Receive the server response and send data to server
print("Pinging  " + str(host) + ", " + str(port) + ":")
for i in range(10):
    try: 
        initialTime = time.time()
        pingCount += 1
        clientsocket.sendto(struct.pack('<i', pingCount),(host, port))
        dataEcho, address = clientsocket.recvfrom(2)
        endTime = time.time()
        print("Ping message number " + str(pingCount) + " RTT: " 
                        + str(round(endTime - initialTime, 6)) + " secs")
        totalTime =+ (endTime - initialTime)
        timeList.append(endTime - initialTime)
    except:
        print("Ping message number " + str(pingCount) + " timed out")

timeList.sort()
print("Statistics:")
print(str(pingCount) + " packets transmitted, " + str(len(timeList)) + " received, " 
                            + str(round(((pingCount - len(timeList)) / 10) * 100, 0))  
                                                                     + "% packet loss")

if timeList:
    print("Min/Max/AV RTT = " + str(round(timeList[0], 6)) + " / " 
            + str(round(timeList[-1], 6)) + " / " + str(round(totalTime/10, 6)))


    
#Close the client socket
clientsocket.close()
