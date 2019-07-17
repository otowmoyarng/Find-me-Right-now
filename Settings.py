import configparser

# Settting.iniを管理するクラス
class Settings:
    
    setting = None

    # コンストラクタ
    # iniファイルを読み込み
    def __init__(self):
        setting = configparser.ConfigParser()
        setting.read('setting.ini')

    # setting.iniよりアクセストークンを取得する
    def getToken():
        return setting['LINENotify']['line_notify_token']

    # setting.iniよりアクセスURLを取得する
    def getAPIPath():
        return setting['LINENotify']['line_notify_api']
