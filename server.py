import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"{username}: {message}")
                broadcast(f"{username}: {message}", client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

def handle_new_connection(client_socket):
    username = client_socket.recv(1024).decode('utf-8')
    clients.append(client_socket)
    print(f"{username} has joined the chat")
    broadcast(f"{username} has joined the chat", client_socket)
    threading.Thread(target=handle_client, args=(client_socket, username)).start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5557))  # Changed port to 5556
server.listen(5)
clients = []

print("Server started...")
while True:
    client_socket, addr = server.accept()
    threading.Thread(target=handle_new_connection, args=(client_socket,)).start()
