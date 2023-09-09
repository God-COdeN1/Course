# exemple_1
from array import array

# exemple_2
my_array = array("i", [1, 2, 3, 4, 5])

# exemple_3
from array import array

my_int_array = array("i", [1, 2, 3, 4, 5])
my_float_array = array("f", [0.1, 0.2, 0.3, 0.4, 0.5])
my_unicode_array = array("u", ["a", "b", "c", "d", "e"])

# exemple_4
print(my_array[0])  # Виведе: 1
print(my_array[2])  # Виведе: 3

# exemple_5
my_array.append(6)  # Додає елемент 6 в кінець масиву
my_array.remove(2)  # Видаляє перший знайдений елемент зі значенням 2
my_array[3] = 10  # Змінюємо значення 4-го елемента на 10

# exemple_6
print(len(my_array))  # Виведе: 5
for element in my_array:
    print(element)  # Виведе всі елементи масиву по черзі

# exemple_7
my_list = [1, 2, 3, "Hello", True]

# exemple_8
my_tuple = (1, 2, "Hello")

# exemple_9
my_dict = {"name": "John", "age": 30, "city": "New York"}

# exemple_10
my_set = {1, 2, 3, 4, 5}

# exemple_11
# Створення пустого списку
my_list = []

# Додавання елементів по одному
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)  # Виведе: [1, 2, 3]

# exemple_12
# Створення списку з визначеними значеннями
fruits = ["apple", "banana", "orange", "grape"]

print(fruits)  # Виведе: ['apple', 'banana', 'orange', 'grape']

# exemple_13
mixed_list = [1, "hello", 3.14, True]

print(mixed_list)  # Виведе: [1, 'hello', 3.14, True]

# exemple_14
my_tuple = (10, 20, 30)
converted_list = list(my_tuple)

print(converted_list)  # Виведе: [10, 20, 30]

# exemple_15
# Списковий вираз для створення списку квадратів чисел від 1 до 5
squares = [x**2 for x in range(1, 6)]

print(squares)  # Виведе: [1, 4, 9, 16, 25]

# exemple_16
# [вираз for елемент in ітерабельний об'єкт if умова]

# exemple_17
numbers = [x for x in range(10)]
# Результат: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# exemple_18
squares = [x**2 for x in range(1, 6)]
# Результат: [1, 4, 9, 16, 25]

# exemple_19
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
# Результат: [2, 4, 6, 8]

# exemple_20
string = "Hello, World!"
characters = [ch for ch in string]
# Результат: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']

# exemple_21
my_list.append(6)  # Додаємо 6 в кінець списку
my_list.insert(2, 7)  # Додаємо 7 на позицію 2 (індексуючи з 0)

# exemple_22
my_list.remove(3)  # Видаляємо перший елемент зі значенням 3
popped_element = my_list.pop()  # Видаляємо та повертаємо останній елемент

# exemple_23
my_list[1] = 10  # Змінюємо елемент з індексом 1 на 10

# exemple_24
element = my_list[3]  # Отримуємо елемент з індексом 3

# exemple_25
for item in my_list:
    print(item)

# exemple_26
length = len(my_list)

# exemple_27
my_list.sort()  # Сортуємо список за зростанням
my_list.sort(reverse=True)  # Сортуємо список за спаданням
sorted_list = sorted(my_list)  # Створюємо новий список з відсортованими елементами

# exemple_28
index = my_list.index(4)  # Знаходимо індекс першого елемента зі значенням 4

# exemple_29
new_list = my_list + [8, 9, 10]

# exemple_30
my_list.clear()  # видаляє всі елементи зі списку, робить його пустим

# exemple_31
my_list = [1, 2, 3, 4, 5]

# exemple_32
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Створимо список для подальших прикладів

my_list.append(8)
print(my_list)  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]

# exemple_33
my_list.insert(2, 7)
print(my_list)  # [3, 1, 7, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]

# exemple_34
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]

# exemple_35
my_list.remove(9)
print(my_list)  # [3, 1, 7, 4, 1, 5, 2, 6, 5, 3, 5, 8]

# exemple_36
popped_value = my_list.pop(4)
print(popped_value)  # 1
print(my_list)  # [3, 1, 7, 4, 5, 2, 6, 5, 3, 5, 8]

# exemple_37
index_of_5 = my_list.index(5)
print(index_of_5)  # 4

# exemple_38
index_of_5 = my_list.index(5)
print(index_of_5)  # 4

# exemple_39
my_list.sort()
print(my_list)  # [1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8]

# exemple_40
my_list.reverse()
print(my_list)  # [8, 7, 6, 5, 5, 5, 4, 3, 3, 2, 1]

# exemple_41
my_list_copy = my_list.copy()
print(my_list_copy)

# exemple_42
my_list.clear()
print(my_list)  # []

# exemple_43
length = len(my_list)
print(length)  # 8

# exemple_44
maximum = max(my_list)
print(maximum)  # 8

# exemple_45
minimum = min(my_list)
print(minimum)  # 1

# exemple_46
total = sum(my_list)
print(total)  # 15

# exemple_47
if 3 in my_list:
    print("3 is in the list")
else:
    print("3 is not in the list")

if 10 not in numbers:
    print("10 is not in the list")

# exemple_48
fruits = ["apple", "banana", "orange", "grape", "pear"]

if "banana" in fruits:
    print("Banana is in the list")
else:
    print("Banana is not in the list")

if "kiwi" not in fruits:
    print("Kiwi is not in the list")
else:
    print("Kiwi is in the list")

# exemple_49
list1 = [1, 2, 3]
list2 = list1  # list2 тепер також вказує на той самий об'єкт, що і list1

list1.append(4)
print(list2)  # [1, 2, 3, 4], зміна була відображена і в list2

# exemple_50
original_list = [1, 2, 3]
clone_list = original_list.copy()  # Створюємо копію списку

original_list.append(4)
print(clone_list)  # [1, 2, 3], клон не був змінений

# exemple_51
original_list = [1, 2, 3]
clone_list = original_list[:]  # Створюємо копію списку за допомогою зрізу

original_list.append(4)
print(clone_list)  # [1, 2, 3], клон не був змінений

# exemple_52
my_list = [10, 20, 30, 40, 50]

search_item = 30
found = False

for item in my_list:
    if item == search_item:
        found = True
        break

if found:
    print("Item found")
else:
    print("Item not found")

# exemple_53
my_list = [10, 20, 30, 40, 50]

search_item = 30

if search_item in my_list:
    print("Item found")
else:
    print("Item not found")

# exemple_54
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][2])  # Доступ до елемента у другому рядку та третьому стовпці (6)

# exemple_55
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix[1, 2])  # Доступ до елемента у другому рядку та третьому стовпці (6)
