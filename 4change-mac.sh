#! /bin/bash

echo
echo "[*] Shutting down wlan0 interface..."
ifconfig wlan0 down
echo Done.

echo
echo "[*] Changing MAC address..."
macchanger -p wlan0
echo
echo Done.

echo
echo "[*] Starting up wlan0 interface..."
ifconfig wlan0 up
echo Done.

echo
