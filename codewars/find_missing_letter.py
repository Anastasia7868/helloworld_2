def find_missing_letter(chars):
    x = int
    #print(ord('O'))
    for i in range(len(chars)-1):
        if ord(chars[i+1]) - ord(chars[i]) != 1:
            letter = ord(chars[i]) + 1


    return chr(letter)


print(find_missing_letter(['O','Q','R','S']))
print(find_missing_letter(['a','b','c','d','f']))
