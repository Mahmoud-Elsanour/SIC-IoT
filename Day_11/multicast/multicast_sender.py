import socket
import struct

message = b'IMPORTANT DATA!!'
multicast_group = ('224.10.10.10', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set timeout
sock.settimeout(1)

# Set time-to-live
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send data
try:
    print('Sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)

    # Look for responce
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(1024)
        except socket.timeout:
            print('Timed out, no more responces')
            break
        else:
            print('recieved {!r} from {}'.format(data, server))

finally:
    print('Closing socket')
    sock.close()
