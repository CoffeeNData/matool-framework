#! /bin/bash
echo "[*] Installing dependencies..."
sudo apt update
sudo apt upgrade
sudo apt install macchanger python python3-pip nmap nano cat
echo "Done."

echo

echo "[*] Adding a notes file..."
mkdir ~/.matool-documents
echo "This is your notes file. You can freely modify it at your wish using 'mnotes' while using Matool. If you accidentaly delete this, run INSTALL.sh to fix it." > ~/.matool-documents/matnotes.txt
echo "Done."

echo

echo "[*] Copying to '/bin' folder..."
sudo cp ./matool.py /bin/matool
echo Done

echo

echo "[*] Fixing permissions..."
sudo chmod +x /bin/matool
echo "Done."

echo

echo "Well, thats's pretty much it. You should be able now to run 'matool'. Happy hunting!"
echo
