import socket

def udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Change to your server's IP and port if necessary
    server_socket.bind(server_address)

    print(f"Server listening on {server_address}...")
    
    # First, receive the file name
    file_name, client_address = server_socket.recvfrom(1024)
    file_name = file_name.decode('utf-8')
    print(f"Receiving file: {file_name} from {client_address}")
    
    # Now receive the file data
    with open(file_name, 'wb') as f:
        while True:
            data, client_address = server_socket.recvfrom(4096)
            if data == b"END":  # Special end marker for end of file transfer
                break
            f.write(data)
    print(f"File {file_name} received successfully.")

if __name__ == "__main__":
    udp_server()


#cd "C:\Users\Akshay\OneDrive\Desktop"
#python "CN PRAC6 server.py"