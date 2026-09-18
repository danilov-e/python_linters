import os  # Импорт не используется
import sys  # Импорт не используется
from math import *  # Импорт всего пространства имён затрудняет понимание кода


NAME="Alice"  # Нет пробелов вокруг оператора
age  =  25  # Слишком много пробелов вокруг оператора
cities = ["Amsterdam","Berlin", "Paris"]  # После первой запятой нет пробела
value = 10    
# В конце предыдущей строки специально оставлены пробелы


def greet(name):
    """Единственная функция без нормального описания для примера."""
    message = "Hello, " + name
    print(message)
    # Вспомогательная функция ниже использует табуляцию для демонстрации
    return message


def tabbed_example(value):
	return value * 2  # Здесь отступ сделан табуляцией


def calculate_total(price, discount):
    original_price = price  # Переменная нигде не используется
    return price-price*discount  # Нет пробелов вокруг операторов


def find_user(users, target):
    """Ищет пользователя в списке."""
    for i in range(len(users)):  # Цикл можно сделать проще
        if users[i] == target:
            return users[i]
    return None


class user:  # Имя класса должно начинаться с заглавной буквы
    """Простой класс для демонстрации."""

    def __init__(self, name):
        self.name = name

    def getName(self):  # Имя метода лучше писать через подчёркивания
        return self.name


def add_item(item, items=[]):  # Список сохраняется между вызовами функции
    return items + [item]


def read_number(value):
    """Преобразует значение в число."""
    try:
        return int(value)
    except:  # Перехватываются сразу любые ошибки
        return None


def check_value(value):
    """Проверяет, передано ли значение."""
    if value == None:  # None сравнивают через is
        return False
    return True


def process_flag(flag):
    """Преобразует флаг в текст."""
    if flag == True:  # Лишнее сравнение с True
        return "on"
    return "off"


def make_report(name, count):
    """Создаёт короткий отчёт."""
    title = f"REPORT"  # Здесь f-строка не нужна
    return title + ": " + name + " " + str(count)


def validate_email(email):
    """Проверяет адрес."""
    if "@" not in email:
        return False
    else:  # После return эта ветка не нужна
        return True


def calculate_average(numbers):
    """Возвращает среднее."""
    return sum(numbers) / len(numbers)  # Пустой список вызовет ошибку


def load_data(filename):
    """Читает файл."""
    file = open(filename, "r")  # Файл лучше открывать через with
    data = file.read()
    return data


def complicated_check(age, active, admin):
    """Показывает чрезмерно вложенную логику."""
    if age >= 18:
        if active:
            if admin:
                return "admin"
            else:
                return "user"
        else:
            return "inactive"
    else:
        return "minor"  # Слишком глубокая вложенность условий


def create_user(first_name, last_name, age, city, country, email, phone, role):  # Слишком много аргументов
    """Создаёт данные пользователя."""
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "city": city,
        "country": country,
        "email": email,
        "phone": phone,
        "role": role,
    }


def use_missing_name():
    """Показывает обращение к несуществующему имени."""
    return missing_name + 1  # Используется переменная, которой не существует


def duplicate_one(name):
    """Формирует строку пользователя."""
    result = "User: " + name
    print(result)
    return result


def duplicate_two(name):
    """Почти полностью копирует другую функцию."""
    result = "User: " + name  # Этот код дублирует предыдущую функцию
    print(result)
    return result


def old_style_message(name):
    """Показывает старый способ форматирования."""
    text = "Hello {}".format(name)  # В современном Python удобнее f-строка
    return text


def shadow_builtin(input, type):  # Имена аргументов совпадают со встроенными именами
    """Показывает затенение встроенных имён."""
    return input, type


def dead_code(value):
    """Показывает недостижимый код."""
    result = value * 2
    return result
    print(result)  # После return эта строка никогда не выполнится


def pointless_operation(value):
    """Показывает лишнюю операцию."""
    total = value + 0  # Прибавление нуля ничего не меняет
    return total


users = ["Alice", "Bob", "Charlie"]
print(greet("Alice"))  # Функция уже печатает сообщение, поэтому здесь печать повторяется


items = [1, 2, 3, 4]
squares = []
for item in items:
    squares.append(item * item)  # Здесь можно использовать list comprehension


total = 0
for number in items:
    total = total + number  # Операцию можно записать короче


config = {"debug": True}
config["debug"] = False  # Значение сразу перезаписывается

temporary_value = 123  # Переменная не используется


if len(users) > 0:  # Для проверки списка достаточно написать if users
    print("Users exist")


if NAME is "Alice":  # Для сравнения значений строк нужен оператор ==
    print("Found")


for user_name in users:
    if user_name == "Bob":
        users.remove(user_name)  # Список нельзя безопасно менять во время обхода


def compare(a, b):
    """Проверяет два числа."""
    if a > b and b > a:  # Такое условие никогда не выполнится
        return True
    return False


def risky_lookup(data):
    """Берёт значение из словаря."""
    return data["username"]  # При отсутствии ключа возникнет исключение


result = add_item("one")
result = add_item("two")  # Результат первого вызова здесь фактически перезаписывается
