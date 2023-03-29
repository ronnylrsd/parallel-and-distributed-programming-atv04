# Importações importantes para o funcionamento do servidor
import socket
import threading

from tcp_client import handle_client


# Função que executa o servidor
def run_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Faz o bind do socket à porta e endereço local
    server_socket.bind(('localhost', 1234))
    # Coloca o socket em modo de escuta (listen)
    server_socket.listen(5)
    # Imprime mensagem de que o servidor está ouvindo na porta 1234
    print('Server listening on port 1234...')
    # Loop principal do servidor
    while True:
        # Aceita uma nova conexão de cliente
        client_socket, client_address = server_socket.accept()
        # Imprime mensagem de que uma nova conexão foi aceita
        print('Accepted connection from {}:{}'.format(
            client_address[0], client_address[1]))
        # Cria uma nova thread para tratar a conexão com o cliente
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket,))
        # Inicia a thread
        client_handler.start()


# Função principal que é executada quando o script é chamado
if __name__ == '__main__':
    run_server()
