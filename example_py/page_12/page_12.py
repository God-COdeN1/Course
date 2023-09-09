# exemple_1
my_tuple = (1, 2, 3, "hello", 4.5)

# exemple_2
print(my_tuple[0])  # Виведе: 1
print(my_tuple[3])  # Виведе: hello

# exemple_3
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[0][1])  # Виведе: 2
print(nested_tuple[1][0])  # Виведе: 3

# exemple_4
# Кортеж як координати точки на площині
point = (3, 5)
x, y = point
print("X координата:", x)
print("Y координата:", y)


# Повернення декількох значень з функції
def get_name_and_age():
    name = "John"
    age = 30
    return name, age


name, age = get_name_and_age()
print("Ім'я:", name)
print("Вік:", age)

# Використання кортежів як ключів у словниках
student_grades = {("John", "Doe"): 85, ("Jane", "Smith"): 92}
print(student_grades[("John", "Doe")])


# Передача декількох аргументів у функцію
def print_coordinates(x, y):
    print("X координата:", x)
    print("Y координата:", y)


coordinates = (4, 7)
print_coordinates(*coordinates)

# Зберігання даних для обробки великої кількості даних
data = ([1, 2, 3], ("apple", "banana", "cherry"), {"name": "John", "age": 25})

list_data, tuple_data, dict_data = data
print("Список даних:", list_data)
print("Кортеж даних:", tuple_data)
print("Словник даних:", dict_data)
