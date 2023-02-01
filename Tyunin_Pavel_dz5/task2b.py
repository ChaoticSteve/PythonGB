'''
Создайте программу для игры в ""Крестики-нолики"".
Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка,
внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9),
сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу
( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
'''

def draw_field(field):
    count = 1
    for line in field:
        row = ''
        for i in range(len(line)):
            if line[i] == ' ':
                if i != 2:
                    row += str(count) + '|'
                else:
                    row += str(count)
            else:
                if i != 2:
                    row += line[i] + '|'
                else:
                    row += line[i]
            count += 1
        print(f'{row}')

def check_pos(indx, symbol):
    global field
    if 1 <= indx <= 3:
        if field[0][indx-1] == 'X' or field[0][indx-1] == 'O':
            print('Место занято')
        else:
            field[0][indx-1] = symbol
    elif 4 <= indx <= 6:
        if field[1][indx-4] == 'X' or field[1][indx-4] == 'O':
            print('Место занято')
        else:
            field[1][indx-4] = symbol
    elif 7 <= indx <= 9:
        if field[2][indx-7] == 'X' or field[2][indx-7] == 'O':
            print('Место занято')
        else:
            field[2][indx-7] = symbol

def check_line(line, symbol):
    global run
    if line[0] == symbol and line[1] == symbol and line[2] == symbol:
        print(f'Победа за {symbol}')
        run = False

def check_winner(symbol):
    global field
    for line in field:
        check_line(line, symbol)
    line = []
    for i in range(3):
        line.append(field[i][i])
    check_line(line, symbol)
    check_line([field[2][0], field[1][1], field[0][2]], symbol)

def check_field(field):
    clear = True
    for line in field:
        if not (line[0].isalpha() and line[1].isalpha() and line[2].isalpha()):
            clear = False
    if clear:
        print('Ничья, очищаю поле.')
        field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        draw_field(field)



field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
draw_field(field)
run = True
cross = True
while run:
    if cross:
        print('Ход крестиков')
        indx = int(input('Введи позицию для крестика: '))
        check_pos(indx, 'X')
        draw_field(field)
        #check_winner('X')
        check_field(field)
        #cross = False
        print(' ')
    else:
        print('Ход ноликов')
        indx = int(input('Введит позицию для нолика: '))
        check_pos(indx, 'O')
        draw_field(field)
        check_winner('O')
        cross = True
        print(' ')
