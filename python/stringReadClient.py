import socket

serverName = "127.0.0.1"
serverPort = 13000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

filename = input("파일 이름 입력: ")
clientSocket.send(filename.encode())

filedata = clientSocket.recv(1024)
print("서버 응답:", filedata.decode())

clientSocket.close()
