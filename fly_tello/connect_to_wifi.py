from fly_tello import FlyTello

#
# Sets the drone up to use the same WiFi network.
#
# Before running this file, you need to connect directly to the Tello EDU's ad-hoc network.
# This only needs to be run once per drone, or if the drone is reset.
#
# *NOTE*: Do not commit any changes to this file, or you will be sharing you WiFi information with the world!
#

with FlyTello(['XXX']) as fly:
    fly.set_ap_wifi(ssid='vayermakingrouter', password='0879697389')
