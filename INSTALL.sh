#! /bin/bash

echo
echo "[*] Installing dependencies..."

xterm -e sudo apt update
xterm -e sudo apt upgrade
xterm -e sudo apt install macchanger python python3-pip nmap

echo "Done."
echo

echo
echo "[*] Fixing permissions..."

xterm -e sudo chmod +x matool.py

echo "Done."
echo

echo
echo "Well, thats's pretty much it. You should be able now to run 'python3 matool.py'. Happy hunting!"
echo
