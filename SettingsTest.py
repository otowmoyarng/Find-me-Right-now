import unittest
from Settings import Settings

# Setttingsユニットテストクラス
class SettingsTest(unittest.TestCase):

    # # テスト準備
    def setUp(self):
        self.config = Settings()

    # テストケース：コンストラクタ
    def test_constructor(self):
        self.assertIsNotNone(self.config)
        
    # テストケース：iniファイル設定値取得メソッド
    def test_getSettings(self):
        self.assertIsNotNone(self.config.getLINENotify_Token())
        self.assertIsNotNone(self.config.getLINENotify_APIPath())

    # テストケース：iniファイル設定値書き込みメソッド
    def test_writeSettings(self):
        token = input('テスト実行するtokenを入力してください。')
        self.config.writeLINENotify_Token(token)
        self.assertEqual(token, self.config.getLINENotify_Token())

if __name__ == '__name__':
    unittest.main()