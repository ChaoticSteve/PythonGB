'''
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
from math import pi


def get_round(d):  # скучный вариант через round
    try:
        if 1 <= d[1] <= 13:
            return round(pi, d[1])
        return False
    except IndexError as e:
        return None


def get_nearest(d):  # через округление внутри f-строк пайтона
    try:
        if 1 <= d[1] <= 13:
            return '0.' + str(d[1] + 1)
        return False
    except IndexError as e:
        return None


if __name__ == '__main__':
    d = list(map(len, input('Введите точность вида "0.01": ').split('.')))
    if get_round(d) and get_nearest(d):
        print(f'Число Пи с заданной точностью: {get_round(d)}')
        print(f'Число Пи с заданной точностью: {pi:{get_nearest(d)}}')
    else:
        print('Вышел за диапазон точности')
