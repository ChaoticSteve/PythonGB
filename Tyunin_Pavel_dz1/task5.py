'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
from math import sqrt

def get_length(a, b):
    length = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    return length

if __name__ == '__main__':
    try:
        a = list(map(int, input('Введите координаты первой точки через ",": ').split(',')))
        b = list(map(int, input('Введите координаты второй точки через ",": ').split(',')))
        print(f'Расстояние между точками {get_length(a, b):0.3f}')
    except ValueError as e:
        print('Не верно введены координаты')