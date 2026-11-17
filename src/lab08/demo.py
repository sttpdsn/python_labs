from models import *
from serialize import *

print("make_student:")
student1 = make_student("Иванова Анна Викторовна", "2008-03-04", "БЭК-26-6-1", 4.0)
print(student1)

print("\nstudent_age:")
print(student_age(student1))

print("\nformat_student:")
print(format_student(student1))

print("\nДесериализация из JSON:")
students_serialized = students_from_json('data/lab08/students_input.json')
for student in students_serialized:
    for field, value in student.items():
        print(f'{field}: {value}')
    print('\n')

students_to_json(students_serialized, 'data/lab08/students_output.json')

print('\nДесериализация из CSV')
data_from_csv = students_from_csv('data/lab08/students_input.csv')
for student in data_from_csv:
    for field, value in student.items():
        print(f'{field}: {value}')
    print('\n')

print("\nupdate_student на неверные данные, вызывается student_from_dict и validate_student, падающий с ошибкой")
try:
    student1_bad = update_student(student1, gpa=-1)
except ValueError as exc:
    print(f"Ошибка: {exc}")


print("\nДесериализация из students_bad.json показывает ошибки во всех полях")
students_from_json('data/lab08/students_bad.json')