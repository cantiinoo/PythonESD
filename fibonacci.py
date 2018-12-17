
limite = int(raw_input("Saisir la limite : "))

a = 0
b = 1
resultat = 0
print a
print b

while resultat < limite:
    resultat = a + b
    a = b
    b = resultat
    resultat = a + b
    print resultat    
    




