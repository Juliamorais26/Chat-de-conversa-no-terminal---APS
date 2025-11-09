import socket #comunicação de rede (TCP/IP)
from cryptography.fernet import Fernet #criptografia simétrica
import threading # permite executar envio e recebimento ao mesmo tempo

# Carrega a mesma chave secreta
with open("chave.key", "rb") as f:
    key = f.read()
cipher = Fernet(key)  # Cria o objeto Fernet para cifrar/decifrar mensagens com a chave lida

# Configuração do usuário(Costa brasileira)
HOST = input("Digite o IP do servidor (Usuário Costa brasileira): ")
PORT = 5000

# Cria um socket TCP (IPv4)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tenta conectar ao servidor
client.connect((HOST, PORT))

print(" Conectado ao servidor! Agora você pode conversar.\n")

# Função para receber mensagens
def receber():
    while True:
        try:
            dados = client.recv(2048)
            if not dados:
                break
            mensagem = cipher.decrypt(dados).decode()  # Decifra e converte de bytes para texto
            print(f"\n Navio: {mensagem}")  # Exibe a mensagem recebida
        except Exception:
            print("\n Erro ao decifrar mensagem ou conexão encerrada.")
            break

# Função para enviar mensagens
def enviar():
    while True:
        msg = input("Costa brasileira: ")
        if msg.lower() == "sair":
            client.close()
            break
        msg_cifrada = cipher.encrypt(msg.encode()) # Converte a string para bytes e criptografa
        client.send(msg_cifrada) # Envia a mensagem cifrada

# Threads para enviar e receber simultaneamente
threading.Thread(target=receber, daemon=True).start()
enviar()
