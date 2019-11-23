import nmap
import sys
from time import sleep

scanCount=0
currenthost= ""

print()
host= '192.168.5.1/24'
print()

print("[*] Scanning...")
scanner= nmap.PortScanner()
scan= scanner.scan(host, arguments='-F')
print("Done.")

print()
print("Listing...")
print()
while scanCount<255:

    scanCount=scanCount+1
    currenthost= '192.168.5.'+str(scanCount)
    try:
        ip=str(scan['scan'][currenthost]['addresses']['ipv4'])
        mac=str(scan['scan'][currenthost]['addresses']['mac'])
        provider=str(scan['scan'][currenthost]['vendor'][mac])

        print(ip+ " > " + mac + " (" + provider + ")")
        print()

    except:
        pass