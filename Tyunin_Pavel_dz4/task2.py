'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''

def get_factors(number):
    factors = []
    factor = 2
    while factor ** 2 <= number:
        if number % factor == 0:
            factors.append(factor)
            number //= factor
        else:
            factor += 1
    if number > 1:
        factors.append(number)
    return factors

if __name__ == '__main__':
    number = int(input('Введите число: '))
    print(f'Список множителей: {get_factors(number)}')

