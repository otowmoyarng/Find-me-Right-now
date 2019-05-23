# -*- coding: utf-8 -*-
import requests
import configparser

# 設定ファイル情報
config = ""
line_notify_token = ""
line_notify_api = ""

# iniファイルを読み込み
def iniread():
    global config
    global line_notify_token
    global line_notify_api
    config = configparser.ConfigParser()
    config.read('setting.ini')
    line_notify_token = config['LINENotify']['line_notify_token']
    line_notify_api = config['LINENotify']['line_notify_api']

def main():
    # 設定ファイル読み込み
    iniread()

    print("LINEへ送信するメッセージを入力してください。")
    message = input("送信メッセージ：")
    
    print('送信メッセージ：' + message)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

if __name__== '__main__':
    main()