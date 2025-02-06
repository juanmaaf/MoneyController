import unittest
from config import settings

class TestConfig(unittest.TestCase):

    def test_app_configuration(self):
        self.assertEqual(settings.app.name, "MoneyController")
        self.assertEqual(settings.app.env, "development")

    def test_log_configuration(self):
        self.assertEqual(settings.log.level, "INFO")
        self.assertEqual(settings.log.logfile, "/tmp/money_controller.log")

if __name__ == "__main__":
    unittest.main()