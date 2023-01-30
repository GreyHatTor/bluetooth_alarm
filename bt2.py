import subprocess
import pygame
import time

#This is a code to get a beep sound constantly if the bluetooth device is disconnected from this device.
#print("1st") - uncomment to check outputs
print("-"*100)
print('''

 ▄▄▄▄   ▄▄▄█████▓    ▄▄▄       ██▓    ▄▄▄       ██▀███   ███▄ ▄███▓
▓█████▄ ▓  ██▒ ▓▒   ▒████▄    ▓██▒   ▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒
▒██▒ ▄██▒ ▓██░ ▒░   ▒██  ▀█▄  ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░
▒██░█▀  ░ ▓██▓ ░    ░██▄▄▄▄██ ▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██ 
░▓█  ▀█▓  ▒██▒ ░     ▓█   ▓██▒░██████▒▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒
░▒▓███▀▒  ▒ ░░       ▒▒   ▓▒█░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░
▒░▒   ░     ░         ▒   ▒▒ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░
 ░    ░   ░           ░   ▒     ░ ░    ░   ▒     ░░   ░ ░      ░   
 ░                        ░  ░    ░  ░     ░  ░   ░            ░   
      ░                                                            

						# Developed by	: GreyHatTor
						# Credits	: Aash
''')

print("-"* 100)
print("Started and Running...")
	
def connected():
	result = subprocess.check_output("hcitool con", shell=True)
	# print("2nd") - uncomment to check outputs
	if "handle" in result.decode("utf-8"):
		print("Bluetooth device connected")
	else:
		print("No bluetooth devices connected")
		pygame.init()
		pygame.mixer.Sound("beep.wav").play()

while True:
	connected()
	time.sleep(1)
