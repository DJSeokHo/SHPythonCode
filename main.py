# coding: utf-8
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
    email_test()
