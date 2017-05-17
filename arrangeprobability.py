def probability(b, n):
    if (b/n) * ((b-1)/(n-1)) == 1/2:
        return True
    else:
        return False


print(probability(15, 21))
