"""3 часть  добавить в игру несклоько пользователей
Добавить возможность ввода имен пользователей
добавить систему поочередного хода
добавить объявление попебителя"""

import random
def game():
    number = random.randint(1,100)
    #print(number)
    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    level = int(input('выберете уровень сложности 1-3: '))
    max_count = levels[level]
    user_count = int(input('введите количество пользователей: '))
    users = []
    is_winner = False
    winner_name = None
    for user in range(1, user_count+1):
        user_name = input(f'Введите имя {user} ползователя: ')
        users.append(user_name)
    #print(users)

    while not is_winner:
        count +=1

        if count > max_count:
            print('все пользователи програли! Количество попыток исчерпано')
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход пользователя {user}')
            user_number = int(input('Введите число: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            if user_number > number:
                print('введенное число БОЛЬШЕ загаданного')
            else:
                print('Введенное число МЕНЬШЕ загаданного')
    else:
        print(f'Победа! Число угаданно верно пользователем {winner_name}')
if __name__ == '__main__':
    game()