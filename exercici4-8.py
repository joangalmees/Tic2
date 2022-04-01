print ("Este programa recibe sitete números y te devuelve la suma de estos")
total=0
negatiu=0
positiu=0
zero=0

for i in range(7):
    x = float(input("Introduce un número: "))
    if x > 0:
        positiu+=1
    elif x < 0:
        negatiu-=1
    else:
        zero+=1
    total = total + x
print("El total es: ", total)
print("Hi ha", positiu,"positius, hi ha", negatiu,"negatius hi ha", zero, "zeros")