import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific IP address and port
    server_ip = '127.0.0.1'  # Localhost for testing; replace with actual server IP in a real network
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

    # Close the connection
    conn.close()

if __name__ == "__main__":
    start_server()

# terminal
#cd %USERPROFILE%\OneDrive\Desktop
#python CN-5server.py
