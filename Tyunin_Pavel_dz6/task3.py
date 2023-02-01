'''
Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
'''

if __name__ == '__main__':
    ls = [2, 3, 4, 5, 6]
    length = len(ls)//2+1 if len(ls) % 2 != 0 else len(ls)//2
    multiply = [ls[i] * ls[len(ls) - i - 1] for i in range(length)]
    print(f'Исходный список: {ls}\n'
          f'Произведение пар чисел: {multiply}')