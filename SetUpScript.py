"""
セットアップ用スクリプト
Setting.iniファイルの初期設定を行う。
"""
from Settings import Settings

config = Settings()
cpins = config.getConfigParserInstance()

print("Setting.iniの初期設定を開始します。")
print()
print("LINE Notify登録時のアクセストークンを入力してください。")

token = input('アクセストークン：')
cpins.set(config.NOTIFY, config.NOTIFY_TOKEN, token)
print("アクセストークンを登録しました。")

cpins.set(config.NOTIFY, config.NOTIFY_APIURL, 'https://notify-api.line.me/api/notify')
print("API用URLを登録しました。")

with open('setting.ini', 'w') as contextfile:
    cpins.write(contextfile)

print()
print("Setting.iniの初期設定が完了しました。")
