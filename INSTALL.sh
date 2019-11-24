#! /bin/bash

echo
echo "[*] Installing dependencies..."

sudo apt update && apt upgrade
sudo apt install macchanger python python3-pip nmap

echo "Done."
echo

echo
echo "[*] Installing Python requirements..."

pip3 install python-nmap

echo "Done."

echo
echo "[*] Fixing permissions..."

sudo chmod +x matool.py

echo "Done."
echo

echo
echo "Well, thats's pretty much it. You should be able now to run 'python3 matool.py'. Happy hunting!"
echo
