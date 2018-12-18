# coding: utf-8
import os
from scapy.all import *
#
#def main():
#	os.system("cls")
#	print("""
#                             _____                                 
#                            / ____|                                
#  ___  ___ __ _ _ __  _   _| (___   ___ __ _ _ __  _ __   ___ _ __ 
# / __|/ __/ _` | '_ \| | | |\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# \__ \ (_| (_| | |_) | |_| |____) | (_| (_| | | | | | | |  __/ |   
# |___/\___\__,_| .__/ \__, |_____/ \___\__,_|_| |_|_| |_|\___|_|   
#               | |     __/ |                                       
#               |_|    |___/                                        
# """)
#	tcp_scan()
#

host = raw_input("Adresse IP a scanner : ")
debPort = int(raw_input("Debut de port a scanner : "))
finPort = int(raw_input("Fin de port a scanner : "))+1

for port in (debPort, finPort):
	SYN = 0x02
	ACK = 0x10
	SYNACK = SYN | ACK
	syn_pkt = IP(dst=host)/TCP(dport=port, flags='S')
   	synack_pkt = sr1(syn_pkt, timeout=1)
   	if synack_pkt is None:
   		print("Port injoingnable")
   	elif synack_pkt['TCP'].flags == SYNACK:
   		print("Port "+ str(port)+" Open")
   	else:
   		print("Port "+ str(port)+ " Closed")