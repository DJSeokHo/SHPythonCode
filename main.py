# _*_ coding: utf-8 _*_
# @Time : 2022/08/02 10:56 PM
# @Author : Coding with cat
# @File : main
# @Project : SHPythonCode
import openpyxl

from framewrok.utility.log_utility import ILog
import os
from PIL import Image

def compress_png_images(input_folder: str, output_folder: str, target_size: tuple[int, int]):
    """
    遍历 input_folder 目录，压缩所有 PNG 图片到指定分辨率，并保存在 output_folder。

    :param input_folder: 图片所在文件夹
    :param output_folder: 处理后的图片保存路径
    :param target_size: (width, height) 目标分辨率
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                image = Image.open(input_path)

                # 等比例缩放
                image.thumbnail(target_size, Image.LANCZOS)

                # 无损压缩保存 PNG
                image.save(output_path, format="PNG", optimize=True)

                print(f"✔ {filename} 处理完成，保存至 {output_path}")
            except Exception as e:
                print(f"❌ 处理 {filename} 时出错: {e}")


import opencc

def convert_simplified_to_traditional(input_file: str, output_file: str):
    """
    读取文本文件，将其中的简体中文转换为繁体中文，结果保存到另一个文件中。

    :param input_file: 输入的文本文件路径
    :param output_file: 输出的文本文件路径，保存转换后的繁体文本
    """
    # 创建转换器
    converter = opencc.OpenCC('s2t.json')  # 简体转繁体

    try:
        # 读取原始文本
        with open(input_file, 'r', encoding='utf-8') as file:
            simplified_text = file.read()

        # 转换简体中文到繁体中文
        traditional_text = converter.convert(simplified_text)

        # 保存转换后的内容到新的文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(traditional_text)

        print(f"简体中文已转换为繁体中文，保存到 {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")


# 示例使用

if __name__ == '__main__':
    ILog.debug(__file__, "test")
    # GIFUtility.make_gif("images", gif_name="haetae.gif")
    # compress_png_images("temp_image", "temp_image/compress", (200, 200))

    convert_simplified_to_traditional('temp_file/nation_code.dart', 'temp_file/nation_code_new.dart')

