def tribonacci(signature, n):
    liste = signature
    for i in range(n-3) :
        liste += [sum(liste[::-1][:3])]
    return liste[:n]