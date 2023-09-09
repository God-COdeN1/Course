# exemple_1
x = 10
if x > 5:
    print(
        "x більше за 5"
    )  # Ця інструкція належить до блоку, який виконується, якщо умова x > 5 істинна
else:
    print(
        "x менше або рівний 5"
    )  # Ця інструкція належить до блоку, який виконується, якщо умова x > 5 не є істинною

# exemple_2
a = 5
b = 10
result = a < b  # Це буде True, оскільки 5 менше за 10

# exemple_3
x = True
y = False

result_and = x and y  # Результат буде False, оскільки обидва операнда не є True
result_or = x or y  # Результат буде True, оскільки хоча б один операнд є True
result_not = not x  # Результат буде False, оскільки not інвертує True в False

# exemple_4
if умова:
    # Блок коду, який виконується, якщо умова True
else:
    # Блок коду, який виконується, якщо умова False

# exemple_5
number = 5
if number % 2 == 0:
    print("Це парне число.")
else:
    print("Це непарне число.")

# exemple_6
user_input = int(input("Введіть число: "))
if user_input > 0:
    print("Ви ввели додатне число.")
else:
    print("Ви ввели від'ємне або нуль.")

# exemple_7
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element)

# exemple_8
x = 10
y = 5

if x > y:
    print("x більше за y")
    if x == 10:
        print("x рівний 10")
else:
    print("x менше або рівний y")

# exemple_9
student1 = {"ім'я": "Анна", "оцінки": [85, 90, 78]}
student2 = {"ім'я": "Петро", "оцінки": [92, 88, 95]}
клас = [student1, student2]
