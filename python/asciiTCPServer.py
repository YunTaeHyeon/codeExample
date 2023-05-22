import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("listen")

while True:
    connectionSocket, addr = serverSocket.accept()

    string = connectionSocket.recv(1024).decode()

    if string.isalpha():
        ascii_string = ' '.join(str(ord(c)) for c in string)  # convert to ASCII
        connectionSocket.send(ascii_string.encode())

    else:
        print("영어가 아닙니다")

    connectionSocket.close()