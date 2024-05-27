import socket
import threading

def handle_client(client_socket):
    # Receive and store the client's name
    client_name = client_socket.recv(1024).decode()
    print(f"Connected client: {client_name}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received message from {client_name}: {data.decode()}")
        client_socket.send("Message received".encode())
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8888))
    server.listen(5)
    print("Server listening on port 8888")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
