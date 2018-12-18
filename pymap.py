# coding: utf-8
import socket, os, colorama, time
from colorama import Style, Fore, init

init(autoreset=True)

os.system("cls")
print ("""
            ___  ___            
            |  \/  |            
 _ __  _   _| .  . | __ _ _ __  
| '_ \| | | | |\/| |/ _` | '_ \ 
| |_) | |_| | |  | | (_| | |_) |
| .__/ \__, \_|  |_/\__,_| .__/ 
| |     __/ |            | |    
|_|    |___/             |_|

""") 


adresseIp = raw_input("Adresse IP a scanner : ")
debPort = int(raw_input("Debut de port a scanner : "))
finPort = int(raw_input("Fin de port a scanner : "))

print(Fore.YELLOW+"\nDebut du scan a : "+time.strftime("%X")+"\n")

print("----------------------")
for port in range(debPort, finPort+1):
	s = socket.socket()
	s.settimeout(1)
	resultat = s.connect_ex((adresseIp, port))
	if resultat == 0:
		print (Fore.GREEN + "[+] Port {} Open".format(port))
	else:
		print (Fore.RED + "[-] Port {} Closed".format(port))
	s.close()
print("----------------------")
print(Fore.YELLOW+"\nFin du scan a : "+time.strftime("%X")+"\n")
