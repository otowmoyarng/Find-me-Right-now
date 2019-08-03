# -*- coding: utf-8 -*-
import requests
import configparser
from Settings import Settings

# 設定ファイル情報
# line_notify_token = ""
# line_notify_api = ""

# iniファイルを読み込み
# def iniread():
#     global line_notify_token
#     global line_notify_api
#     # config = configparser.ConfigParser()
#     # config.read('setting.ini')
#     # line_notify_token = config['LINENotify']['line_notify_token']
#     # line_notify_api = config['LINENotify']['line_notify_api']
#     config = Settings()
#     line_notify_token = config.getLINENotify_Token()
#     line_notify_api = config.getLINENotify_APIPath()

def main():
    # 設定ファイル読み込み
    # iniread()
    config = Settings()

    print("LINEへ送信するメッセージを入力してください。")
    message = input("送信メッセージ：")
    
    print('送信メッセージ：' + message)
    payload = {'message': message}
    # headers = {'Authorization': 'Bearer ' + line_notify_token}
    # requests.post(line_notify_api, data=payload, headers=headers)
    headers = {'Authorization': 'Bearer ' + config.getLINENotify_Token()}
    requests.post(config.getLINENotify_APIPath(), data=payload, headers=headers)

if __name__== '__main__':
    main()