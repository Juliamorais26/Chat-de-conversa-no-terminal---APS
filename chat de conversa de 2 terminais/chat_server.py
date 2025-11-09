import socket #comunicação de rede (TCP/IP)
from cryptography.fernet import Fernet #criptografia simétrica
import threading # permite executar envio e recebimento ao mesmo tempo

# Carrega chave secreta
with open("chave.key", "rb") as f:
    key = f.read()
cipher = Fernet(key) # Cria o objeto Fernet para cifrar/decifrar mensagens com a chave lida

# Configuração do servidor
# Pede ao usuário o IP do servidor
HOST = "0.0.0.0"  
PORT = 5000

# Cria um socket TCP (IPv4)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tenta conectar ao servidor
server.bind((HOST, PORT)) 
server.listen()

print(f" Servidor (Costa brasileira) aguardando conexão em {HOST}:{PORT}...")

conn, addr = server.accept() 
print(f" Conectado com {addr}")

# Função para receber mensagens
def receber():
    while True:
        try:
            dados = conn.recv(2048) #Recebe mensagens criptografadas
            if not dados:
                break
            mensagem = cipher.decrypt(dados).decode()  # Decifra e converte de bytes para texto
            print(f"\n Costa brasileira: {mensagem}") # Exibe a mensagem recebida
        except Exception:
            print("\n Erro ao decifrar mensagem ou conexão encerrada.")
            break

# Função para enviar mensagens
def enviar():
    while True:
        msg = input("Navio: ")
        if msg.lower() == "sair":
            conn.close()
            break
        msg_cifrada = cipher.encrypt(msg.encode())  # Converte a string para bytes e criptografa
        conn.send(msg_cifrada) # Envia a mensagem cifrada

# Threads para enviar e receber simultaneamente
threading.Thread(target=receber, daemon=True).start()
enviar()
