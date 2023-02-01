'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Модуль сжатия:
Для чисел:
Входные данные:
111112222334445
Выходные данные:
5142233415
Также должно работать и для букв:
Входные данные:
AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
Выходные данные:
6A1F2D7C1A17E
(5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.
'''


def compression(string):
    result = ''
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            result += str(count) + string[i]
            count = 1
    if count > 1 or (string[-2] != string[-1]):
        result += str(count) + string[-1]
    return result


def decompression(string):
    result = ''
    count = ''
    for symbol in string:
        if symbol.isdigit():
            count += symbol
        else:
            result += symbol * int(count)
            count = ''
    return result


if __name__ == '__main__':
    st = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
    print(f'После сжатия: {compression(st)}\nВосстановленная строка: {decompression(compression(st))}')
