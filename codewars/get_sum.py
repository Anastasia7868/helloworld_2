def get_sum(a,b):
    number = 0
    if a < b:
        for i in range(a, b+1, 1):
            number += i
    #print(number)
    elif a == b:
        number = a
    else:
        for i in range(b, a+1, 1):
            number += i

    return number

print(get_sum(0,-1))
