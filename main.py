# coding: utf-8
import os

from framework.module.send_mail.manager.email_manager import EmailManager
from framework.util.debug.debug_util import ILog
from framework.util.file.file_util import FileUtil
from framework.util.system.system_util import SystemUtil


def email_test():

    emailManager = EmailManager()

    emailManager.set_target(FileUtil.load_file(SystemUtil.get_current_project_root_path(), "test.txt"))
    emailManager.create_sender()
    emailManager.start()


if __name__ == '__main__':
    pass
    # email_test()

    # filePath = '/Users/seokho/Desktop/未命名文件夹 2/'
    # for i, j, k in os.walk(filePath):
    #     print(i, j, k)
    target_list = FileUtil.load_file(SystemUtil.get_current_project_root_path(), "tttttt.txt")
    for target in target_list:

        original_target = target

        start_position = target.find("(\"")
        end_position = target.find("\")")

        target_will_replace = target[start_position + 2: end_position]
        target = target[start_position + 2: end_position]

        if target.find("-") != -1:
            dash_position = target.find("-")
            target = target[0: dash_position - 1]

        if target.find("(") != -1 and target.find(")") != -1:
            start_position = target.find("(")
            target = target[0: start_position]

        if len(target) > 4:
            target = target[0: 4]

        # print(target)
        # print(original_target)
        original_target = original_target.replace(target_will_replace, target)
        print(original_target)
        # print(f'{target} {start_position} {end_position}')
