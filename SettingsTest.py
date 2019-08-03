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
        self.assertIsNotNone(self.config.getConfigParserInstance())
        self.assertIsNotNone(self.config.getLINENotify_Token())
        self.assertIsNotNone(self.config.getLINENotify_APIPath())

if __name__ == '__name__':
    unittest.main()