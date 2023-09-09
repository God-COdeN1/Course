# exemple_1
def print_coordinates(x, y, z):
    print("X:", x)
    print("Y:", y)
    print("Z:", z)


coordinates = (10, 20, 30, 40)
print_coordinates(
    *coordinates
)  # Розпаковуємо кортеж і передаємо його елементи як аргументи


# exemple_2
def print_items(*items):
    for item in items:
        print(item)


print_items("apple", "banana", "cherry")  # Упаковуємо аргументи в список items


# exemple_3
def greet(name, message="Hello"):
    print(f"{message}, {name}!")


greet("Alice")  # Виведе: Hello, Alice!
greet("Bob", "Hi")  # Виведе: Hi, Bob!


# exemple_4
def describe_person(name, age, occupation):
    print(f"{name} is {age} years old and works as a {occupation}.")


describe_person(age=30, name="Alice", occupation="teacher")

# exemple_5
x = 10  # Глобальна змінна


def outer():
    y = 20  # Змінна замикання

    def inner():
        z = 30  # Локальна змінна
        print(x + y + z)

    inner()


outer()


# exemple_6
def my_function():
    x = 10  # Локальна змінна
    print(x)


my_function()
# print(x) в цьому місці призведе до помилки, оскільки x - це локальна змінна функції

# exemple_7
x = 10  # Глобальна змінна


def my_function():
    print(x)  # Виведе значення x, оскільки x - глобальна змінна


my_function()
print(x)  # Також виведе значення x


# exemple_8
def greet(name):
    return f"Hello, {name}!"


welcome = greet  # Присвоєння функції змінній

print(welcome("Alice"))  # Виведе: Hello, Alice!


# exemple_9
def apply(func, x):
    return func(x)


def double(n):
    return n * 2


result = apply(double, 5)
print(result)  # Виведе: 10


# exemple_10
def get_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = get_multiplier(2)
triple = get_multiplier(3)

print(double(5))  # Виведе: 10
print(triple(5))  # Виведе: 15


# exemple_11
def square(x):
    return x**2


def cube(x):
    return x**3


functions = [square, cube]

for func in functions:
    print(func(3))  # Виведе: 9, потім 27


# exemple_12
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# exemple_13
def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)
