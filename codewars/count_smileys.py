def count_smileys(arr):
    count = 0
    if len(arr) == 0:
        return 0
    else:
        for i in range(len(arr)):
            #for j in range(len(arr[i])):
            if ':)' in arr[i]:
                count +=1
                #print(arr[i])
            elif ':-)' in arr[i]:
                count +=1
            elif ':~)' in arr[i]:
                count +=1
            elif ':D' in arr[i]:
                count +=1
            elif ';)' in arr[i]:
                count +=1
            elif ';D' in arr[i]:
                count +=1
            elif ';-)' in arr[i]:
                count +=1
            elif ';~)' in arr[i]:
                count +=1
            elif ';~D' in arr[i]:
                count +=1
            elif ':-D' in arr[i]:
                count +=1
            elif ':~D' in arr[i]:
                count +=1
            elif ';-D' in arr[i]:
                count +=1
    return count
    
print(count_smileys([':D',':~)',';~D',':)']))
