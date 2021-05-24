import socket, sys, time
print('...Client side...')
time.sleep(1)

soch = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

server_host = input('Enter server\'s IP address: ')
name = input('Enter the client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soch.connect((server_host, port))
print('Hey, you are Connected now! \n')
soch.send(name.encode())
server_name = soch.recv(1024)
server_name = server_name.decode()
print('{} has joined '.format(server_name))
print('Enter exit to leave')

while True:
    message = soch.recv(1024)
    message = message.decode()
    print(server_name, '>>', message)
    message = input(str('Me >> '))
    if message == 'exit':
        message = 'Leaving the chat room... Have a good day, Byee!!'
        soch.send(message.encode())
        print('\n')
        break
    soch.send(message.encode())

