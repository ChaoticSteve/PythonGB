'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def get_negafibonacci(n):
    numbers = [0, 1]
    for i in range(1, n):
        numbers.append(numbers[i] + numbers[i - 1])
    l = len(numbers)
    nega_numbers = [numbers[l - i - 1] * -1 if (l - i - 1) % 2 == 0 else numbers[l - i - 1] for i in range(l)]
    nega_numbers.pop()
    return nega_numbers + numbers

if __name__ == '__main__':
    n = int(input('Введите количество чисел Фибоначчи: '))
    print(f'Набор чисел Негафибоначчи: {get_negafibonacci(n)}')
