# exemple_1
empty_dict = {}

# exemple_2
student = {"ім'я": "Богдан", "вік": 20, "курс": 3, "спеціальність": "Комп'ютерні науки"}

# exemple_3
student = dict(ім_я="Богдан", вік=20, курс=3, спеціальність="Комп'ютерні науки")
# або
student = dict(
    [
        ("ім'я", "Богдан"),
        ("вік", 20),
        ("курс", 3),
        ("спеціальність", "Комп'ютерні науки"),
    ]
)

# exemple_4
key = "продукт"
value = "яблуко"
my_dict = {key: value}

# exemple_5
my_dict = {}
my_dict["ключ1"] = "значення1"
my_dict["ключ2"] = "значення2"

# exemple_6
name = "Богдан"
age = 25

# exemple_7
person = {"ім'я": name, "вік": age}

# exemple_8
my_dict = {"ключ1": "значення1", "ключ2": "значення2"}
my_dict.clear()
print(my_dict)  # {}

# exemple_9
original = {"a": 1, "b": 2}
copy_dict = original.copy()

# exemple_10
my_dict = {"ім'я": "Іван", "вік": 25}
name = my_dict.get("ім'я", "Невідомо")  # Іван
height = my_dict.get("зріст", "Невідомо")  # Невідомо

# exemple_11
my_dict = {"ім'я": "Іван", "вік": 25}
keys = my_dict.keys()  # Вертає dict_keys(["ім'я", "вік"])

# exemple_12
my_dict = {"ім'я": "Іван", "вік": 25}
values = my_dict.values()  # Вертає dict_values(["Іван", 25])

# exemple_13
my_dict = {"ім'я": "Іван", "вік": 25}
items = my_dict.items()  # Вертає dict_items([("ім'я", "Іван"), ("вік", 25)])

# exemple_14
my_dict = {"ім'я": "Іван", "вік": 25}
age = my_dict.pop("вік")  # Видаляє "вік" та повертає 25

# exemple_15
my_dict = {"ім'я": "Іван", "вік": 25}
item = my_dict.popitem()  # Видаляє та повертає ("вік", 25)

# exemple_16
my_dict = {"ім'я": "Іван"}
extra_info = {"вік": 25, "спеціальність": "Комп'ютерні науки"}
my_dict.update(extra_info)

# exemple_17
student = {"ім'я": "Іван", "вік": 20, "курс": 3, "спеціальність": "Комп'ютерні науки"}

# Додавання нової пари ключ-значення
student["середній_бал"] = 4.5

# exemple_18
name = student["ім'я"]
age = student.get("вік")

# exemple_19
student["вік"] = 21

# exemple_20
del student["курс"]

# exemple_21
if "спеціальність" in student:
    print("Студент має спеціальність")

# exemple_22
for key in student:
    print("Ключ:", key, "Значення:", student[key])

for value in student.values():
    print("Значення:", value)

for key, value in student.items():
    print("Ключ:", key, "Значення:", value)

# exemple_23
keys = student.keys()
values = student.values()

# exemple_24
extra_info = {"стать": "чоловіча", "зріст": 180}
student.update(extra_info)
