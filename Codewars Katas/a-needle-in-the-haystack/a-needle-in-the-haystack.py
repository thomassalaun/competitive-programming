def find_needle(haystack):
    n = 0
    for i in haystack :
        if str(i) == 'needle' :
            return "found the needle at position " + str(n)
        n += 1
    return None
        