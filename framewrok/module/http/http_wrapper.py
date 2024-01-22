import requests
from requests import Response

from framewrok.utility.log_utility import ILog


class HTTPWrapper:

    __headers: dict = {}
    __body: dict = {}
    __url: str = ""

    def url(self, url: str):
        self.__url = url
        return self

    def header(self, headers: dict):
        self.__headers = headers
        return self

    def body(self, body: dict):
        self.__body = body
        return self

    def post(self) -> str:
        response: Response = requests.post(
            url=self.__url,
            headers=self.__headers,
            json=self.__body
        )

        ILog.debug(__file__, self.__url)
        ILog.debug(__file__, response.status_code)

        return str(response.content, encoding="utf-8")
