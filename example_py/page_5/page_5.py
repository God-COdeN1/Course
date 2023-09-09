# exemle_1
my_string = "Hello world!"
print(my_string)

# Спробуєм змінити рядок
my_string[0] = "h"  # Це призведе до помилки, оскільки рядки незмінні

# exemple_2
# Створимо нову змінну зі зміненим першим символом
my_modified_string = "h" + my_string[1:]

# exemple_3
my_string = "Hello world"
print(my_string, id(my_string))
my_string = "hello world"
print(my_string, id(my_string))

# exemple_4
my_string = "Hello, World!"
print(len(my_string))  # Вивід: 13

# exemple_5
my_string = "hello, world!"
print(my_string.upper())  # Вивід: HELLO, WORLD!

# exemple_6
my_string = "HELLO, WORLD!"
print(my_string.lower())  # Вивід: hello, world!

# exemple_7
my_string = "hello, world!"
print(my_string.capitalize())  # Вивід: Hello, world!

# exemple_8
my_string = "hello, world!"
print(my_string.title())  # Вивід: Hello, World!

# exemple_9
my_string = "   Hello, World!   "
print(my_string.strip())  # Вивід: "Hello, World!"

# exemple_10
my_string = "   Hello, World!   "
print(my_string.lstrip())  # Вивід: "Hello, World!   "

# exemple_11
my_string = "   Hello, World!   "
print(my_string.rstrip())  # Вивід: "   Hello, World!"

# exemple_12
my_string = "Hello, World!"
print(my_string.find("World"))  # Вивід: 7
print(my_string.find("Python"))  # Вивід: -1 (not found)

# exemple_13
my_string = "apple,orange,banana"
print(my_string.split(","))  # Вивід: ['apple', 'orange', 'banana']

# exemple_14
my_string = "Hello, hello, hello, world!"
count_hello = my_string.count("hello")
print(count_hello)  # Вивід: 3

# exemple_15
# Об'єднання елементів списку з роздільником ', '
fruits = ["apple", "banana", "orange"]
result = ", ".join(fruits)
print(result)
# Вивід: "apple, banana, orange"

# Об'єднання символів рядка з роздільником ':'
my_string = "hello"
result = ":".join(my_string)
print(result)
# Вивід: "h:e:l:l:o"

# exemple_16
# string[start_index:end_index]

# exemple_17
my_string = "Hello, world!"
# Отримаємо фрагмент рядка з індексом від 0 до 5 (включно)
# Альтернативно, ви можете опустити стартовий індекс, якщо хочете почати з початку:
row_slice = my_string[:5]
print(row_slice)  # Вивід: "Hello"

# exemple_18
# Однорядковий рядок
message = "Hello, World!"

# Багаторядковий рядок
multiline_message = """This is a multi-line
string in Python."""

# exemple_19
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)  # Вивід: John Doe

# exemple_20
escaped_string = "This is a new line.\n\tThis is a tab."
# Вивід:
# This is a new line.
#   This is a tab.

# exemple_21
my_string = "Hello, World!"

if "Hello" in my_string:
    print("Found 'Hello' in the text.")

# exemple_22
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# exemple_23
name = "Bob"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

# exemple_24
name = "Charlie"
age = 28
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)

# exemple_25
name = "David"
age = 35
formatted_string = "My name is {0} and I am {1} years old.".format(name, age)
print(formatted_string)

# exemple_26
name = "Eve"
age = 40
formatted_string = "My name is {name_1} and I am {age_1} years old.".format(
    name_1=name, age_1=age
)
print(formatted_string)

# exemple_27
name = "Frank"
age = 22
formatted_string = "My name is " + name + " and I am " + str(age) + " years old."
print(formatted_string)
