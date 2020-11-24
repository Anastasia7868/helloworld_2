def anagrams(word, words):
    answer = []
    sum_word = 0
    for letter in word:
        sum_word += ord(letter)
    #print(sum_word)
    for element in words:
        sum_element = 0
        for letter in element:
            sum_element += ord(letter)
    #    print(sum_element)
        if len(word) == len(element) and sum_word==sum_element:
            answer.append(element)
    return answer


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
