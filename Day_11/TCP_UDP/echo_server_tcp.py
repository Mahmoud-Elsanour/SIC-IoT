import socket

# Create a TCP/IPv4 socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.56.101', 999)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # Recieve the data
        while True:
            data = connection.recv(16)
            print('recieved {!r}'.format(data))
            if data:
                print('Sending data back!!')
                connection.sendall(data)
            else:
                print('No data from', client_address)
                break

    finally:
        print('Closing the connection')
        connection.close()
