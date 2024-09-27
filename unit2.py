import unittest
import calculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result=calculator.subtract(20,18)
        self.assertEqual(result, 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
