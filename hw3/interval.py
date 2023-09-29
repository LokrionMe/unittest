import unittest


def number_in_interval(n: int) -> bool:
    return 25 < n < 100


class TestInterval(unittest.TestCase):

    def test_number_in_interval(self):
        self.assertTrue(number_in_interval(35))


if __name__ == '__main__':
    unittest.main(verbosity=2)
