#run these in kali command line
#apt install python-scapy
#iw wlan0 interface add mon0 type monitor
#ifconfig mon0 up

from scapy.all import *

def PacketHandler(pkt) :
  if pkt.haslayer(Dot11) :
    if pkt.type == 0 and pkt.subtype == 8 :
      if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        try:
            extra = pkt.notdecoded
            rssi = -(256-ord(extra[-4:-3]))
        except:
            rssi = -100
        print "WiFi signal strength:", rssi, "dBm of", pkt.addr2, pkt.info

sniff(iface="mon0", prn = PacketHandler)
