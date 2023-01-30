'''
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
from random import randint
def get_polynomial(k):
    num = randint(0, 100)
    if k == 1:
        if num == 0:
            return '= 0'
        elif num == 1:
            return 'x = 0'
        else:
            return str(num) + '*x = 0'
    if num == 0:
        return get_polynomial(k - 1)
    elif num == 1:
        return 'x**' + str(k) + ' + ' + get_polynomial(k - 1)
    return str(num) + '*x**' + str(k) + ' + ' + get_polynomial(k - 1)


if __name__ == '__main__':
    k = int(input('Задайте наибольшую степень в многочлене: '))
    with open('polinomial.txt', 'w', encoding='utf-8') as f:
        f.write(get_polynomial(k))