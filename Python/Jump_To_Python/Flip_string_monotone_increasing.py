def flip_count(S) :
    list_S = list(S)
    print(list_S)
    length = len(list_S)
    if length % 2 == 0:
        if list_S[:int(length/2)+1].count('1') > list_S[int(length/2):].count('0') :
            result = list_S[int(length/2):].count('0')
        else : result = list_S[:int(length/2)+1].count('1')
    else :
        if list_S[int((length+1)/2)] == '0':
            result = list[int((length+1)/2)+1:].count('0')
        else : result = list[:int((length+1)/2)].count('1')
    return result