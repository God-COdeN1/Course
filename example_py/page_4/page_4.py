# exemple_1
# while умова:
# Блок коду, який виконується, поки умова істинна

# exemple_2
count = 0
while count < 5:
    print(count)
    count += 1

# exemple_3
user_input = ""
while user_input != "quit":
    user_input = input("Введіть 'quit', щоб завершити: ")

# exemple_4
while True:
    print("Цей цикл ніколи не завершиться!")

# exemple_5
for i in range(1, 6):
    if i == 3:
        continue  # Пропустити ітерацію, коли i = 3
    print(i)

# exemple_6
for i in range(1, 6):
    if i == 3:
        break  # Завершити цикл, коли i = 3
    print(i)

# exemple_7
for i in range(1, 6):
    print(i)
else:
    print("Цикл завершено без використання break.")
# exemple_8
for змінна in послідовність:
    # Блок коду, що виконується для кожного елемента послідовності
# exemple_9
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# exemple_10
def my_function():
    x = 10  # Локальна змінна
    print(x)

my_function()  # Виклик функції

# exempel_11
y = 20  # Глобальна змінна

def my_function():
    local_variable = 10
    print(y)  # Звернення до глобальної змінної

my_function()
print(y)  # Змінна доступна поза функцією
