'''
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
'''


def get_dict(p):
    p_d = {}
    for elem in p:
        if '*x**' in elem:
            nums = elem.split('*x**')
            p_d[nums[1]] = nums[0]
        elif 'x**' in elem:
            nums = elem.split('x**')
            p_d[nums[1]] = '1'
        else:
            nums = elem.split('*x')
            p_d['1'] = nums[0]
    return p_d


def get_sum(p1_d, p2_d):
    polinomial = ''
    l = len(p1_d)
    for key in p1_d:
        if l > 1:
            if key in p2_d:
                polinomial += str(int(p1_d[key]) + int(p2_d[key])) + '*x**' + key + ' + '
            elif p1_d[key] == '1':
                polinomial += 'x**' + key + ' + '
            else:
                polinomial += p1_d[key] + '*x**' + key + ' + '
        else:
            if key in p2_d:
                pass
                polinomial += str(int(p1_d[key]) + int(p2_d[key])) + '*x'
            else:
                polinomial += p2_d[key] + '*x'
        l -= 1
    return polinomial


def get_result(p1, p2):
    polinomial = ''
    p1_d = get_dict(p1.split(' + '))
    p2_d = get_dict(p2.split(' + '))
    if len(p1_d) >= len(p2_d):
        return get_sum(p1_d, p2_d)
    return get_sum(p2_d, p1_d)

if __name__ == '__main__':
    with open('polinomial.txt', 'r', encoding='utf-8') as f:
        p1 = f.read().replace(' = 0', '')
    with open('polinomial1.txt', 'r', encoding='utf-8') as f:
        p2 = f.read().replace(' = 0', '')
    print(f'Первый многочлен: {p1}\n'
          f'Второй многочлен: {p2}\n'
          f'Их сумма: {get_result(p1, p2)}')
    with open('polinomial_sum.txt', 'w', encoding='utf-8') as f:
        f.write(get_result(p1, p2))
