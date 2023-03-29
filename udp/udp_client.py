#Rodar depois do udp_server.py
import socket
#Define o endereço IP local e a porta do servidor
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
#Define a mensagem que será enviada ao servidor
MESSAGE = "Hello, Server!"
#Cria um objeto de socket UDP
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
#Envia a mensagem definida anteriormente ao servidor no endereço e porta especificados. O método encode() é usado para converter a mensagem para bytes antes de enviá-la.