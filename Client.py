from socket import *
serverName = 'localhost'
serverPort = 4000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
serverResponse = clientSocket.recv(1024)
print(serverResponse.decode())
while True:
    clientInput = input("enter the server command: ")
    clientSocket.send(clientInput.encode())
    serverResponse = clientSocket.recv(1024)
    print(serverResponse.decode())
clientSocket.close

