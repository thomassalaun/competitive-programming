from collections import Counter

def find_uniq(arr):
    def get_key(word):
        letters = [y.lower() for y in word if y.isalpha()]
        return tuple(sorted(set(letters)))

    caracterisations = [get_key(word) for word in arr]
    frequences = Counter(caracterisations)

    unique_key = None
    for key, count in frequences.items():
        if count == 1:
            unique_key = key
            break

    for word in arr:
        if get_key(word) == unique_key:
            return word