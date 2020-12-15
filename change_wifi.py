from fly_tello import FlyTello
import config

my_tellos = list()
my_tellos.append(config.tello_serial_number) 

<<<<<<< HEAD
with FlyTello(my_tellos) as fly:
    fly.set_ap_wifi(config.ssid, config.passwd)
=======
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
>>>>>>> 26e88d6832230fbdfb47bcf12864b6de12b49a60
