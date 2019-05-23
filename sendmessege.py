import requests

line_notify_token = "<ここにアクセストークンを定義する>"
line_notify_api = 'https://notify-api.line.me/api/notify'

def main():
    print("LINEへ送信するメッセージを入力してください。")
    message = input("送信メッセージ：")
    
    print('送信メッセージ：' + message)
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

if __name__== '__main__':
    main()