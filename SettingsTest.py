import unittest
import Settings

# Setttingsユニットテストクラス
class SettingsTest(unittest.TestCase):

    setting = None

    # # テスト準備
    def setUp(self):
        setting = Settings()
        print(setting)

    # テストケース：コンストラクタ
    def test_constructor(self):
        self.assertIsNotNone(setting)
        
    # テストケース：設定値取得メソッド
    # def test_settings(self):
    #     self.assertIsNotNone(setting.getToken())
    #     self.assertIsNotNone(setting.getAPIPath())

if __name__ == '__name__':
    unittest.main()