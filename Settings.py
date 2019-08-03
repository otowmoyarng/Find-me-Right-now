from configparser import ConfigParser
from pconst import const

# Settting.iniを管理するクラス
class Settings:
    
    # setting.ini セクション名
    NOTIFY = 'LINENotify'
    const.SECTION_LINENotify = NOTIFY
    # LINENotifyセクション　トークン名
    NOTIFY_TOKEN = 'line_notify_token'
    const.LINENotify_TOKEN = NOTIFY_TOKEN
    # LINENotifyセクション　URL
    NOTIFY_APIURL = 'line_notify_api'
    const.LINENotify_APIURL = NOTIFY_APIURL

    # コンストラクタ
    # iniファイルを読み込み
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('setting.ini', encoding="utf-8")

    # ConfigParserインスタンスを生成する
    def getConfigParserInstance(self):
        return self.config

    # setting.iniよりアクセストークンを取得する
    def getLINENotify_Token(self):
        # return self.config[NOTIFY][NOTIFY_TOKEN]
        return self.config[const.SECTION_LINENotify][const.LINENotify_TOKEN]

    # setting.iniよりアクセスURLを取得する
    def getLINENotify_APIPath(self):
        # return self.config[NOTIFY][NOTIFY_APIURL]
        return self.config[const.SECTION_LINENotify][const.LINENotify_APIURL]