# _*_ coding: utf-8 _*_
# @Time : 2023/01/02 2:37 PM
# @Author : Coding with cat
# @File : gif_utility
# @Project : SHPythonCode
import os

import imageio


class GIFUtility:

    @staticmethod
    def make_gif(path: str, gif_name: str = "gif.gif"):
        _pic_lst = os.listdir(path)

        _final_pic_lst = []
        for pic in _pic_lst:
            if pic.endswith(".png") or pic.endswith(".jpg") or pic.endswith(".jpeg"):
                _final_pic_lst.append(pic)

        gif_images = []
        for name in _final_pic_lst:
            filename = os.path.join(path, name)
            gif_images.append(imageio.imread(filename))  # 读取图片

        imageio.mimsave(gif_name, gif_images, 'GIF', duration=0.5)
