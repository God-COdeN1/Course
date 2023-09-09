# exemple_1
my_set = set([1, 2, 3, 4, 4, 4])  # Створення множини зі списку
my_set.add(5)  # Додавання нового елемента
my_set.remove(2)  # Видалення елемента

# exemple_2
frozen_set = frozenset([1, 2, 3, 4])  # Створення незмінного множини
another_set = {frozen_set, 5, 6}  # Використання незмінної множини в іншій множині

# exemple_3
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)  # Вивід: {1, 2, 3}

# exemple_4
my_set = {1, 2, 3}
my_set.remove(2)
my_set.discard(3)  # Вивід: {1}

# exemple_5
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2
# Або
result = set1.union(set2)
print(result)  # Вивід: {1, 2, 3, 4, 5}

# exemple_6
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2
# Або
result = set1.intersection(set2)
print(result)  # Вивід: {3}

# exemple_7
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 - set2
# Або
result = set1.difference(set2)
print(result)  # Вивід: {1, 2}

# exemple_8
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2
# Або
result = set1.symmetric_difference(set2)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2
print(result)  # Вивід: {1, 2, 4, 5}

# exemple_9
set1 = {1, 2}
set2 = {1, 2, 3, 4}
is_subset = set1.issubset(set2)
is_superset = set2.issuperset(set1)
print(is_subset)  # Вивід: True
print(is_superset)  # Вивід: True

# exemple_10
my_set = {1, 2, 3}
contains_element = 2 in my_set
print(contains_element)  # Вивід: True

# exemple_11
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
print(unique_elements)  # Вивід: {1, 2, 3, 4, 5}

# exemple_12
my_set = {1, 2, 3, 4, 5}
if 3 in my_set:
    print("Елемент 3 є в множині")

# exemple_13
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(my_list))
print(unique_elements)  # Вивід: [1, 2, 3, 4, 5]

# exemple_14
student_data = {"John": 25, "Jane": 22, "Tom": 25, "Alice": 21}
unique_ages = set(student_data.values())
print(unique_ages)  # Вивід: {25, 22, 21}

# exemple_15
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
common_elements = set1 & set2
print(common_elements)  # Вивід: {3, 4, 5}
