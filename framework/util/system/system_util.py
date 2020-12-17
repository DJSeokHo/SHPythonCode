# -*- coding: utf-8 -*-
import sys


class SystemUtil:

    @staticmethod
    def get_current_project_root_path():

        project_dir = sys.path[0]
        return project_dir
