import getopt
import sys
import random
from fractions import Fraction


def change(a):   # *,/ 转成 ×，÷
    if a == '*':
        a = '×'
    elif a == '/':
        a = '÷'
    return a


def problem(area=10):  # 随机生成一道题目(自然数四则运算或分数运算)，运算符不超过3个
    operator_num = random.randint(1, 3)  # 随机运算符
    flag = random.randint(1, 2)  # 随机四则或分数
    if flag == 1:  # 四则
        expression = print_expression = str(random.randint(1, area))  # 1
        bracket = (random.choice(['(', '']) if not operator_num == 1 else '')  # 单运算符不用加括号
        for i in range(operator_num):  # 随机个运算符 （自然数四则运算）
            op = str(random.choice(operators))
            num = str(random.randint(1, area))  # 数值不超过area
            if bracket == ')':  # 右括号在数字右边
                print_expression += change(op) + num + bracket  # 输出的表达式  1×2
                expression += op + num + bracket  # 计算的表达式 1*2
            else:  # 左括号在数字左边
                print_expression += change(op) + bracket + num
                expression += op + bracket + num
            bracket = (')' if bracket == '(' else '')
        results = eval(expression)  # 运算结果
    else:  # 分数
        expression = print_expression = str(Fraction(random.randint(1, area), random.randint(1, area)))  # 1
        bracket = (random.choice(['(', '']) if not operator_num == 1 else '')
        for i in range(operator_num):
            op = str(random.choice(operators))
            num = Fraction(random.randint(1, area), random.randint(1, area))  # 分数
            if bracket == ')':
                if float(num) > 1:  # 假分数转带分数
                    print_expression += change(op) + str(int(num)) + '’' + str(num - int(num)) + bracket  # 3/2 -> 1'1/2
                else:
                    print_expression += change(op) + str(num) + bracket  # 输出的表达式
                expression += op + str(num) + bracket
            else:
                if float(num) > 1:
                    print_expression += change(op) + bracket + str(int(num)) + '’' + str(num - int(num))
                else:
                    print_expression += change(op) + bracket + str(num)
                expression += op + bracket + str(num)  # 计算的表达r式 1*2
            bracket = (')' if bracket == '(' else '')
        results = round(eval(expression), 3)
    if results >= 0 and results not in open('results.txt', 'a+'):  # 结果不为负, 答案不重复
        print(expression)
        open('problems.txt', 'a+').write(print_expression+'='+str(results)+'\n')  # 存放题目
        open('results.txt', 'a+').write(str(results) + '\n')  # 存放答案
        print(print_expression+'='+str(results))
    else:
        problem()


def compare(txt_list):  # 对比题目和答案文件
    correct = wrong = []
    for i in range(len(open(txt_list[1], 'r').readlines())):
        result = open(txt_list[1], 'r').readlines()[i]
        problem = open(txt_list[0], 'r').readlines()[i]
        correct.append(i + 1) if result[:-1] == (problem[problem.index('=')+1:-1]) else wrong.append(i+1)
    print('Correct: {}{}'.format(len(correct), tuple(correct))+'\n' + 'Wrong: {}{}'.format(len(wrong), tuple(wrong)))


opts, args = getopt.getopt(sys.argv[1:], "hn:r:e:a:")
print(opts, args)
operators = ['+', '-', '*', '/']
if '-r' in opts[len(opts)-1]:  # 题目数值范围
    problem_num = opts[0][1]
    area = opts[1][1]
    for j in range(int(problem_num)):
        problem(area=int(area))
elif '-n' in opts[0]:  # 参数控制生成题目的个数（必须）
    problem_num = opts[0][1]
    for j in range(int(problem_num)):
        problem()
if '-e' in opts[0] or '-a' in opts[0]:
    txt_list = []  # 题目文件和答案文件
    for i in opts:
        txt_list.append(i[1])
    compare(txt_list)
    print(txt_list)
