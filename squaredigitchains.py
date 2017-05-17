

b = 0
def squaredigits(n):
    b = 0
    a = list(map(int, str(n)))
    #print(len(a))
    for i in range(0, len(a)):
        b = b + (a[i] ** 2)
    if b == 89:
        return True
    elif b == 1:
        return False
    else:
        squaredigits(b)
c = 0
x = 0
for x in range(1, 10000000):
    if squaredigits(x):
        c = c + 1
#print(squaredigits(85))
print(c)
