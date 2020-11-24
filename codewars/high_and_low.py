def high_and_low(numbers):
    number = numbers.split(' ')

    posledovatelnost = []

    for num in number:
        posledovatelnost.append(int(num))

    return f'{max(posledovatelnost)} {min(posledovatelnost)}'

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
