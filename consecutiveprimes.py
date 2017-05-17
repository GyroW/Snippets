def isprime(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
                return True       
                # if input number is less than
                # or equal to 1, it is not prime
    else:
        return False



sum = 0
n = 2 
while sum < 1000000:
    if isprime(n):
        print(n)
        print(sum)
        sum = sum + n
    n = n + 1
   
