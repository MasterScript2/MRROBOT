import os
import git
import time
import colorama
import random
from colorama import Fore
from time import sleep

RED = Fore.RED
BLUE = Fore.BLUE
WHITE = Fore.WHITE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW

#path = "write the path: "

class System_funtions:
	clear = "clear"
class Numbers:
	number_one = (RED+"<"+YELLOW+"1"+RED+">"+WHITE)
	number_two = (RED+"<"+YELLOW+"2"+RED+">"+WHITE)
	number_three = (RED+"<"+YELLOW+"3"+RED+">"+WHITE)
	number_four = (RED+"<"+YELLOW+"4"+RED+">"+WHITE)
	number_five = (RED+"<"+YELLOW+"5"+RED+">"+WHITE)
	number_six = (RED+"<"+YELLOW+"6"+RED+">"+WHITE)
	number_seven = (RED+"<"+YELLOW+"7"+RED+">"+WHITE)
	number_eight = (RED+"<"+YELLOW+"8"+RED+">"+WHITE)
	number_nine = (RED+"<"+YELLOW+"9"+RED+">"+WHITE)
	number_ten = (RED+"<"+YELLOW+"10"+RED+">"+WHITE)
	number_none = (RED+"<"+YELLOW+"00"+RED+">"+WHITE)
class Lists:
	information = ["nmap", "dmitry", "dnsenum", "sherlock"]
	explotation = ["MetasplotFramework", "SET", "msfvenom"]
	maintaing = ["proxychains"]
	password = ["hydra", "medusa", "Ncrack", "jonh", "cupp", "crunch"]
	wireless = ["reaver", "wifite", "wifite2", "aircrack-ng"]
	sniff = ["bettercap", "wireshark", "macchanger"]
	back = ["back"]
	principal = [f"\n{Numbers.number_one} Information Gathering", f"{Numbers.number_two} Explotations Tools", f"{Numbers.number_three  } Maintaing Access", f"{Numbers.number_four} Passwords Attacks", f"{Numbers.number_five} wireless pentesting", f"{Numbers.number_six} sniffing&&spoffing", f"{Numbers.number_none} exit"]
class Banners:
	ban_1 = 'toilet "MR ROBOT" --filter border'
	ban_2 = 'toilet "MR ROBOT" --filter metal'
	ban_3 = 'toilet -f pagga MRROBOT'
randoms_banners = random.choice([Banners.ban_1, Banners.ban_2, Banners.ban_3])

os.system(System_funtions.clear)
os.system(randoms_banners)
print(RED+"creator: "+YELLOW+"@MasterScript2")
for princ in Lists.principal:
	print(princ)
	sleep(0.2)
user = int(input(BLUE+"===> "+RED))
if user == 1:
	os.system(System_funtions.clear)
	os.system(randoms_banners)
	print(Numbers.number_one, Lists.information[0], "\n"+Numbers.number_two, Lists.information[1], "\n"+Numbers.number_three, Lists.information[2], "\n"+Numbers.number_four, Lists.information[3], "\n"+Numbers.number_none, Lists.back[0])
	Gathering = int(input(BLUE+"===> "+RED))
	if Gathering == 1:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing nmap...")
		time.sleep(3)
		os.system("apt -y install nmap")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif Gathering == 2:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing dmitry...")
		time.sleep(3)
		os.system("apt -y install dmitry")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif Gathering == 3:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing dnsenum...")
		time.sleep(3)
		os.system("apt -y install dnsenum")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif Gathering == 4:
		rute_sherlock = input(RED+"Write the path: "+BLUE)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Connecting with https://github.com ...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Starting cloning...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"cloning https://github.com/sherlock-project/sherlock")
		time.sleep(3)
		git.Git(f"{rute_sherlock}").clone("https://github.com/sherlock-project/sherlock")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+f"Installation completed, saved in {rute_sherlock} wait...")
		time.sleep(5)
		os.system("python3 MRROBOT.py")
	elif Gathering == 00:
		os.system("python3 MRROBOT.py")
	else:
		print(RED+"error, fatal !!!, choose a correct option")
		time.sleep(3)
		os.system("python3 MRROBOT.py")
elif user == 2:
	os.system(System_funtions.clear)
	os.system(randoms_banners)
	print("\n"+Numbers.number_one, Lists.explotation[0], "\n"+Numbers.number_two, Lists.explotation[1], "\n"+Numbers.number_none, Lists.back[0])
	explot = int(input(BLUE+"===> "+RED))
	if explot == 1:
		rute_meta = input("Write the path: ")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Connecting with https://github.com ...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Starting cloning...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"cloning https://github.com/rapid7/metasploit-framework")
		time.sleep(3)
		git.Git(f"{rute_meta}").clone("https://github.com/rapid7/metasploit-framework")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+f"Installation completed, saved in {rute_meta} wait...")
		time.sleep(5)
		os.system("python3 MRROBOT.py")
	elif explot == 2:
		rute_set = input("Write the path: ")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Connecting with https://github.com ...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Starting cloning...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"cloning https://github.com/trustedsec/social-engineer-toolkit")
		time.sleep(3)
		git.Git(f"{rute_meta}").clone("https://github.com/trustedsec/social-engineer-toolkit")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+f"Installation completed, saved in {rute_meta} wait...")
		time.sleep(5)
		os.system("python3 MRROBOT.py")
	elif explot == 00:
		os.system("python3 MRROBOT.py")
	else:
		print(RED+"error, fatal !!!, choose a correct option")
		time.sleep(3)
		os.system("python3 MRROBOT.py")
elif user == 3:
	os.system(System_funtions.clear)
	os.system(randoms_banners)
	print("\n"+Numbers.number_one, Lists.maintaing[0], "\n"+Numbers.number_none, Lists.back[0])
	main = int(input(BLUE+"===> "+RED))
	if main == 1:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing proxychains...")
		time.sleep(3)
		os.system("apt -y install proxychains")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif main == 00:
		os.system("python3 MRROBOT.py")
	else:
		print(RED+"error, fatal !!!, choose a correct option")
		time.sleep(3)
		os.system("python3 MRROBOT.py")
elif user == 4:
	os.system(System_funtions.clear)
	os.system(randoms_banners)
	print("\n"+Numbers.number_one, Lists.password[0], "\n"+Numbers.number_two, Lists.password[1], "\n"+Numbers.number_three, Lists.password[2], "\n"+Numbers.number_four, Lists.password[3], "\n"+Numbers.number_five, Lists.password[4], "\n"+Numbers.number_six, Lists.password[5], "\n"+Numbers.number_none, Lists.back[0])
	passwd = int(input(BLUE+"===> "+RED))
	if passwd == 1:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing hydra...")
		time.sleep(3)
		os.system("apt -y install hydra")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif passwd == 2:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing medusa...")
		time.sleep(3)
		os.system("apt -y install medusa")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif passwd == 3:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing ncrack...")
		time.sleep(3)
		os.system("apt -y install ncrack")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif passwd == 4:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing john...")
		time.sleep(3)
		os.system("apt -y install john")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif passwd == 5:
		passwd_path = input("Write the path: ")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Connecting with https://github.com ...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Starting cloning...")
		time.sleep(3)
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"cloning https://github.com/Mebus/cupp")
		time.sleep(3)
		git.Git(f"{passwd_path}").clone("https://github.com/Mebus/cupp")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+f"Installation completed, saved in {passwd_path} wait...")
		time.sleep(5)
		os.system("python3 MRROBOT.py")
	elif passwd == 6:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing crunch...")
		time.sleep(3)
		os.system("apt -y install crunch")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif passwd == 00:
		os.system("python3 MRROBOT.py")
	else:
		print(RED+"error, fatal !!!, choose a correct option")
		time.sleep(3)
		os.system("python3 MRROBOT.py")
elif user == 5:
	os.system(System_funtions.clear)
	os.system(randoms_banners)
	print("\n"+Numbers.number_one, Lists.wireless[0], "\n"+Numbers.number_two, Lists.wireless[1], "\n"+Numbers.number_three, Lists.wireless[2], "\n"+Numbers.number_four, Lists.wireless[3], "\n"+Numbers.number_none, Lists.back[0])
	wir = int(input(RED+"===> "+BLUE))
	if wir == 1:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing reaver...")
		time.sleep(3)
		os.system("apt -y install reaver")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
	elif wir == 2:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing wifite...")
		time.sleep(3)
		os.system("apt -y install wifite")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
	elif wir == 3:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing wifite2...")
		time.sleep(3)
		os.system("apt -y install wifite2")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
	elif wir == 4:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing aircrack-ng...")
		time.sleep(3)
		os.system("apt -y install aircrack-ng")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
	elif wir == 00:
		os.system("python3 MRROBOT.py")
	else:
		print(RED+"error, fatal !!!, choose a correct option")
		time.sleep(3)
		os.system("python3 MRROBOT.py")
elif user == 6:
	os.system(System_funtions.clear)
	os.system(randoms_banners)
	print("\n"+Numbers.number_one, Lists.sniff[0], "\n"+Numbers.number_two, Lists.sniff[1], "\n"+Numbers.number_three, Lists.sniff[2], "\n"+Numbers.number_none, Lists.back[0])
	sniffi = int(input(BLUE+"===> "+RED))
	if sniffi == 1:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing bettercap...")
		time.sleep(3)
		os.system("apt -y install bettercap")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif sniffi == 2:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing wireshark...")
		time.sleep(3)
		os.system("apt -y install wireshark")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif sniffi == 3:
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"performing an update on the system...")
		time.sleep(3)
		os.system("apt -y update")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Installing macchanger...")
		time.sleep(3)
		os.system("apt -y install macchanger")
		print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"INSTALATION COMPLETE, please wait..")
		sleep(4)
		os.system("python3 MRROBOT.py")
	elif sniffi == 00:
		os.system("python3 MRROBOT.py")
	else:
		print(RED+"error, fatal !!!, choose a correct option")
		time.sleep(3)
		os.system("python3 MRROBOT.py")
elif user == 00:
	print(RED+"["+YELLOW+"*"+RED+"]"+WHITE+"Closing program....")
	time.sleep(3)
