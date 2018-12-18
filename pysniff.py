# coding: utf-8
from scapy.all import *
"""
def pkt_callback(pkt):
	pkt.show()

sniff(prn=pkt_callback, filter="port 80", store=0)
"""

def http_header(packet):
        http_packet=str(packet)
        if http_packet.find('POST'):
                print POST_print(packet)
        print packet
def POST_print(packet1):
        print "***************************************POST PACKET****************************************************"
        print packet1
        print "*****************************************************************************************************\n"


sniff(prn=POST_print, filter="port 80", store=0, lfilter= lambda p: "POST" in str(p))