import time
import rssi
#import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


interface = 'wlan1'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['dd-wrt','linksys']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.

kit = MotorKit()

for i in range(25):
        kit.stepper2.onestep(style=stepper.MICROSTEP)
        for x in range(25):
                kit.stepper1.onestep(style=stepper.MICROSTEP)
                ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
                print(ap_info)
                time.sleep(0.01)

kit.stepper1.release()
kit.stepper2.release()

