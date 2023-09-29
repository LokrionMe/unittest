import unittest


def even_odd_number(n: int) -> bool:
    return n % 2 == 0


class TestOdd(unittest.TestCase):

    def test_even_odd_number(self):
        self.assertTrue(even_odd_number(4))


if __name__ == '__main__':
    unittest.main(verbosity=2)
