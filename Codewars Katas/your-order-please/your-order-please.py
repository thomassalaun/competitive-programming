def order(sentence):
    sentence_array = sentence.split()
    maxi = len(sentence_array)
    ordered_sentence_array = []
    
    for i in range(1, maxi + 1) :
        for j in sentence_array : 
            if str(i) in j : 
             ordered_sentence_array.append(j)
             sentence_array.remove(j)
                
    return ' '.join(ordered_sentence_array)
    
print(order("is2 Thi1s T4est 3a"))