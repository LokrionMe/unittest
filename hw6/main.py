'''Модуль представляет из себя функцию для проверки среднего значения
двух списков и класса для тестирования данной функции
pylint выдает: 'Your code has been rated at 9.29/10'
покрытие тестами состовляет ~ 93%
'''
import unittest

def mid_val(list_one: list, list_two: list):
    """Скрипт сравнивает средние значения от каждого списка
    и выдает информацию у какого списка среднее значение больше"""
    if len(list_one) == 0 or len(list_two) == 0:
        return "List must have one or more values"
    if sum(list_one)/len(list_one) > sum(list_two)/len(list_two):
        return "The first list has a larger average value"
    if sum(list_one)/len(list_one) < sum(list_two)/len(list_two):
        return "The second list has a larger average value"
    return "The average values are equal"


class TestMidVal(unittest.TestCase):

    def test_zero_values(self):
        '''Тест на пустой список'''
        a = []
        b = [1, 2]
        self.assertEqual(mid_val(a, b), 'List must have one or more values')

    def test_second_large(self):
        '''Тест на большее среднее второго списка'''
        a = [1, 2, 3]
        b = [3, 4, 5]
        self.assertEqual(
            mid_val(a, b), "The second list has a larger average value")

    def test_first_large(self):
        '''Тест на большее среднее первого списка'''
        a = [4, 5, 6]
        b = [1, 2, 3]
        self.assertEqual(
            mid_val(a, b), "The first list has a larger average value")

    def test_equal(self):
        '''Тест на равенство среднего двух списков'''
        a = [1, 2, 3]
        b = [1, 2, 3]
        self.assertEqual(mid_val(a, b), 'The average values are equal')


if __name__ == '__main__':
    unittest.main(verbosity=2)
