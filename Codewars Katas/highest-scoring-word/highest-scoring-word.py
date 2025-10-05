def high(x):
    score = lambda x: sum(map(lambda y: ord(y) - 96, str(x)))
    
    return max(x.split(), key = score)