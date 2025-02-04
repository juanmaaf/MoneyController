import unittest
from unittest.mock import patch, MagicMock
from loguru import logger
from logger import init_logger
import sys

class TestLogger(unittest.TestCase):
    @patch("logger.settings")
    def test_init_logger(self, mock_settings):
        mock_settings.get.side_effect = lambda key, default: {
            "log.level": "INFO",
            "log.logfile": "/tmp/test_log.log",
        }.get(key, default)

        with patch.object(logger, "remove") as mock_remove, \
             patch.object(logger, "add") as mock_add:
            
            returned_logger = init_logger()

            mock_remove.assert_called_once()

            self.assertEqual(mock_add.call_count, 2)

            mock_add.assert_any_call(
                sys.stdout,
                level="INFO",
                format="{time} | {level} | {message}",
            )
            mock_add.assert_any_call(
                "/tmp/test_log.log",
                level="INFO",
                format="{time} | {level} | {message}",
                rotation="1 week",
            )
            self.assertEqual(returned_logger, logger)

if __name__ == "__main__":
    unittest.main()