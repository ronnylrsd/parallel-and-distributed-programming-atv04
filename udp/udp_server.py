#Rodar antes do udp_client.py 
import socket
#Define o endereço IP e a porta do servidor
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
#Cria um objeto de socket UDP
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
#Faz o "bind"(associação) do endereço IP e da porta do servidor com o objeto de socket
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:", data.decode())
#Aguarda indefinidamente por mensagens recebidas no objeto de socket sock. Quando uma mensagem é recebida, ela é armazenada na variável data e o endereço do remetente é armazenado na variável addr. Então, a mensagem recebida é exibida na tela.
# 1024 é o tamanho máximo da mensagem que pode ser recebida. Se a mensagem recebida for maior do que esse tamanho, ela será truncada.

