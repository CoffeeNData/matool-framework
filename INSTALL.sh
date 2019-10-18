#! /bin/bash

echo
echo "[*] Installing dependencies..."

sudo apt-get update && apt get upgrade
sudo apt-get install macchanger python python3-pip

echo "Done."
echo

echo
echo "[*] Installing requirements..."

pip3 install os

echo "Done."

echo
echo "[*] Fixing permissions..."

sudo chmod +x matool.py

echo "Done."
echo

echo
echo "Well, thats's pretty much it. You should be able now to run 'python3 matool.py'. Happy hunting!"
echo
