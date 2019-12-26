import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 8000

server_socket.bind((host, port))
server_socket.listen(10)

while True:
    clientsocket, addr = server_socket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Thank you for connecting' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
