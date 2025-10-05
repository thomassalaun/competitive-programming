def dig_pow(n, p):
    digits_n = [int(i) for i in str(n)]
    
    number = sum([digits_n[i]**(p+i) for i in range(len(digits_n))])
    
    k = 1
    test = n*k
    while test <= number :
        if test == number : 
            return k
        k += 1
        test = n*k
    return -1