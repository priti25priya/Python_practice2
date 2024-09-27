import unittest
import calculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result=calculator.divide(9,3)
        self.assertEqual(result, 3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
