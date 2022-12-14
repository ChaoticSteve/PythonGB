#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def check_predicate(xyz):
    if len(xyz) == 3:
        dis = not (xyz[0] or xyz[1] or xyz[2])
        con = not xyz[0] and not xyz[1] and not xyz[2]
        result = dis == con
        if result:
            print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - истинно')
        else:
            print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - ложно')
    else:
        print('Ввели больше 3-х чисел')
if __name__ == '__main__':
    try:
        xyz = list(map(int, input('Введите 3 числа через ",": ').split(',')))
        check_predicate(xyz)
    except ValueError as e:
        print('Нужно вводить числа через ","')


