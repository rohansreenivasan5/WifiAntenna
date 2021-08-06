import rssi

interface = 'wlan0'
rssi_scanner = rssi.RSSI_Scan(interface)

homeSSID = 'test'
mac = 'ff:ff:ff:ff'

scan = rssi_scanner.getRawNetworkScan()


