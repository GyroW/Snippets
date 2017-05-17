x = 1

while x < 1000000000000:
    y = 0
    two     =   sorted(list(map(str, str(2*x))))
    three   =   sorted(list(map(str, str(3*x))))
    four    =   sorted(list(map(str, str(4*x))))
    five    =   sorted(list(map(str, str(5*x))))
    six     =   sorted(list(map(str, str(6*x))))
    for i in range(0, len(two)):
       if two[i] == three[i] == four[i] == five[i] == six[i]:
           y = y + 1
       if y == len(two):
           print("x =", x)








    x = x + 1 
    


