'''
Реализуйте алгоритм перемешивания списка.
'''

from random import randint


def randlist(list):
    indx_list = []
    new_list = []
    for i in range(len(list)):
        while True:
            indx = randint(0, len(list) - 1)
            if indx not in indx_list:
                indx_list.append(indx)
                break
        new_list.append(list[indx])
    return new_list


if __name__ == '__main__':
    ls = [n for n in range(0, 20)]
    print(f'Исходный список: {ls}\nПеремешанный список: {randlist(ls)}')
