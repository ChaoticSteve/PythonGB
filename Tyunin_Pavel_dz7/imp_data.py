def save_data(contacts):
    contact = [str(len(contacts))]
    text = ['Имя: ', 'Фамилия: ', 'Номмер телефона: ', 'Комментарий: ']
    for i in range(len(text)):
        contact.append(input(text[i]))
    with open('contacts.txt', 'a', encoding='UTF-8') as f:
            f.write(','.join(contact) + '\n')
    contacts.append(contact)




if __name__ == '__main__':
    save_data()


