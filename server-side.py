import socket
import sys
import time

print('Setting up the server')
time.sleep(1)

soc = socket.socket()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = 1234
soc.bind((hostname, port))
print(hostname, '({})'.format(ip))
name = input('Enter the name: ')
soc.listen(1)

print('Waiting for incoming connections...')
connection, addr = soc.accept()

print('Received connection from ', addr[0], '{',addr[1],'}/n')
print('Connection established from: {}, ({})'.format(addr[0], addr[0]))

client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected')
print('Press exit to leave the chat room')
connection.send(name.encode())

while True:
    message = input('Me >> ')
    if message=='exit':
        message = 'Leaving the chat. Have a good day, Byee!'
        connection.send(message.encode())
        print('\n')
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client_name, '>>', message)
