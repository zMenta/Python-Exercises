
# rows = 2
# coded = 'hlowrd_el_ol'

rows = 3
coded = 'mnes__ya_____mi'


# def decodeString(numberOfRows, encodedString):
#     array = [] 
#     for i in range(numberOfRows):
#         array.append([-1] * numberOfRows * len(encodedString))
        
        
#     i = 0
#     j = 0
#     for letter in encodedString:
#         array[j].insert(i, letter)
#         i += 1
#         j += 1
        
#         if j >= numberOfRows:
#             j = 0
    
#     print(array[0])
#     print(array[1])


# decodeString(rows, coded)


def decodeString(numberOfRows, encodedString):
    size = int(len(encodedString) / numberOfRows)
    array = []
    decoded_string = ""
    
    for i in range(numberOfRows):
        array.append([])
    
    letter_index = 0
    for j in range(numberOfRows):
        for i in range(size):
            array[j].append(encodedString[letter_index])
            letter_index += 1
    
    aux_i = 0
    aux_j = 0
    column = 1
    for j in range(numberOfRows):
        for i in range(size):   
            if aux_i >= size:
                break
            
            decoded_string += array[aux_j][aux_i]
            
            if column >= size:
                break
            
            aux_i += 1
            aux_j += 1
            
            
            if aux_j >= numberOfRows:
                aux_j = 0
                aux_i = column
                column += 1
    
    
    return decoded_string.replace("_", " ")


print(decodeString(rows, coded))