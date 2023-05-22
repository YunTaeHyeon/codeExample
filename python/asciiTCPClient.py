import socket

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

string = input("문자열 입력: ")
clientSocket.send(string.encode())

modifiedstring = clientSocket.recv(1024)
print("변환 값:", modifiedstring.decode())

clientSocket.close()

