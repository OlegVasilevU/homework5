#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var = 1, 2, 3, 'Имя', 'Фамилия', 'Отчество'
print(tuple(immutable_var))
# immutable_var[1] = 5 # Не дает изменить обьект, тк кортеж неизменяемый.
# И не поддерживает обращение по элементам. TypeError: 'tuple' object does not support item assignment
mutable_list = [1, 2, 3, 'Имя', 'Фамилия', 'Отчество']
mutable_list[1] = 4
mutable_list[2] = 'Список'
mutable_list.remove('Отчество')
mutable_list.append('Год рождения')
print(mutable_list)