def count_bits(n):
    p = bin(n)
    b = ''
    s = 0
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    b = list(b)

    for i in range(0, len(b)):
        if int(b[i]) == 1:
            s = s+1
    #return s
    #return b.count("1")
    return p.count("1")
print(count_bits(9))


def countBits(n):
    return bin(n).count("1")

print(countBits(9))