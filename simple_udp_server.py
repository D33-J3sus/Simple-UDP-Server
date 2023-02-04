import socket

localIP = "127.0.0.1"
localPort = 80
bufferSize = 1024

msgFromServer = "Test: Sending data RECEIVED"
bytesToSend = str.encode(msgFromServer)

# Create datagram socket
UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP Server up and listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Send a reply to client
    UDPServerSocket.sendto(bytesToSend, address)