# _*_ coding: utf-8 _*_
# @Time : 2022/09/15 1:40 PM
# @Author : Coding with cat
# @File : imgur_example
# @Project : SHPythonCode
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

from framewrok.utility.log_utility import ILog

client_id = '425e328c69d4219'
client_secret = '34f546124904ee0326756df4315f19ffb1f17a99'
access_token = '0c42ecff66f6496ccd2b723c6fd0237d28b9bfa1'
refresh_token = '304ae6370cf18e28870b8ee70cc836e4c0c136cc'


def create_album(client: ImgurClient, title: str, description: str) -> dict:

    try:

        album = client.create_album(fields={
            'title': title,
            'description': description
        })

        return album

    except ImgurClientError as e:
        ILog.debug(__file__, e.error_message)
        return dict()


def upload_image(client: ImgurClient, album_hash: str, path: str, name: str, title: str, description: str) -> dict:

    try:

        config = {'album': album_hash, 'name': name, 'title': title, 'description': description}

        image = client.upload_from_path(path=path, config=config, anon=False)

        return image

    except ImgurClientError as e:
        ILog.debug(__file__, e.error_message)
        return dict()


if __name__ == '__main__':

    imgur_client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    # album = create_album(client=imgur_client, title='test', description='description album')
    # ILog.debug(__file__, type(album))
    # ILog.debug(__file__, album)

    image = upload_image(client=imgur_client, album_hash='6DjSWVu', path='WechatIMG1.jpeg',
                         name='test1.jpg', title='test1 title', description='test1 description')
    ILog.debug(__file__, type(image))
    ILog.debug(__file__, image)
    ILog.debug(__file__, image['id'])
    ILog.debug(__file__, image['link'])
