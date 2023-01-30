'''
Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале.
Игроки ходят друг за другом, вписывая желаемое количество конфет.
Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.

В качестве дополнительного усложнения можно:
        a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

        b) Подумайте как наделить бота ""интеллектом""
        (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать,
        чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
'''

from random import randint, choice
from time import sleep


def easy_bot():
    name = input('Ваше имя? ')
    replicas = ['Хмммм...', 'Дай подумать', 'Сколько же взять?', 'Думаю...', 'Интересно, а если так']
    amount = 221
    if randint(1, 2) == 1:
        player = True
    else:
        player = False
    while amount > 0:
        if player:
            print('Ход игрока')
            num = int(input('Сколько конфет возьмёшь? '))
            if num <= 28 and num <= amount:
                amount -= num
                player = False
            else:
                if num > amount:
                    print('Взято больше оставшихся конфет')
                else:
                    print('Взято больше 28 конфет')
        else:
            print('Ход противника')
            print(f'{choice(replicas)}')
            sleep(randint(1, 3))
            if amount > 28:
                num = randint(1, 28)
                print(f'Взято {num} конфет')
                amount -= num
            else:
                num = randint(1, amount)
                print(f'Взято {num} конфет')
                amount -= num
            player = True
        print(f'На столе осталось {amount} конфет\n')
    if player:
        return f'Победа за компьютером\n'
    return f'Поздравляю, победа за {name}\n'


def hard_bot():
    name = input('Ваше имя? ')
    replicas = ['Хмммм...', 'Дай подумать', 'Сколько же взять?', 'Думаю...', 'Интересно, а если так']
    amount = 221
    if randint(1, 2) == 1:
        player = True
    else:
        player = False
    while amount > 0:
        if player:
            print('Ход игрока')
            num = int(input('Сколько конфет возьмёшь? '))
            if num <= 28 and num <= amount:
                amount -= num
                player = False
            else:
                if num > amount:
                    print('Взято больше оставшихся конфет')
                else:
                    print('Взято больше 28 конфет')
        else:
            print('Ход противника')
            print(f'{choice(replicas)}')
            sleep(randint(1, 3))
            if amount < 29:
                num = amount
            else:
                num = amount - (((amount // 28) * 28) + 1)
                if num == -1:
                    num = 28 - 1
                elif num == 0:
                    num = 28
            while num > 28 or num < 1:
                num = randint(1, 28)
            print(f'Взято {num} конфет')
            amount -= num
            player = True
        print(f'На столе осталось {amount} конфет\n')
    if player:
        return f'Победа за компьютером\n'
    return f'Поздравляю, победа за {name}\n'


def get_rules():
    print(f'На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.\n'
          f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
          f'Все конфеты оппонента достаются сделавшему последний ход.\n')


def play_pvp():
    amount = 221
    name1, name2 = input('Имя/Ник первого игрока: '), input('Имя/Ник второго игрока: ')
    if randint(1, 2) == 1:
        first = True
        second = False
        print('По жеребьёвке первым ходит', name1)
    else:
        first = False
        second = True
        print('По жеребьёвке первым ходит', name1)
    while amount > 0:
        num = int(input('Сколько конфет возьмёшь? '))
        if first and num <= 28 and num <= amount:
            amount -= num
            first = False
            second = True
            print(f'Ход {name2}')
        elif second and num <= 28 and num <= amount:
            amount -= num
            first = True
            second = False
            print(f'Ход {name1}')
        else:
            if num > amount:
                print('Взято больше оставшихся конфет')
            else:
                print('Взято больше 28 конфет')
        print(f'На столе осталось {amount} конфет\n')
    if first:
        return f'Победил {name2}\n'
    return f'Победил {name1}\n'


if __name__ == '__main__':
    print('Время сыграть в игру')
    action = input(f'Выбери действие\n'
                   f'   1-правила\n'
                   f'   2-человек провив человека\n'
                   f'   3-человек против простого ПК\n'
                   f'   4-человек против умного ПК\n'
                   f'   0-закончить играть\n'
                   f'>>> ')
    while action != '0':
        if action == '1':
            get_rules()
        elif action == '2':
            print(play_pvp())
        elif action == '3':
            print(easy_bot())
        elif action == '4':
            print(hard_bot())
        else:
            print(f'Странный выбор, даже не знаю, что ответить...\n')
        action = input(f'Выбери действие\n'
                       f'   1-правила\n'
                       f'   2-человек провив человека\n'
                       f'   3-человек против простого ПК\n'
                       f'   4-человек против умного ПК\n'
                       f'   0-закончить играть\n'
                       f'>>> ')
    print(f'Всего доброго')
