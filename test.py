import unittest
from calculator import *


class CalculatorTest(unittest.TestCase):
    # 生成题目数是否符合预期
    def test_problems_num(self):
        nums, problem_num = run([('-n', '10'), ('-r', '10')])
        self.assertEqual(nums, problem_num)

    # 运算符转换
    def test_change(self):
        self.assertEqual('×', change('*'))


if __name__ == '__main__':
    unittest.main()
