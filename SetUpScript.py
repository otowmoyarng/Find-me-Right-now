"""
セットアップ用スクリプト
設定ファイルの初期設定を行う。
"""
from Settings import Settings

print("設定ファイルの初期設定を開始します。")
print()

print("設定ファイル名を入力してください。省略するとsetting.iniとなります。")
filename = input("設定ファイル名：")
if filename is None or filename == '':
    filename = 'setting.ini'
    config = Settings()
else:
    config = Settings(filename)
cpins = config.getConfigParserInstance()

print("LINE Notify登録時のアクセストークンを入力してください。")
token = input('アクセストークン：')
cpins.set(config.NOTIFY, config.NOTIFY_TOKEN, token)
print("アクセストークンを登録しました。")

cpins.set(config.NOTIFY, config.NOTIFY_APIURL, 'https://notify-api.line.me/api/notify')
print("API用URLを登録しました。")

with open(filename, 'w') as contextfile:
    cpins.write(contextfile)

print()
print("設定ファイルの初期設定が完了しました。")
