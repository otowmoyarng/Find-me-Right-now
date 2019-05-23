import configparser

config = ""

# iniファイルを読み込み
def iniread():
    global config
    config = configparser.ConfigParser()
    config.read('setting.ini')

# テスト実行メソッド
def main():
    iniread()
    
    # セクション名
    print(config.sections())

    # 定義項目名
    print([key for key in config['LINENotify']])
    
    # 定義値
    print(config['LINENotify']['line_notify_token'])

if __name__== '__main__':
    main()