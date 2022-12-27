'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

def get_binary(number):
    if number == 0:
        return ''
    return get_binary(number//2) + str(number%2)

if __name__ == '__main__':
    number = int(input('Введите число: '))
    print(f'Его двоичная запись: {get_binary(number)}')