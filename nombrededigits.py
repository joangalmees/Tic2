n=int(input("Introdueix un número qualsevol: "))
count=0
while(n>0):
    count=count+1
    n=n//10
print("El número de digits en aquest nombre son:",count)