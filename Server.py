import socket
import time

serverPort = 4000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to recieve")
while True: 
        connectionSocket, addr = serverSocket.accept()
        connectionSocket.settimeout(15)
        userInput = "Got connection from", addr
        print(userInput)
        connectionSocket.send(userInput.encode())
        while len(userInput):
            try:
                userInput = connectionSocket.recv(1024).decode()
                print("userInput = ", userInput)
                if userInput == 'TIME':
                    now = "The time is " + time.ctime()
                    connectionSocket.send(now.encode())
                    userInput = ''
                if userInput == 'EXIT':
                    print("Connection from", addr, "Disconnected")
                    end = "Goobye, Thanks for using the server"
                    connectionSocket.send(end.encode())
                    connectionSocket.close()
                else:
                    error = "Invalid Command"
                    connectionSocket.send(error.encode())
            except socket.timeout:
                print("Connection from", addr, "Got Timeout")
                timedOut = "Timed Out"
                connectionSocket.send(timedOut.encode())
                connectionSocket.close()
                break;        
        connectionSocket.close()
serverSocket.close();


