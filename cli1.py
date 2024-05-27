import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))

    # Ask the user to enter their name
    name = input("Enter your name: ")
    client.send(name.encode())
    
    while True:
        message = input("Enter message (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client.send(message.encode())
        response = client.recv(1024)
        print(f"Server response: {response.decode()}")

    client.close()

if __name__ == "__main__":
    start_client()
