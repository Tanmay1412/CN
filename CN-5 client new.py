import socket
import os

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_ip = '127.0.0.1'
    server_port = 12345
    client_socket.connect((server_ip, server_port))

    # Send a message to the server
    client_socket.sendall("Hello from Client!".encode())

    # Receive a response from the server
    data = client_socket.recv(1024).decode()
    print(f"Server says: {data}")

    # ----- File Transfer Section -----
    # Ask for a file to send
    filename = input("Enter the file name to send (with extension): ")

    if os.path.exists(filename):
        # Send filename first
        client_socket.sendall(filename.encode())

        # Send the file contents
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(1024)
                if not bytes_read:
                    break
                client_socket.sendall(bytes_read)
        print("File sent successfully.")
    else:
        print("File not found!")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
