a = 0
b = 0
sum = 0
sums =[] 
while a < 100:
    if b == 100:
        a = a + 1
        b = 0

    c = a ** b 
    
    d =  list(map(int, str(c)))
    for i in range(0, len(d)):
        sum = sum + d[i]
    sums.append(sum)
    if sum == 972:
        e = a
        r = b
    
    sum = 0
    
    
    
    
    b = b + 1
print(sorted(sums))
print(e, r)
