"""
📌 Task 5: Функция, которая считает средний балл студентов
Напишите функцию average_scores(scores), которая принимает словарь {имя: список оценок} и 
возвращает новый словарь {имя: средний балл}.

🔹 Пример работы:
print(average_scores({"Alice": [90, 80, 85], "Bob": [70, 75, 80]}))

Ожидаемый результат:
{'Alice': 85.0, 'Bob': 75.0}
"""

def average_scores(scores):
    # TODO: Напишите код здесь
    pass

# Тесты
assert average_scores({"Alice": [90, 80, 85], "Bob": [70, 75, 80]}) == {"Alice": 85.0, "Bob": 75.0}
assert average_scores({}) == {}
assert average_scores({"John": [50, 60, 70], "Mike": [80, 85, 90]}) == {"John": 60.0, "Mike": 85.0}
assert average_scores({"Sam": [100], "Chris": [50, 60]}) == {"Sam": 100.0, "Chris": 55.0}
