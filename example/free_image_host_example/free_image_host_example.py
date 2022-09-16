# _*_ coding: utf-8 _*_
# @Time : 2022/09/15 11:13 PM
# @Author : Coding with cat
# @File : free_image_host_example
# @Project : SHPythonCode
from framewrok.module.http.requests_wrapper.requests_wrapper import RequestsWrapper
from framewrok.module.http.response_object.response_object import ResponseObject
from framewrok.utility.json_utility import JSONUtility
from framewrok.utility.log_utility import ILog


def upload_image() -> ResponseObject:

    response: ResponseObject = RequestsWrapper().url(
        url='https://freeimage.host/api/1/upload'
    ).form_datas(
        form_datas={
            'key': '6d207e02198a847aa98d0a2a901485a5',
            'action': 'upload',
            'format': 'json'
        }
    ).post(file_key='source', file=open('Untitled.jpg', 'rb'))

    ILog.debug(__file__, response.get_dictionary())
    ILog.debug(__file__, response.get_data())
    return response


if __name__ == '__main__':

    response_object = upload_image()
    data = response_object.get_data()
    # ILog.debug(__file__, type(data))
    # ILog.debug(__file__, data)
    data_object = JSONUtility.to_json_object(data)

    image = data_object['image']
    # ILog.debug(__file__, type(image))
    # ILog.debug(__file__, image)

    original_image = image['image']
    thumb_image = image['thumb']
    medium_image = image['medium']

    ILog.debug(__file__, JSONUtility.parsing_str(original_image, 'url'))
    ILog.debug(__file__, JSONUtility.parsing_str(thumb_image, 'url'))
    ILog.debug(__file__, JSONUtility.parsing_str(medium_image, 'url'))
