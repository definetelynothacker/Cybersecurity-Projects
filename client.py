import socket

def start_client(): 
    sock = socket.socket()

    PORT = 8000
    local = '127.0.0.1'

    sock.connect((local, PORT))

    while True:
        message = input("Send message to server: ")
        sock.send(message.encode())

        if message.lower() == 'stop' or message.lower() == 'exit' or not message:
            print("Connection closed")
            break

        response = sock.recv(1024)
        print(f"Received from server: {response.decode()}")

    sock.close()

if __name__ == "__main__":
    start_client()