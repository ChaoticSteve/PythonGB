'''
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

def get_pair_multiply(numbers):
    length = len(numbers)//2
    if len(numbers) % 2 != 0:
        length += 1
    mult_numbers = [numbers[i]*numbers[len(numbers) - i - 1] for i in range(length)]
    return mult_numbers

if __name__ == '__main__':
    numbers = [2, 3, 4, 5, 6, 7, 8]
    print(f'Набор цифр: {numbers}\nПроизведение пар: {get_pair_multiply(numbers)}')



