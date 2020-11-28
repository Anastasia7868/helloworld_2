def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i%2 == 0 :
            even.append(i)
        else:
            odd.append(i)
    if len(odd) < len(even):

        return int(''.join(map(str, odd)))
    else:
        return int(''.join(map(str,even)))



print(find_outlier([2, 4, 6, 8, 10, 3]))
