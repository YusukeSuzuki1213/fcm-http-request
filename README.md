![](https://github.com/YusukeSuzuki1213/fcm-http-request/workflows/Lint/badge.svg)
# fcm-http-request
FCMを送信するクライアント
## Usage
1. `$ git clone git@github.com:YusukeSuzuki1213/fcm-http-request.git`
1. `$ pipenv install`
1. `$ pipenv run pre-commit install`
1. Firebase Consoleからサービスアカウントキーを取得し、`service-account.json`として保存
1. `.env.sample`を参考に`.env`を作成
    - `PROJECT_ID`を設定: FirebaseConsoleにて確認できる
    - `FIREBASE_DEVICE_TOKEN`を設定: デバイスを一意に特定できるFirebase Device Tokenを指定する。
