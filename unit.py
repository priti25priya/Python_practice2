import unittest
import calculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result=calculator.add(10,5)
        self.assertEqual(result, 15)  # add assertion here


if __name__ == '__main__':
    unittest.main()
