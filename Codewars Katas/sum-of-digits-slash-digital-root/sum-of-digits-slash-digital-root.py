def digital_root(n):
    n = sum([int(x) for x in str(n).split()])
    while len(str(n)) != 1 :
        n = sum([int(x) for x in str(n)])
    return n