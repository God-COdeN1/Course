# exemple_1
lambda arguments: expression

# exemple_2
# Оголошення анонімної функції, яка додає два числа
add = lambda x, y: x + y

result = add(5, 3)
print(result)  # Виводить 8

# exemple_3
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
squared_list = list(squared)  # [1, 4, 9, 16, 25]

# exemple_4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_list = list(even_numbers)  # [2, 4, 6, 8, 10]

# exemple_5
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)  # 120 (1 * 2 * 3 * 4 * 5)

# exemple_6
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
zipped = zip(names, scores)
zipped_list = list(zipped)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# exemple_7
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

# exemple_8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# exemple_9
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)

# exemple_10
names = ["Alice", "Bob", "Charlie"]
sorted_names = sorted(names, key=lambda x: len(x))


# exemple_11
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure_instance = outer_function(10)
result = closure_instance(5)  # Виклик inner_function зі змінною x=10
print(result)  # Виведе 15
