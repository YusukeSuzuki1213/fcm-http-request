import json
import requests
from oauth2client.service_account import ServiceAccountCredentials
import settings

SERVICE_ACCOUNT_PATH = "./service-account.json"
SCOPES = "https://www.googleapis.com/auth/firebase.messaging"
URL = "https://fcm.googleapis.com/v1/projects/{}/messages:send".format(
    settings.PROJECT_ID
)


def get_access_token():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_PATH, SCOPES
    )
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token


def request_fcm(access_token):

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
    }
    payload = {
        "message": {
            "token": settings.FIREBASE_DEVICE_TOKEN,
            "android": {
                "data": {
                    "title": "タイトル",
                    "body": "ボディ",
                    "uri": "sosotown://index/search?hoge",
                }
            },
        }
    }

    r = requests.post(URL, data=json.dumps(payload), headers=headers)
    print(r.text)


if __name__ == "__main__":
    access_token = get_access_token()
    request_fcm(access_token)
