import socket
import os

def udp_client(file_path):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)  # Change to server's IP and port if necessary

    # Get the file name from the file path
    file_name = os.path.basename(file_path)
    
    # Send the file name first
    client_socket.sendto(file_name.encode('utf-8'), server_address)
    
    # Now send the file data in chunks
    with open(file_path, 'rb') as f:
        while True:
            bytes_read = f.read(4096)  # Read the file in chunks of 4096 bytes
            if not bytes_read:
                break
            client_socket.sendto(bytes_read, server_address)
    
    # Send an "END" message to indicate the end of the file transfer
    client_socket.sendto(b"END", server_address)
    print(f"File {file_name} sent successfully.")

if __name__ == "__main__":
    # Replace with the full path of the file you want to send (script, text, audio, video)
    file_path = r"C:\Users\HP\OneDrive\Desktop\CNPract\hi.txt"# e.g., "/path/to/yourfile.txt", "/path/to/yourfile.mp3"
    udp_client(file_path)


#cd "C:\Users\Akshay\OneDrive\Desktop"
# python "CN PRAC6 client.py"
# add hi.txt file in line no.29