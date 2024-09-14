import socket

def start_server():
    PORT = 8000
    IP = socket.gethostbyname(socket.gethostname())

    # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created.")

    #bind socket
    sock.bind(('localhost', PORT))
    print("Socket Binded.")

    #socket listen
    sock.listen(5)
    print("Socket listening...")

    connection, addr = sock.accept()
    print(f"Connected by {addr}")

    while True:
        message = connection.recv(1024)
        message = message.decode()
        print(f"Message from client: {message}")

        if message.lower() == 'stop' or message.lower() == 'exit' or not message:
            connection.send("Connection closed".encode())
            break

        response = input("Send message to client: ")
        connection.send(response.encode())

    connection.close()

if __name__ == "__main__":
    start_server()