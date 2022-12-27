'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''

def get_summ(number):
    summ = 0
    for num in number:
        if num.isdigit():
            summ += int(num)
    return summ

if __name__ == '__main__':
    number = input('Введите вещественное число: ')
    print(f'Сумма чисел введённого числа: {get_summ(number)}')