# Importa a classe Fernet da biblioteca cryptography.
from cryptography.fernet import Fernet

# Gera uma chave aleatória de 32 bytes codificada.
key = Fernet.generate_key()

# Abre (ou cria) um arquivo chamado "chave.key" no modo de escrita binária ("wb").
# Em seguida, grava dentro dele a chave gerada.
with open("chave.key", "wb") as f:
    f.write(key)

print("Chave gerada e salva em 'chave.key'.")
