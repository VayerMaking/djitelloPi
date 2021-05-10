import socket
import time

tello_address = ('192.168.10.1', 8889)

# Create a UDP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind to a local port on our machine
sock.bind(('', 9000))

# send messages
def send(message):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

# recive messages
def receive():
  try:
    response, ip_address = sock.recvfrom(128)
    print("Received message: " + response.decode(encoding='utf-8') + " from Tello with IP: " + str(ip_address))
  except Exception as e:
    print("Error receiving: " + str(e))


# start reciving commands on the Tello
send("command")

# receive a response
receive()

time.sleep(3)

send("streamoff")

receive()

# close the UDP socket
sock.close()
