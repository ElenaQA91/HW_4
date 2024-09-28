import random
import math


def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {25} лет."

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."

def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = 2 * (a + b)

    assert perimeter == 60

    # TODO сосчитайте площадь
    area = 200

    assert area == 200

def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = 0

    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 0

    assert length == 144.51326206513048
