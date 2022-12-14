'''Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''


def check_quarter(x, y):
    if x < 0:
        if y < 0:
            print('III четверть')
        else:
            print('II четверть')
    else:
        if y < 0:
            print('IV четверть')
        else:
            print('I четверть')
if __name__ == '__main__':
    try:
        x = int(input('Введите координату по X: '))
        y = int(input('Введите координату по Y: '))
        check_quarter(x, y)
    except ValueError as e:
        print('Введено не число')