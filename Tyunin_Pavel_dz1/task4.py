'''
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
'''
def get_range(quarter):
    if quarter == '1':
        return 'x > 0 и y > 0'
    elif quarter == '2':
        return 'x > 0 и y < 0'
    elif quarter == '3':
        return 'x < 0 и y < 0'
    elif quarter == '4':
        return 'x < 0 и y > 0'
    return 'данной четверти нет'

if __name__ == '__main__':
    quarter = input('Введите номер четверти: ')
    print(f'Диапазон данной четверти: {get_range(quarter)}')