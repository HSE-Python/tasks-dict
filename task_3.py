"""
📌 Task 3: Функция, которая переворачивает ключи и значения в словаре
Напишите функцию reverse_dict(d), которая меняет местами ключи и значения в словаре.

🔹 Пример работы:
print(reverse_dict({"a": 1, "b": 2, "c": 3}))

Ожидаемый результат:
{1: 'a', 2: 'b', 3: 'c'}
"""

def reverse_dict(d):
    # TODO: Напишите код здесь
    pass

# Тесты
assert reverse_dict({"x": 10, "y": 20}) == {10: "x", 20: "y"}
assert reverse_dict({}) == {}
assert reverse_dict({"apple": "red", "banana": "yellow"}) == {"red": "apple", "yellow": "banana"}
assert reverse_dict({1: "one", 2: "two", 3: "three"}) == {"one": 1, "two": 2, "three": 3}
