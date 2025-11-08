import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_ip = '127.0.0.1'  # Localhost for testing; replace with actual server IP in a real network
    server_port = 12345
    client_socket.connect((server_ip, server_port))

    # Send a message to the server
    client_socket.sendall("Hello from Client!".encode())

    # Receive a response from the server
    data = client_socket.recv(1024).decode()
    print(f"Server says: {data}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()

#terminal
#cd %USERPROFILE%\OneDrive\Desktop
#python CN-5client.py
