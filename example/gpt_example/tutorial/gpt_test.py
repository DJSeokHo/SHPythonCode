# _*_ coding: utf-8 _*_
# @Time : 2023/03/23 5:59 PM
# @Author : Coding with cat
# @File : gpt_test
# @Project : SHPythonCode
from requests import Response

from framewrok.module.http.http_wrapper import HTTPWrapper
from framewrok.utility.log_utility import ILog

# TestKey: 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
if __name__ == '__main__':
    response = HTTPWrapper() \
        .url("https://api.openai.com/v1/chat/completions") \
        .header({
            "Content-Type": "application/json",
            "Authorization": "Bearer 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"
        }) \
        .body({
            "model": "gpt-3.5-turbo-1106",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Hello!"
                }
            ]
        }) \
        .post()

    ILog.debug(__file__, response)
