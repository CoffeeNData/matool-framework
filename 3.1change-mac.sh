#! /bin/bash

echo
echo "[*] Shutting down wlan0 interface..."
ifconfig wlan0 down
echo Done.
