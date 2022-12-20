'''
Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
Пример:
- Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
        Сумма 9.06
'''

def get_summ(dict_num):
    numbers = list(dict_num.values())
    return sum(numbers)


if __name__ == '__main__':
    n = int(input('Введите количество чисел: '))
    dict_num = {num:round((1+1/num)**num, 2) for num in range(1, n+1)}
    print(f'Числовой ряд: {dict_num}.\nСумма значений: {get_summ(dict_num):0.2f}')