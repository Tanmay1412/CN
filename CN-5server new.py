import socket
import os

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port
    server_ip = '127.0.0.1'
    server_port = 12345
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {server_ip}:{server_port}...")

    # Accept a connection
    conn, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive a message from the client
    data = conn.recv(1024).decode()
    print(f"Client says: {data}")

    # Respond with "Hello"
    conn.sendall("Hello from Server!".encode())

    # ----- File Transfer Section -----
    # Receive file name
    filename = conn.recv(1024).decode()
    print(f"Receiving file: {filename}")

    # Open a file to save incoming data
    with open("received_" + filename, "wb") as f:
        while True:
            bytes_read = conn.recv(1024)
            if not bytes_read:
                # No more data, file transfer done
                break
            f.write(bytes_read)
    print(f"File received successfully as received_{filename}")

    # Close the connection
    conn.close()
    server_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_server()
