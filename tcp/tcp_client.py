# Importações importantes para o funcionamento do servidor
import socket
import threading


# Função que trata cada conexão de cliente
def handle_client(client_socket):
    # Recebe a mensagem enviada pelo cliente
    request = client_socket.recv(1024)
    # Cria uma resposta para enviar de volta ao cliente
    response = 'Hello, client! Your message was: ' + request.decode()
    # Envia a resposta de volta ao cliente
    client_socket.send(response.encode())
    # Fecha a conexão com o cliente
    client_socket.close()
