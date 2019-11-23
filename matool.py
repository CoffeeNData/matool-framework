from os import system
import nmap

print("")
print("Welcome to the MAC Address Assisted Toolkit - Matool-")
print("")

def customChange(mac):
	print("[*] Shutting down wlan0...")
	system("ifconfig wlan0 down")
	print("Done.")

	print()

	print("[*] Changing MAC to " + str(mac) + "...")
	system("macchanger -m " + str(mac) + " wlan0")
	print("Done.")

	print()

	print("[*] Shutting up wlan0...")
	system("ifconfig wlan0 up")
	print("Done.")
	print()

def personalChange():
	print("[*] Shutting down wlan0...")
	system("ifconfig wlan0 down")
	print("Done.")

	print()

	print("[*] Changing to default MAC...")
	system("macchanger -p wlan0")
	print("Done.")

	print()

	print("[*] Shutting up wlan0...")
	system("ifconfig wlan0 up")
	print("Done.")
	print()




def help():
	print("Available options:")
	print("")
	print("exit      -  Exits. Also works with 'quit'")
	print("cmac      -  Changes to a custom MAC")
	print("pmac      -  Changes to your permanent MAC")
	print("smac      -  Shows current MAC address")
	print("help      -  Shows this list")
	print("ping      -  Pings Google")
	print("scan      -  Scans the local network. Will not work with arguments")
	print("clear     -  Clears the screen")

help()

while True:

	option=input("Option > ")

	if option=="quit" or option=="exit":
		break
	elif option=="cmac":
		custom_mac=input("New MAC >  ")
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
		system('python3 scanner.py')
	elif option=="smac":
		system("macchanger -s wlan0")
		print()
	else:
		pass

print("[*] Quitting...")