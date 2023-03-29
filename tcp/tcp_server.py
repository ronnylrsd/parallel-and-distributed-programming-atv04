import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    response = 'Hello, client! Your message was: ' + request.decode()
    client_socket.send(response.encode())
    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(5)
    print('Server listening on port 1234...')
    while True:
        client_socket, client_address = server_socket.accept()
        print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    run_server()
