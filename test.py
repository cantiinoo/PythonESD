"""
dico ={
    "Nom" : "Deborde",
    "Prenom" : "Quentin",
    "Age" : 22
    }


for i in dico.keys():
    print i

for i in dico.values():
    print i

for i in dico.items():
    print i


import os
from time import sleep

cmd = raw_input("Votre cmd : ")
os.system(cmd)
os.system("pause")
"""

def sayHello(name):
    if (name):
        print "Ton nom est " + name
    else:
        print "Dis moi ton nom"
         
sayHello("Quentin")
