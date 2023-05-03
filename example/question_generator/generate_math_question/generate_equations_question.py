# _*_ coding: utf-8 _*_
# @Time : 2023/05/02 2:37 PM
# @Author : Coding with cat
# @File : generate_equations_question
# @Project : SHPythonCode

import random

from framewrok.utility.log_utility import ILog


# 一元一次
def generate_1_1_equation(x):
    equation = ""
    equation_types = [
        "ax + b = c",
        "ax - b = c",
        "a + bx = c",
        "a - bx = c",
        "a + b = cx",
        "a - b = cx",
        "ax = b + c",
        "ax = b - c",
        "a = bx + c",
        "a = bx - c",
        "a = b + cx",
        "a = b - cx",
    ]

    equation_type = random.choice(equation_types)

    a, b, c = random_a_b_c()

    if "ax + b = c" == equation_type:
        left_result = a * x + b
        right_result = c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x + b
            right_result = c
        equation = f"{a}x + {b} = {c}"
    elif "ax - b = c" == equation_type:
        left_result = a * x - b
        right_result = c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x - b
            right_result = c
        equation = f"{a}x - {b} = {c}"
    elif "a + bx = c" == equation_type:
        left_result = a + b * x
        right_result = c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a + b * x
            right_result = c
        equation = f"{a} + {b}x = {c}"
    elif "a - bx = c" == equation_type:
        left_result = a - b * x
        right_result = c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a - b * x
            right_result = c
        equation = f"{a} - {b}x = {c}"
    elif "a + b = cx" == equation_type:
        left_result = a + b
        right_result = c * x
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a + b
            right_result = c * x
        equation = f"{a} + {b} = {c}x"
    elif "a - b = cx" == equation_type:
        left_result = a - b
        right_result = c * x
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a - b
            right_result = c * x
        equation = f"{a} - {b} = {c}x"
    elif "ax = b + c" == equation_type:
        left_result = a * x
        right_result = b + c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x
            right_result = b + c
        equation = f"{a}x = {b} + {c}"
    elif "ax = b - c" == equation_type:
        left_result = a * x
        right_result = b - c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x
            right_result = b - c
        equation = f"{a}x = {b} - {c}"
    elif "a = bx + c" == equation_type:
        left_result = a
        right_result = b * x + c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a
            right_result = b * x + c
        equation = f"{a} = {b}x + {c}"
    elif "a = bx - c" == equation_type:
        left_result = a
        right_result = b * x - c
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a
            right_result = b * x - c
        equation = f"{a} = {b}x - {c}"
    elif "a = b + cx" == equation_type:
        left_result = a
        right_result = b + c * x
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a
            right_result = b + c * x
        equation = f"{a} = {b} + {c}x"
    elif "a = b - cx" == equation_type:
        left_result = a
        right_result = b - c * x
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a
            right_result = b - c * x
        equation = f"{a} = {b} - {c}x"

    if equation.find("+ -"):
        equation = equation.replace("+ -", "- ")
    if equation.find("- -"):
        equation = equation.replace("- -", "+ ")
    if equation.find("- +"):
        equation = equation.replace("- +", "- ")
    if equation.find("+ +"):
        equation = equation.replace("+ +", "+ ")

    return equation


# 一元一次 (双)
def generate_double_1_1_equation(x):
    equation = ""
    equation_types = [
        "ax + b = cx + d",
        "ax + b = cx - d",
        "ax - b = cx + d",
        "ax - b = cx - d"
    ]

    equation_type = random.choice(equation_types)

    a, b, c, d = random_a_b_c_d()

    if "ax + b = cx + d" == equation_type:
        left_result = a * x + b
        right_result = c * x + d
        while left_result != right_result:
            a, b, c, d = random_a_b_c_d()
            left_result = a * x + b
            right_result = c * x + d
        equation = f"{a}x + {b} = {c}x + {d}"
    elif "ax + b = cx - d" == equation_type:
        left_result = a * x + b
        right_result = c * x - d
        while left_result != right_result:
            a, b, c, d = random_a_b_c_d()
            left_result = a * x + b
            right_result = c * x - d
        equation = f"{a}x + {b} = {c}x - {d}"
    elif "ax - b = cx + d" == equation_type:
        left_result = a * x - b
        right_result = c * x + d
        while left_result != right_result:
            a, b, c, d = random_a_b_c_d()
            left_result = a * x - b
            right_result = c * x + d
        equation = f"{a}x - {b} = {c}x + {d}"
    elif "ax - b = cx - d" == equation_type:
        left_result = a * x - b
        right_result = c * x - d
        while left_result != right_result:
            a, b, c, d = random_a_b_c_d()
            left_result = a * x - b
            right_result = c * x - d
        equation = f"{a}x - {b} = {c}x - {d}"

    if equation.find("+ -"):
        equation = equation.replace("+ -", "- ")
    if equation.find("- -"):
        equation = equation.replace("- -", "+ ")
    if equation.find("- +"):
        equation = equation.replace("- +", "- ")
    if equation.find("+ +"):
        equation = equation.replace("+ +", "+ ")

    return equation


# 一元二次
def generate_1_2_equation(x):
    equation = ""
    equation_types = [
        "ax^2 + bx + c = 0",
        "ax^2 + bx - c = 0",
        "ax^2 - bx + c = 0",
        "ax^2 - bx - c = 0",
    ]

    equation_type = random.choice(equation_types)

    a, b, c = random_a_b_c_big()

    if "ax^2 + bx + c = 0" == equation_type:
        left_result = a * pow(x, 2) + b * x + c
        right_result = 0
        while left_result != right_result:
            a, b, c = random_a_b_c_big()
            left_result = a * pow(x, 2) + b * x + c
            right_result = 0
        equation = f"{a}x\u00b2 + {b}x + {c} = 0"
    elif "ax^2 + bx - c = 0" == equation_type:
        left_result = a * pow(x, 2) + b * x - c
        right_result = 0
        while left_result != right_result:
            a, b, c = random_a_b_c_big()
            left_result = a * pow(x, 2) + b * x - c
            right_result = 0
        equation = f"{a}x\u00b2 + {b}x - {c} = 0"
    elif "ax^2 - bx + c = 0" == equation_type:
        left_result = a * pow(x, 2) - b * x + c
        right_result = 0
        while left_result != right_result:
            a, b, c = random_a_b_c_big()
            left_result = a * pow(x, 2) - b * x + c
            right_result = 0
        equation = f"{a}x\u00b2 - {b}x + {c} = 0"
    elif "ax^2 - bx - c = 0" == equation_type:
        left_result = a * pow(x, 2) - b * x - c
        right_result = 0
        while left_result != right_result:
            a, b, c = random_a_b_c_big()
            left_result = a * pow(x, 2) - b * x - c
            right_result = 0
        equation = f"{a}x\u00b2 - {b}x - {c} = 0"

    if equation.find("+ -"):
        equation = equation.replace("+ -", "- ")
    if equation.find("- -"):
        equation = equation.replace("- -", "+ ")
    if equation.find("- +"):
        equation = equation.replace("- +", "- ")
    if equation.find("+ +"):
        equation = equation.replace("+ +", "+ ")

    return equation


def generate_2_2_equation(x, y):
    equation = ""
    equation_types = [
        "ax + by = c",
        "ax - by = c"
    ]

    equation_type = random.choice(equation_types)

    a, b = random_a_b()

    if "ax + by = c" == equation_type:
        left_result = a * x + b * y
        right_result = random.randint(-1000, 1000)
        while left_result != right_result:
            a, b = random_a_b()
            left_result = a * x + b * y
            right_result = random.randint(-1000, 1000)
        equation = f"{a}x + {b}y = {right_result}"
    elif "ax - by = c" == equation_type:
        left_result = a * x - b * y
        right_result = random.randint(-1000, 1000)
        while left_result != right_result:
            left_result = a * x - b * y
            right_result = random.randint(-1000, 1000)
        equation = f"{a}x - {b}y = {right_result}"

    if equation.find("+ -"):
        equation = equation.replace("+ -", "- ")
    if equation.find("- -"):
        equation = equation.replace("- -", "+ ")
    if equation.find("- +"):
        equation = equation.replace("- +", "- ")
    if equation.find("+ +"):
        equation = equation.replace("+ +", "+ ")

    return equation


def generate_3_3_equation(x, y, z):
    equation = ""
    equation_types = [
        "ax + by + cz = d",
        "ax + by - cz = d",
        "ax - by + cz = d",
        "ax - by - cz = d",
    ]

    equation_type = random.choice(equation_types)

    a, b, c = random_a_b_c()

    if "ax + by + cz = d" == equation_type:
        left_result = a * x + b * y + c * z
        right_result = random.randint(-1000, 1000)
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x + b * y + c * z
            right_result = random.randint(-1000, 1000)
        equation = f"{a}x + {b}y + {c}z = {right_result}"
    elif "ax + by - cz = d" == equation_type:
        left_result = a * x + b * y - c * z
        right_result = random.randint(-1000, 1000)
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x + b * y - c * z
            right_result = random.randint(-1000, 1000)
        equation = f"{a}x + {b}y - {c}z = {right_result}"
    elif "ax - by + cz = d" == equation_type:
        left_result = a * x - b * y + c * z
        right_result = random.randint(-1000, 1000)
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x - b * y + c * z
            right_result = random.randint(-1000, 1000)
        equation = f"{a}x - {b}y + {c}z = {right_result}"
    elif "ax - by - cz = d" == equation_type:
        left_result = a * x - b * y - c * z
        right_result = random.randint(-1000, 1000)
        while left_result != right_result:
            a, b, c = random_a_b_c()
            left_result = a * x - b * y - c * z
            right_result = random.randint(-1000, 1000)
        equation = f"{a}x - {b}y - {c}z = {right_result}"

    if equation.find("+ -"):
        equation = equation.replace("+ -", "- ")
    if equation.find("- -"):
        equation = equation.replace("- -", "+ ")
    if equation.find("- +"):
        equation = equation.replace("- +", "- ")
    if equation.find("+ +"):
        equation = equation.replace("+ +", "+ ")

    return equation


def random_a_b_c_big():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    return a, b, c


def random_a_b():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    return a, b


def random_a_b_c():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    return a, b, c


def random_a_b_c_d():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    d = random.randint(-10, 10)
    return a, b, c, d


if __name__ == '__main__':
    # ILog.debug(__file__, "when x = 6")
    # results = generate_1_1_equation(x=6)
    # ILog.debug(__file__, results)
    #
    # ILog.debug(__file__, "=========\n")
    #
    # ILog.debug(__file__, "when x = 3")
    # results = generate_1_1_equation(x=3)
    # ILog.debug(__file__, results)
    #
    # ILog.debug(__file__, "=========\n")
    #
    # ILog.debug(__file__, "when x = 5")
    # results = generate_double_1_1_equation(x=5)
    # ILog.debug(__file__, results)
    #
    # ILog.debug(__file__, "=========\n")
    #
    # ILog.debug(__file__, "when x = 9")
    # results = generate_double_1_1_equation(x=9)
    # ILog.debug(__file__, results)

    # ILog.debug(__file__, "when x = 7")
    # results = generate_1_2_equation(x=7)
    # ILog.debug(__file__, results)

    ILog.debug(__file__, "when x = 1, y = 2")
    results = generate_2_2_equation(x=1, y=2)
    ILog.debug(__file__, results)
    results = generate_2_2_equation(x=1, y=2)
    ILog.debug(__file__, results)

    # ILog.debug(__file__, "when x = 1, y = 2, z = 3")
    # results = generate_3_3_equation(x=1, y=2, z=3)
    # ILog.debug(__file__, results)
    # results = generate_3_3_equation(x=1, y=2, z=3)
    # ILog.debug(__file__, results)
    # results = generate_3_3_equation(x=1, y=2, z=3)
    # ILog.debug(__file__, results)


