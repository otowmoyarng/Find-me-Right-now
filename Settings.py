from configparser import ConfigParser
from pconst import const

# Settting.iniを管理するクラス
class Settings:
    
    # setting.ini セクション名
    const.NOTIFY = 'LINENotify'
    # LINENotifyセクション　トークン名
    const.NOTIFY_TOKEN = 'line_notify_token'
    # LINENotifyセクション　URL
    const.NOTIFY_APIURL = 'line_notify_api'

    # コンストラクタ
    # iniファイルを読み込み
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('setting.ini', encoding="utf-8")

    # setting.iniよりアクセストークンを取得する
    def getLINENotify_Token(self):
        return self.config[const.NOTIFY][const.NOTIFY_TOKEN]

    # setting.iniよりアクセスURLを取得する
    def getLINENotify_APIPath(self):
        return self.config[const.NOTIFY][const.NOTIFY_APIURL]

    # アクセストークン書き込み用
    def writeLINENotify_Token(self, token):
        self.config.set(const.NOTIFY, const.NOTIFY_TOKEN, token)