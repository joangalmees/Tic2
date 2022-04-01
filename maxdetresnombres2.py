from easyinput import read
a, b, c = read(int, int, int)
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
elif a == b or a == c or b == c:
    print(max(a ,b ,c))
max(a, b, c)
