#! /bin/bash

echo
echo "[*] Installing dependencies..."

xterm -e sudo apt update
xterm -e sudo apt upgrade
xterm -e sudo apt install macchanger python python3-pip nmap nano cat

echo "Done."
echo

echo "[*] Adding a notes file..."

echo "This is your notes file. You can freely modify it at your wish using 'mnotes' while using Matool. If you accidentaly delete this, run INSTALL.sh to fix it." > matnotes.txt

echo "Done."
echo

echo "[*] Fixing permissions..."

xterm -e sudo chmod +x matool.py

echo "Done."
echo

echo "Well, thats's pretty much it. You should be able now to run 'python3 matool.py'. Happy hunting!"
echo
