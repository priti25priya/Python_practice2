import unittest
import calculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result=calculator.multiply(10,20)
        self.assertEqual(result, 200)  # add assertion here


if __name__ == '__main__':
    unittest.main()
