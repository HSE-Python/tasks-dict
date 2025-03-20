"""
📌 Task 5: Функция, которая фильтрует словарь по значениям
Напишите функцию filter_dict(d, threshold: int), которая оставляет в словаре только те элементы, 
у которых значение больше threshold.

🔹 Пример работы:
print(filter_dict({"apple": 50, "banana": 20, "cherry": 30}, 25))

Ожидаемый результат:
{'apple': 50, 'cherry': 30}
"""

def filter_dict(d, threshold: int):
    # TODO: Напишите код здесь
    pass

# Тесты
assert filter_dict({"a": 5, "b": 10, "c": 15}, 8) == {"b": 10, "c": 15}
assert filter_dict({}, 3) == {}
assert filter_dict({"one": 100, "two": 200, "three": 50}, 150) == {"two": 200}
assert filter_dict({"x": 0, "y": -10, "z": 5}, 0) == {"z": 5}
