'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв""
'''



if __name__ == '__main__':
    words = 'ываабв лповап абвцукв алоабвабв ываываыв'
    filter_words = ' '.join([word for word in words.split() if 'абв' not in word])
    print(f'Исходная строка: {words}\nОтфильтрованная строка: {filter_words}')
