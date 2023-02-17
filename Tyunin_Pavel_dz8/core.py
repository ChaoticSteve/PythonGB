import json
from random import randint, choice
def add_studend(students):
    student = input('Введите фамилию и имя ученика: ')
    students[student] = {}

def add_subject(students):
    subject = input('Введите предмет: ')
    if len(students) != 0:
        for student in students:
            students[student].setdefault(subject, [])
def add_grade(students):
    student = input('Введите фамилию и имя ученика: ')
    subject = input('Введите предмет: ')
    grade = input('Введите оценку: ')
    if student in students:
        if subject in students[student]:
            if grade.isdigit():
                students[student][subject].append(int(grade))
            else:
                print('Оценка должна быть числом')
        else:
            print('Данного предмета нет в базе')
    else:
        print('Данного ученика нет в базе')
def get_students(students):
    if len(students) != 0:
        print('Список учеников:')
        for student in students:
            print(student)
def get_grades(students):
    student = input('Введите фамилию и имя ученика: ')
    if student in students:
        print(f'Оценки ученика: {student}')
        for subject in students[student]:
            print(subject, '-', *students[student][subject])
    else:
        print('Данного ученика нет в базе')
def get_average(students):
    student = input('Введите фамилию и имя ученика: ')
    subject = input('Введите предмет: ')
    if student in students:
        if subject in students[student]:
            grades = students[student][subject]
            print(f'Средняя оценка по предмету {subject} ученика {student}: {sum(grades)/len(grades):.2f}')
        else:
            print('Данного предмета нет в базе')
    else:
        print('Данного ученика нет в базе')
def get_average_all(students):
    subject = input('Введите предмет: ')
    subjects = []
    for student, info in students.items():
        if subject not in info:
            continue
        subjects.append(sum(info[subject])/len(info[subject]))
    print(f'Средний балл школы по предмету {subject}: {sum(subjects)/len(subjects):.2f}')
def generate_students():
    with open('russian_names.json', encoding='UTF-8-sig') as f:
        d = json.load(f)
        names = [name['Name'] for name in d]
    with open('russian_surnames.json', encoding='UTF-8-sig') as f:
        d = json.load(f)
        surnames = [name['Surname'] for name in d]
    subjects =  ['Чистописание', 'Чтение', 'Труд', 'Природоведение', 'Музыка', 'Математика', 'Алгебра', 'Физика', 'Химия']
    stundents = {}
    for i in range(100):
        stundents[choice(surnames) + ' ' + choice(names)] = {choice(subjects) : [randint(1, 5)]}
    return stundents



