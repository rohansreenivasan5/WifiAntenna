#pip install rssi
#python rssi.py

import rssi

interface = 'wlp1s0'
rssi_scanner = rssi.RSSI_Scan(interface)

#change ssid here
ssids = ['dd-wrt','linksys']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.
ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

print(ap_info)
