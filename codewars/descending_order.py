def descending_order(num):
    #print(str(num))
    spisok = []
    for digit in str(num):
        spisok.append(digit)
    spisok = sorted(spisok)
    #print(spisok)
    #print(spisok[::-1])
    razvorot = ''.join(spisok[::-1])
    #print(razvorot)
    return int(razvorot)
