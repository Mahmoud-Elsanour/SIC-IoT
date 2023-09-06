import socket

# Create a UDP/IPv4 socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.56.101', 999)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


while True:
    # Wait for a connection
    print('Waiting for a message')
    data, client_address = sock.recvfrom(4069)
    

    print('recieved {} bytes from {}'.format(len(data), client_address))
    print(data)

    if data:
        sent =sock.sendto(data, client_address)
        print('Sent {} bytes back to {}'.format(sent, client_address))
