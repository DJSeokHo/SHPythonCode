# _*_ coding: utf-8 _*_
# @Time : 2023/08/03 11:17 AM
# @Author : Coding with cat
# @File : fcm_example
# @Project : SHPythonCode

"""Server Side FCM sample.

Firebase Cloud Messaging (FCM) can be used to send messages to clients on iOS,
Android and Web.

This sample uses FCM to send two types of messages to clients that are subscribed
to the `news` topic. One type of message is a simple notification message (display message).
The other is a notification message (display notification) with platform specific
customizations. For example, a badge is added to messages that are sent to iOS devices.
"""

import argparse
import json
import requests
import google.auth.transport.requests

from google.oauth2 import service_account

from framewrok.utility.log_utility import ILog

PROJECT_ID = 'treasurehunter-93e93'
# PROJECT_ID = 'wheretogo-a5d66'
BASE_URL = 'https://fcm.googleapis.com'
FCM_ENDPOINT = 'v1/projects/' + PROJECT_ID + '/messages:send'
FCM_URL = BASE_URL + '/' + FCM_ENDPOINT
SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


# [START retrieve_access_token]
def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.

    :return: Access token.
    """
    credentials = service_account.Credentials.from_service_account_file(
        # 'wheretogo-a5d66-firebase-adminsdk-aykyj-fe951f53bb.json',
        'treasurehunter-93e93-firebase-adminsdk-xqvel-943e30a213.json',
        scopes=SCOPES
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    token = credentials.token
    ILog.debug(__file__, token)
    return token


# [END retrieve_access_token]

def _send_fcm_message(fcm_message):
    """Send HTTP request to FCM with given message.

    Args:
      fcm_message: JSON object that will make up the body of the request.
    """
    # [START use_access_token]
    headers = {
        'Authorization': 'Bearer ' + _get_access_token(),
        'Content-Type': 'application/json; UTF-8',
    }
    # [END use_access_token]
    resp = requests.post(FCM_URL, data=json.dumps(fcm_message), headers=headers)

    if resp.status_code == 200:
        print('Message sent to Firebase for delivery, response:')
        print(resp.text)
    else:
        print('Unable to send message to Firebase')
        print(resp.text)


def _build_common_message():
    """Construct common notifiation message.

    Construct a JSON object that will be used to define the
    common parts of a notification message that will be sent
    to any app instance subscribed to the news topic.
    """
    return {
        "message":{
            "token":"c31J8jCFDEEgp93O8j0hN0:APA91bHsVIyd-4jdF7PnwW3AufRhL-noJUhxF5ylHFOL2qw7J82MIMB0zstryAsMtWAHvuFEPKRukesKmv9pshXIF66SryAfzOhUZYzsdZoTj-oZZVUlNsCed3XFnbALprLxWLf20Sh1",
            # "token":"dcXC_JW3k0EwtJCe1uMW0S:APA91bGSr9q_HtclOOuxhaGNadbMB1vXDUbXMXOATVrkChCTjcoj24ZRDwSGY0GDd2SRCbImhqVih-rHcnKRy0EUZyGNZFuI5d9pKVFw8ZtRdsQ5T8Y8-dzaBcsSIAGny5vQQBVzx1L8",
            "notification":{
                "body":"This is message!",
                "title":"This is title"
            },
            "data": {
                "id": "12345",
                "result": "0",
                "type": "report"
            },
            "android": {
                "notification": {
                    "click_action": ""
                }
            },
            "apns": {
                "payload": {
                    "aps": {
                        "sound": "pager.wav",
                        "badge": 0,
                        "category" : ""
                    }
                }
            }
        }
    }


def _build_override_message():
    """Construct common notification message with overrides.

    Constructs a JSON object that will be used to customize
    the messages that are sent to iOS and Android devices.
    """
    fcm_message = _build_common_message()

    apns_override = {
        'payload': {
            'aps': {
                'badge': 1
            }
        },
        'headers': {
            'apns-priority': '10'
        }
    }

    android_override = {
        'notification': {
            'click_action': 'android.intent.action.MAIN'
        }
    }

    fcm_message['message']['android'] = android_override
    fcm_message['message']['apns'] = apns_override

    return fcm_message


def main():
    common_message = _build_common_message()
    print('FCM request body for message using common notification object:')
    print(json.dumps(common_message, indent=2))
    _send_fcm_message(common_message)

#     parser = argparse.ArgumentParser()
#     parser.add_argument('--message')
#     args = parser.parse_args()
#     if args.message and args.message == 'common-message':
#         common_message = _build_common_message()
#         print('FCM request body for message using common notification object:')
#         print(json.dumps(common_message, indent=2))
#         _send_fcm_message(common_message)
#     elif args.message and args.message == 'override-message':
#         override_message = _build_override_message()
#         print('FCM request body for override message:')
#         print(json.dumps(override_message, indent=2))
#         _send_fcm_message(override_message)
#     else:
#         print('''Invalid command. Please use one of the following commands:
# python messaging.py --message=common-message
# python messaging.py --message=override-message''')


if __name__ == '__main__':
    main()
