from fly_tello import FlyTello

my_tellos = list()
my_tellos.append('0TQDFB9EUBG09Z')  # Replace with your Tello Serial Number


with FlyTello(my_tellos) as fly:    # Use FlyTello as a Context Manager to ensure safe landing in case of any errors
    fly.takeoff()
    fly.flip("forward")
    fly.up(20)
    fly.flip("forward")
    fly.forward(50)
    fly.up(20)
    fly.rotate_cw(90)
    fly.get_battery()
    fly.get_sdk()
    fly.rotate_ccw(90)
    fly.back(50)

    #with fly.sync_these():          # Keep the following commands in-sync, even with different commands for each Tello
    #    fly.left(30, tello=1)       # Tell just Tello1 to fly left
    #    fly.right(30, tello=2)      # At the same time, Tello2 will fly right
    #fly.flip(direction='forward')   # Flips are easy to perform via the Tello SDK
    fly.land()
