# coding: utf-8
import os

from framework.util.debug.debug_util import ILog


class FileUtil:

    __TAG = "FileUtil"

    @staticmethod
    def storage_file_bytes(folder_path, file_name, file_bytes):

        try:

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            f = open(os.path.join(folder_path, file_name), "wb")
            f.write(file_bytes)
            f.close()
            return True
        except Exception as e:
            print(str(e))
            return False

    @staticmethod
    def load_file(folder_path, file_name):

        content_list = []

        try:
            if not os.path.exists(folder_path):
                return None

            content_list.clear()

            f = open(os.path.join(folder_path, file_name), "r")
            content_array = f.readlines()

            for content in content_array:
                content = content.strip('\n')
                content_list.append(content)

        except Exception as e:
            ILog.debug(FileUtil.__TAG, str(e))
            return None

        finally:
            return content_list

    @staticmethod
    def storage_file(folder_path, file_name, file):

        try:

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file.save(os.path.join(folder_path, file_name))

            return True
        except Exception as e:
            ILog.debug(FileUtil.__TAG, str(e))
            return False

    @staticmethod
    def delete_file(folder_path, file_name):
        try:
            file_path = os.path.join(
                folder_path,
                file_name
            )

            if os.path.exists(file_path):
                os.remove(file_path)

        except Exception as e:
            print(str(e))
