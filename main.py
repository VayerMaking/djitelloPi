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
        s.sendto('command', tello)
        time.sleep(5)
    except socket.error as err:
        print(err)

    return s

def takeoff(s):
    s.sendto('takeoff', tello)
    time.sleep(10)

def rotate90(s):
    s.sendto('cw 90', tello)
    time.sleep(10)

def flip_left(s):
    s.sendto('flip l', tello)
    time.sleep(10)

def land(s):
    s.sendto('land', tello)
    time.sleep(5)

def main():
    s = init_drone()

    takeoff(s)

    rotate90(s)

    #flip_left(s)

    land(s)

if __name__ == '__main__':
    main()
