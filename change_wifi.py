import socket
import time
import config

tello = (config.ip, 8889)

def init_drone():

    # create upd client on PC
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as err:
        print(err)
        exit()

    try:
        # send control commands to the drone
        s.sendto(b'command', tello)
        time.sleep(5)
    except socket.error as err:
        print(err)

    return s
def land(s):
    s.sendto(b'ap vayermakingtello vayertues', tello)
    time.sleep(5)

def main():
    s = init_drone()



if __name__ == '__main__':
    main()
