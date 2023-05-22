import socket

serverPort = 13000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("listen")

while True:
    connectionSocket, addr = serverSocket.accept()
    filename = connectionSocket.recv(1024).decode()

    try:
        with open(filename, 'r') as file:
            data = file.read()
        connectionSocket.send(data.encode())
    except FileNotFoundError:
        connectionSocket.send("파일이 존재하지 않습니다".encode())

    connectionSocket.close()