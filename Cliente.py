import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost' , 7777))
print('Conectado!\n')

namefile = str(input('Arquivo>'))

cliente.send(namefile.encode())

with open (namefile, 'wb') as file:
    while 1:
        data = cliente.recv(1000000)
        if not data:
            break
        file.write(data)
print(f'{namefile}recebido\n')