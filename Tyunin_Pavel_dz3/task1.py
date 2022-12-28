'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

# не точная формулировка задания, т.к нас просят найти нечётные позиции элементов, а в примере показывают чётные позиции
# поэтому реализовал 2 решения.

def get_oddpos_sum(numbers):  # на нечётных позициях - чётные индексы.
    odd_list = [numbers[i] for i in range(0, len(numbers), 2)]
    print(odd_list)
    return sum(odd_list)


def get_oddindx_sum(numbers):  # на чётных позициях - нечётные индексы
    odd_list = [numbers[i] for i in range(1, len(numbers), 2)]
    print(odd_list)
    return sum(odd_list)


if __name__ == '__main__':
    numbers = [2, 3, 5, 9, 3]
    print(f'Набор цифр: {numbers}\n'
          f'Сумма чисел на нечётных индексах: {get_oddindx_sum(numbers)}\n'
          f'Сумма чисел на нечётных позициях: {get_oddpos_sum(numbers)}')

