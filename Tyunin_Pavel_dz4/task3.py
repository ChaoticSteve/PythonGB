'''
Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''
from random import randint
from collections import Counter

def get_unique(numbers):
    unique = []
    count_unique = Counter(numbers)
    for key in count_unique:
        if count_unique[key] == 1:
            unique.append(key)
    return unique

if __name__ == '__main__':
    numbers = [randint(1, 10) for i in range(10)]
    print(f'Исходная последоваетльность: {numbers}\n'
          f'Последовательность неповторяющихся элементов: {get_unique(numbers)}')