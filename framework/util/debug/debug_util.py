# coding: utf-8

class ILog:

    __header = "ILog ======> "

    @staticmethod
    def debug(tag, content):
        print(f'{ILog.__header} {tag} {content}')
