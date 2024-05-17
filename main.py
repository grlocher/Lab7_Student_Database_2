students = [
  {"name": "Lawrence", "hometown": "Detroit", "favorite_food": "pizza"},
  {"name": "Katie", "hometown": "Flint", "favorite_food": "salad"},
  {"name": "Daniel", "hometown": "Troy", "favorite_food": "hamburgers"}
]


def list_names(students) -> [str, str]:
    print('Student names:')
    for i, name in enumerate(students):
        print(f'{i + 1}: {name['name']}')


def get_new_student(students) -> [str, str]:
    new_name = str(input('Please input a name for the new student: >> ')).capitalize()
    new_hometown = str(input('Next please input their hometown: >> ')).capitalize()
    new_food = str(input('Last please input their favorite food: >> ')).lower()
    return {"name": new_name, "hometown": new_hometown, "favorite_food": new_food}


while True:
    print()
    action = str(input('Please select which action you\'d like to take: add, view or quit: >> '))
    if 'view' in action:
        list_names(students)
        student_number = int(input(f'Which student would you like to learn about? Enter a number: >> '))
        print()
        student_name = students[student_number - 1]

        if student_number < 0 or student_number > len(students):
            print(f'Number {student_number} is not a valid student number, please try again.')
        else:
            print(f'Student {student_number} is {students[student_number - 1]['name']}. What would you like to know?')

        selection = str(input('Enter "hometown" or "favorite food": ')).lower()
        if 'hometown' in selection:
            print(f'{students[student_number - 1]['name']} is from {students[student_number - 1]['hometown']}')
        elif 'favorite food' in selection:
            print(f'{students[student_number - 1]['name']}\'s favorite food is {students[student_number - 1]['favorite_food']}')
        else:
            print('That category does not exist. Please try again.')

    elif 'add' in action:
        students.append(get_new_student(students))

    elif 'quit' in action:
        print('Good bye!')
        quit()

    else:
        print('This is not a valid option, please try again.')