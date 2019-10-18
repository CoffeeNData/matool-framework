from os import system

print("")
print("Welcome to the MAC Address Assisted Toolkit - Matool-")
print("")


def help():
	print("Available options:")
	print("")
	print("exit      -  Exits. Also works with 'quit'")
	print("cmac      -  Changes to a custom MAC")
	print("pmac      -  Changes to your permanent MAC")
	print("smac      -  Shows current MAC address")
	print("help      -  Shows this list")
	print("ping      -  Runs ping on google.com")
	print("scan      -  Scans the local network")
	print("clear     -  Clears the screen")

help()

while True:

	mactochangeto=input("\nOption > ")

	if mactochangeto=="quit" or mactochangeto=="exit":
		break
	elif mactochangeto=="cmac":

		custom_mac=input("Write the new MAC address: ")
	
		system("bash 3.1change-mac")
		print("[*] Changing MAC address...")
		print("")
		system("macchanger -m " + custom_mac + " wlan0")
		print("")
		print("Done.")

	elif mactochangeto=="pmac":
		system("bash 4change-mac.sh")
	elif mactochangeto=="help":
		help()
	elif mactochangeto=="clear":
		system("clear")
	elif mactochangeto=="ping":
		system("ping -c 3 google.com")
	elif mactochangeto=="scan":
		print("")
		scanner=input("Write the IP range, or a specific IP: ")
		system("nmap " + scanner)
	elif mactochangeto=="smac":
		system("macchanger -s wlan0")
	else:
		help()

print("[*] Quitting...")
