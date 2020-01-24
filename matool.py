#! /bin/python3
from os import system

"""
FUNCTIONS
"""
def banner():
	print()
	print(" _____       _              __      ")
	print("|     | ___ | |_  ___  ___ |  |     ")
	print("| | | || .'||  _|| . || . ||  |__   ")
	print("|_|_|_||__,||_|  |___||___||_____|  ")
	print()

def customChange(mac):
	print("[*] Shutting down wlan0...")
	system("sudo ifconfig wlan0 down")
	print("Done.")
	print()
	print("[*] Changing MAC to " + str(mac) + "...")
	system("sudo macchanger -m " + str(mac) + " wlan0")
	print("Done.")
	print()
	print("[*] Shutting up wlan0...")
	system("sudo ifconfig wlan0 up")
	print("Done.")
	print()

def personalChange():
	print("[*] Shutting down wlan0...")
	system("sudo ifconfig wlan0 down")
	print("Done.")
	print()
	print("[*] Changing to your default MAC...")
	system("sudo macchanger -p wlan0")
	print("Done.")
	print()
	print("[*] Shutting up wlan0...")
	system("sudo ifconfig wlan0 up")
	print("Done.")
	print()

def randomChange():
	print("[*] Shutting down wlan0...")
	system("sudo ifconfig wlan0 down")
	print("Done.")
	print()
	print("[*] Changing to a random MAC...")
	system("sudo macchanger -r wlan0")
	print("Done.")
	print()
	print("[*] Shutting up wlan0...")
	system("sudo ifconfig wlan0 up")
	print("Done.")
	print()

def help():
	print("Available options:")
	print("")
	print("exit      -  Exits. Also works with 'quit'")
	print("cmac      -  Changes to a custom MAC")
	print("pmac      -  Changes to your permanent MAC")
	print("smac      -  Shows current MAC address")
	print("rmac      -  Changes to a random MAC address")
	print("help      -  Shows this list")
	print("ping      -  Pings Google")
	print("scan      -  Scans the local network. Will not work with arguments")
	print("clear     -  Clears the screen")
	print("rnotes    -  Read the notes file")
	print("mnotes    -  Modifies the notes file.")
	print("             You should write MAC addresses you usually use")

	#The notes file is called "matnotes.txt"
def read_notes():
	print()
	print("<-------------BEGIN OF NOTES------------->")
	system("cat ~/.matool-documents/matnotes.txt")
	print("<--------------END OF NOTES-------------->")
	print()

def modify_notes():
	print("[*] Opening the notes file...")
	system("nano ~/.matool-documents/matnotes.txt")
	print("Done.")
	print()

"""
MAIN PROGRAM
"""

banner()
help()
print()

while True:

	option=input("Option > ")

	if option=="quit" or option=="exit":
		break
	elif option=="cmac":
		custom_mac=input("New MAC > ")
		print()
		customChange(custom_mac)
	elif option=="pmac":
		personalChange()
		print("")
	elif option=="help":
		print()
		help()
		print("")
	elif option=="clear":
		system("clear")
	elif option=="ping":
		system("ping -c 3 google.com")
		print()
	elif option=="scan":
		scanTarget=input("RHOSTS > ")
		system("sudo nmap -F " + str(scanTarget))
	elif option=="smac":
		system("macchanger -s wlan0")
		print()
	elif option=="":
		pass
	elif option=="rnotes":
		read_notes()
	elif option=="mnotes":
		modify_notes()
	elif option=="rmac":
		randomChange()
	else:
		print()
		print("[!] Unknown command. Write 'help' for a list of available tools")
		print()

print()
print("[!] Exited successfully")
quit()
