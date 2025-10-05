def pig_it(text):
    transformation = lambda x : x[1:] + x[0] + 'ay' if x.isalpha() else x
    
    return ' '.join(map(transformation, text.split()))