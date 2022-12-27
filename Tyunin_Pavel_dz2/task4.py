'''
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
'''

def get_multiply(numbers):
    result = 1
    with open('file.txt', 'r', encoding='utf-8') as f:
        for line in f:
            indx = int(line.replace('\n', ''))
            result *= numbers[indx]
    return result


if __name__ == '__main__':
    n = int(input('Введите N для создания диапозона [-N; N]: '))
    numbers = [num for num in range(-n, n + 1)]
    position = input(f'Введите индексы для умножения через пробел(индекс не должен превышать {len(numbers)}): ').split()
    with open('file.txt', 'w', encoding='utf-8') as f:
        for pos in position:
            f.write(pos + '\n')
    print(f'Числовой ряд: {numbers}.\nПроизведение выбранных чисел: {get_multiply(numbers)}')
