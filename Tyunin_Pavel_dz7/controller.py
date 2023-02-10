import exp_data
import imp_data

contacts = []
contacts_sorted = []
exp_data.load_data(contacts)
action = input(f'Выберите действие:\n'
               f'   1 - просмотр всех контактов\n'
               f'   2 - запись контакта\n'
               f'   3 - вывод Фамилии и Имени\n'
               f'   4 - сортировка по id\n'
               f'   5 - сортировка по Фамилии\n'
               f'   0 - завершение\n'
               f'>>> ')
while action != '0':
    if action == '1':
        for i in range(1, len(contacts)):
            print(' '.join(contacts[i]))
    elif action == '2':
        imp_data.save_data(contacts)
    elif action == '3':
        for i in range(1, len(contacts)):
            if '' not in contacts[i]:
               print(contacts[i][1] + ' ' + contacts[i][2])
    elif action == '4':
        for i in range(1, len(contacts)):
            contact = contacts[i]
            contacts_sorted.append(' '.join(contact))
        contacts_sorted.sort()
        for contact in contacts_sorted:
            print(contact)
        contacts_sorted.clear()
    elif action == '5':
        for i in range(1, len(contacts)):
            contact = contacts[i][2] + ' ' + contacts[i][1] \
                      + ' ' + contacts[i][0] + ' ' + contacts[i][3] + ' ' + contacts[i][4]
            contacts_sorted.append(contact)
        contacts_sorted.sort()
        for contact in contacts_sorted:
            contact = contact.split()
            contact = contact[2] + ' ' + contact[0] \
                      + ' ' + contact[1] + ' ' + contact[3] + ' ' + contact[4]
            print(contact)
        contacts_sorted.clear()
    else:
        print('Неизвестная команда')
    action = input(f'Выберите действие:\n'
                   f'   1 - просмотр всех контактов\n'
                   f'   2 - запись контакта\n'
                   f'   3 - вывод Фамилии и Имени\n'
                   f'   4 - сортировка по id\n'
                   f'   5 - сортировка по Фамилии\n'
                   f'   0 - завершение\n'
                   f'>>> ')