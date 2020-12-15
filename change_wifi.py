from fly_tello import FlyTello
import config

my_tellos = list()
my_tellos.append(config.tello_serial_number) 

with FlyTello(my_tellos) as fly:
    fly.set_ap_wifi(config.ssid, config.passwd)
