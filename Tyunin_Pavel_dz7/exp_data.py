def load_data(contacts):
    try:
        with open('contacts.txt', 'r', encoding='UTF-8') as f:
            for line in f:
                line = line.replace('\n', '')
                if line != '':
                    contacts.append(line.split(','))
    except FileNotFoundError:
        with open('contacts.txt', 'w', encoding='UTF-8') as f:
            f.write('ID,Name,Surname,Phone,Comment\n')


if __name__ == '__main__':
    load_data([])