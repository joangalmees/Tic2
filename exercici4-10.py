import random
x=random.randrange(0,3)
"""
Pedra=0
Paper=1
Tissores=2
"""
#print(x)
y=int(input("introdueix Pedra=0 o Paper=1 o Tissores=2: "))
if x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
    print("Has guanyat")
elif x == 0 and y == 0 or x == 1 and y == 1 or x == 2 and y == 2:
    print("Has empatat")
else:
    print("Has perdut")