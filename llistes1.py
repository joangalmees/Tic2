"""
Volem saber si una paraula és capicua:

    entrada: "capicua", sortida: no és capicua
    entrada: "anna", sortida: és capicua
"""

def capicua(paraula):

    r= True
    j = len(paraula) - 1

    for i in paraula: 
        if i != paraula[j]: 
            r=false
        j-=1
    
    return r

def printCapicua(paraula):
    print("Introdueix una paraula qualsevol ", paraula , end=" ")
    if (capicua(paraula)):
        print("Capicua")
    else:
        print("No Capicua")
    return True

entrada="pop"
printCapicua(entrada)
