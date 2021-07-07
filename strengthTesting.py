import time
import rssi
#import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import pandas as pd

df = pd.DataFrame({
'SSID':['Test'],
'Quality':['Test'],
'Signal': [100],
'Xpos': [0],
'Ypos': [0]
 })

print(df)

interface = 'wlan1'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['Tiger8']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.

kit = MotorKit()
xpos=0
ypos=0

for i in range(3):
    kit.stepper2.onestep(style=stepper.MICROSTEP)
    ypos=ypos+1
    xpos=0
    for x in range(3):
        kit.stepper1.onestep(style=stepper.MICROSTEP)
        xpos=xpos+1
        ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
        print(ap_info)
        df1 = pd.DataFrame({
        'SSID':[ap_info[0]['ssid']],
        'Quality':[ap_info[0]['quality']],
        'Signal': [ap_info[0]['signal']],
        'Xpos': [xpos],
        'Ypos': [ypos]})
        df = df.append(df1, ignore_index=True)
        time.sleep(0.01)
        for y in range(3):
            kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)

kit.stepper1.release()
kit.stepper2.release()
print(df)
