import socket

host = 'localhost'
port = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Servidor ouvindo em {host}:{port}...")

print("Aguardando conexão")
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

while True:

    mensagem = conn.recv(1024).decode()
    if not mensagem or mensagem.lower() == 'sair':
        print("Cliente encerrou a conversa.")
        break
        
    print("Cliente:", mensagem)

    resposta = input("Você: ")
    if resposta.lower() == 'sair':
        conn.send(resposta.encode())
        print("Encerrando o chat...")
        break
    conn.send(resposta.encode())

conn.close()

