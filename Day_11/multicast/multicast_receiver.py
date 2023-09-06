import socket

import struct



multicast_group = '224.10.10.10'

server_address = ('', 10000)



# Create a socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# Bind address

sock.bind(server_address)



# Add the socket to the multicast group

group = socket.inet_aton(multicast_group)

mreq = struct.pack('4sL', group, socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)



# Receive respond

while True:

    print('\nWaiting to receive message')

    data, address = sock.recvfrom(1024)



    print('Received {} bytes from {}'.format(len(data), address))

    print(data)



    # Send ACK

    print('Sending acknowledgment to', address)

    sock.sendto(b'ack', address)
