"""
📌 Task 1: Функция, которая создаёт словарь из двух списков
Напишите функцию create_dict(keys, values), которая принимает два списка:
- keys (список ключей)
- values (список значений)
и возвращает словарь, где ключи берутся из keys, а значения из values.

🔹 Пример работы:
print(create_dict(["name", "age", "city"], ["Alice", 25, "New York"]))

Ожидаемый результат:
{'name': 'Alice', 'age': 25, 'city': 'New York'}
"""

def create_dict(keys, values):
    # TODO: Напишите код здесь
    pass

# Тесты
assert create_dict(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}
assert create_dict(["x", "y"], [10, 20]) == {"x": 10, "y": 20}
assert create_dict([], []) == {}
assert create_dict(["key"], ["value"]) == {"key": "value"}
assert create_dict(["one", "two"], [1]) == {"one": 1}  # Укороченный список values
assert create_dict(["a", "b"], [1, 2, 3]) == {"a": 1, "b": 2}  # Лишний элемент в values игнорируется
