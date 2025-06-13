# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = {}

for student in students:
    name = student['first_name']
    if name in names:
         names[name] += 1
    else:
        names[name] = 1

for name, name_count in names.items():
    print(f'{name}: {name_count}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = {}

for student in students:
    name = student['first_name']
    if name in names:
         names[name] += 1
    else:
         names[name] = 1

most_common = max(names, key=names.get)
    
print(f'Самое частое имя среди учеников: {most_common}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

for class_number,  class_students in enumerate(school_students, start=1):
    names = {}
    for student in class_students:
        name = student['first_name']
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
            
    most_common = max(names, key=names.get)
    
    print(f'Самое частое имя в классе {class_number}: {most_common}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for students in school: 
    school_class = students['class']
    students_name = students['students']
    boys = 0
    girls = 0
    for name in students_name:
        if is_male[name['first_name']]: 
            boys += 1
        else:
            girls += 1

    print(f"В классе {students['class']}: девочки {girls}, мальчики {boys}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys_stats = {}
girls_stats = {}

for students in school: 
    school_class = students['class']
    students_name = students['students']
    boys = 0
    girls = 0
    for name in students_name:
        if is_male[name['first_name']]: 
            boys += 1
        else:
            girls += 1
    boys_stats[school_class] = boys
    girls_stats[school_class] = girls    

more_boys = max(boys_stats, key=boys_stats.get)
more_girls = max(girls_stats, key=girls_stats.get)

print(f'Больше всего мальчиков в классе {more_boys}')
print(f'Больше всего девочек в классе {more_girls}')

