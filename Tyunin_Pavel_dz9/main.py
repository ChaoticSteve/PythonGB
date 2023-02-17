import telebot
from random import randint


bot = telebot.TeleBot("TOKEN")
names = []
candies = 221
max_stake = 28
prev_stake = 0
stake = 0

def restart():
    global candies
    global prev_stake
    candies = 50
    prev_stake = 0

def get_player_names(message):
    global names
    names = [message.from_user.first_name, 'Бот']

def coin_toss():
    global switch
    global names
    switch = randint(0, 1)

def switch_turn():
    global switch
    if switch == 1:
        switch = 0
    else:
        switch = 1

def player_move(message):
    global stake
    global prev_stake
    global candies
    if message.text.isdigit() and 0 < int(message.text) <= max_stake:
        stake = int(message.text)
        bot.send_message(message.chat.id, f'Игрок берет {stake} конфет')
        candies -= stake
        prev_stake = stake
        switch_turn()
    else:
        bot.send_message(message.chat.id, f'Можно брать от 1 до {max_stake} конфет!')
    game(message)

def bot_move(message):
    global stake
    global candies
    if candies < 29:
        stake = candies
    else:
        stake = candies - (((candies // 28) * 28) + 1)
        if stake == -1:
            stake = 28 - 1
        elif stake == 0:
            stake = 28
    while stake > 28 or stake < 1:
        stake = randint(1, 28)
    bot.send_message(message.chat.id, f'Бот берет {stake} конфет')
    candies -= stake
    switch_turn()
    game(message)


def game(message):
    if candies > 0:
        bot.send_message(message.chat.id, f'На кону {candies} конфет')
        if switch == 0:
            bot.send_message(message.chat.id, f'Ваш ход. Сколько конфет возьмете (1 - {max_stake}?')
            bot.register_next_step_handler(message, player_move)
        else:
            bot_move(message)
    else:
        bot.send_message(message.chat.id, f'Осталось {candies} конфет')
        switch_turn()
        bot.send_message(message.chat.id, f'Выиграл {names[switch]}!')

def option(message):
    if message.text.lower() == 'да':
        get_player_names(message)
        coin_toss()
        restart()
        bot.send_message(message.chat.id, f'Первый ход за {names[switch]}')
        game(message)
    elif message.text.lower() == 'правила':
        bot.send_message(message.chat.id, f'На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.\n'
                                          f'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
                                          f''f'Все конфеты оппонента достаются сделавшему последний ход.\n')
    else:
        bot.send_message(message.chat.id, f'Неизвестная команда')

def play_game():
    @bot.message_handler(content_types = ["text"])
    def controller(message):
        if message.text.lower() == 'игра':
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, сыграем в игру (да/правила)?')
            bot.register_next_step_handler(message, option)
        else:
            bot.send_message(message.chat.id, f'Напиши игра')
    bot.infinity_polling()
if __name__ == '__main__':
    play_game()