# _*_ coding: utf-8 _*_
# @Time : 2023/04/07 5:32 PM
# @Author : Coding with cat
# @File : generate_math_question
# @Project : SHPythonCode

import random

import openpyxl

from framewrok.utility.log_utility import ILog


def generate_math_problem(number: int, symbol: str):
    operators = ["+", "-", "*", "/"]
    number_range = range(1, 10)

    # 生成包含已知的正整数A的简单数学题目，结果等于A
    while True:
        # 生成四个随机数
        numbers = [random.choice(number_range) for i in range(4)]
        # 生成三个随机运算符
        op1, op2 = random.choices(operators, k=2)
        # 计算结果
        result = eval(f"{numbers[0]} {op1} {numbers[1]} {op2} {numbers[2]} {operators[3]} {numbers[3]}")
        # 如果结果等于已知的正整数A，则输出数学题目
        if result == number:
            # problem_str = f"{numbers[0]} {op1} {numbers[1]} {op2} {numbers[2]} {operators[3]} {numbers[3]} = {number}"
            problem_str = f"{symbol} = {numbers[0]} {op1} {numbers[1]} {op2} {numbers[2]} {operators[3]} {numbers[3]}"
            return problem_str


def replace_coordinates(latitude: float, longitude: float):
    lat_str = str(latitude)
    long_str = str(longitude)

    lat_digits = [int(digit) for digit in lat_str.split(".")[1]]
    long_digits = [int(digit) for digit in long_str.split(".")[1]]

    # select two digits to replace in latitude and longitude respectively
    lat_indices = random.sample(range(len(lat_digits)), 2)
    long_indices = random.sample(range(len(long_digits)), 2)

    number_a = lat_digits[lat_indices[0]]
    number_b = lat_digits[lat_indices[1]]
    number_c = long_digits[long_indices[0]]
    number_d = long_digits[long_indices[1]]

    # replace selected digits with A, B, C, D
    lat_digits[lat_indices[0]] = "A"
    lat_digits[lat_indices[1]] = "B"
    long_digits[long_indices[0]] = "C"
    long_digits[long_indices[1]] = "D"

    # construct replaced latitude and longitude strings
    lat_replaced = lat_str.split(".")[0] + "." + "".join(str(digit) for digit in lat_digits)
    long_replaced = long_str.split(".")[0] + "." + "".join(str(digit) for digit in long_digits)

    # construct dictionary of results
    results = {
        "A": number_a,
        "B": number_b,
        "C": number_c,
        "D": number_d,
        "latitude_replaced": lat_replaced,
        "longitude_replaced": long_replaced
    }

    return results


def read_xlsx_file(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    coordinates_list = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[2] is not None and row[3] is not None:
            coordinates = {
                "latitude": row[3],
                "longitude": row[2]
            }
            coordinates_list.append(coordinates)
    return coordinates_list


if __name__ == '__main__':

    # dictionary = replace_coordinates(35.19126547, 129.0653389)
    # ILog.debug(__file__, f"{dictionary['latitude_replaced']}, {dictionary['longitude_replaced']}")
    #
    # ILog.debug(__file__, generate_math_problem(number=dictionary["A"], symbol="A"))
    # ILog.debug(__file__, generate_math_problem(number=dictionary["B"], symbol="B"))
    # ILog.debug(__file__, generate_math_problem(number=dictionary["C"], symbol="C"))
    # ILog.debug(__file__, generate_math_problem(number=dictionary["D"], symbol="D"))

    list = read_xlsx_file("버스정류장.xlsx")
    ILog.debug(__file__, len(list))

    for item in list:
        dictionary = replace_coordinates(item["latitude"], item["longitude"])
        ILog.debug(__file__, f"{dictionary['latitude_replaced']}, {dictionary['longitude_replaced']}")

        ILog.debug(__file__, generate_math_problem(number=dictionary["A"], symbol="A"))
        ILog.debug(__file__, generate_math_problem(number=dictionary["B"], symbol="B"))
        ILog.debug(__file__, generate_math_problem(number=dictionary["C"], symbol="C"))
        ILog.debug(__file__, generate_math_problem(number=dictionary["D"], symbol="D"))

        ILog.debug(__file__, "=======================================")