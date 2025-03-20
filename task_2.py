"""
📌 Task 2: Функция, которая считает количество вхождений элементов в список
Напишите функцию count_elements(lst), которая принимает список и 
возвращает словарь, где ключи – элементы списка, а значения – их количество вхождений.

🔹 Пример работы:
print(count_elements(["apple", "banana", "apple", "orange", "banana", "banana"]))

Ожидаемый результат:
{'apple': 2, 'banana': 3, 'orange': 1}
"""

def count_elements(lst):
    # TODO: Напишите код здесь
    pass

# Тесты
assert count_elements(["a", "b", "a", "c", "b", "b"]) == {"a": 2, "b": 3, "c": 1}
assert count_elements([]) == {}
assert count_elements(["one", "two", "one", "three"]) == {"one": 2, "two": 1, "three": 1}
assert count_elements([1, 2, 3, 1, 2, 1, 1, 3]) == {1: 4, 2: 2, 3: 2}
assert count_elements(["same", "same", "same"]) == {"same": 3}
