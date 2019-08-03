# -*- coding: utf-8 -*-
import requests
import configparser
from Settings import Settings

def main():
    # 設定ファイル読み込み
    config = Settings()

    print("LINEへ送信するメッセージを入力してください。")
    message = input("送信メッセージ：")
    
    print('送信メッセージ：' + message)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + config.getLINENotify_Token()}
    requests.post(config.getLINENotify_APIPath(), data=payload, headers=headers)

if __name__== '__main__':
    main()