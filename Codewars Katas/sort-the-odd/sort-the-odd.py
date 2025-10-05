def sort_array(source_array):
    phrase = ''.join(['0' if i % 2 == 0 else '1' for  i in source_array])
                     
    even_numbers = [i for i in source_array if i % 2 == 0]
    odd_numbers = [i for i in source_array if i % 2 == 1]
    odd_numbers = sorted(odd_numbers)
    
    sorted_array = []
    for i in phrase :
        if i == '0' :
            added_element = even_numbers[0]
            sorted_array.append(added_element)
            even_numbers.remove(added_element)
        else : 
            added_element = odd_numbers[0]
            sorted_array.append(added_element)
            odd_numbers.remove(added_element)
                     
    return sorted_array
            
    