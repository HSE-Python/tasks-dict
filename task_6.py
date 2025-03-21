"""
📌 Task 6: Функция, которая объединяет два словаря
Напишите функцию merge_dicts(dict1, dict2), которая принимает два словаря 
и объединяет их в один. Если ключ повторяется, значение должно складываться.

🔹 Пример работы:
print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))

Ожидаемый результат:
{'a': 1, 'b': 5, 'c': 4}
"""

def merge_dicts(dict1, dict2):
    # TODO: Напишите код здесь
    pass

# Тесты
assert merge_dicts({"a": 1}, {"a": 2, "b": 3}) == {"a": 3, "b": 3}
assert merge_dicts({}, {}) == {}
assert merge_dicts({"x": 5}, {"x": 10, "y": 20}) == {"x": 15, "y": 20}
assert merge_dicts({"a": 3, "b": 4}, {"a": 2, "c": 5}) == {"a": 5, "b": 4, "c": 5}
