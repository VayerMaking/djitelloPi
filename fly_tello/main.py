from fly_tello import FlyTello

my_tellos = list()
my_tellos.append('0TQDFB9EUBG09Z')  # serial number

with FlyTello(my_tellos) as fly:    # safe landing if errors occur when using a Context Manager
    fly.takeoff()

    fly.flip("forward")
    fly.up(20)
    fly.flip("forward")
    fly.forward(50)
    fly.up(20)              # execute a series of commands to move the drone
    fly.rotate_cw(90)
    fly.get_battery()
    fly.get_sdk()
    fly.rotate_ccw(90)
    fly.back(50)

    fly.land()
