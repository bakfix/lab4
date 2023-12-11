import unittest
from unittest.mock import patch

from insects import Insects
import datetime

class TestInsectsClass(unittest.TestCase):
    def test_valid_data(self):
        insect = Insects("TestInsect", "5.2", "01:01:2022", 1)
        self.assertEqual(insect.size, 5.2)
        self.assertEqual(insect.date, datetime.datetime(2022, 1, 1))

    def test_invalid_size(self):
        with patch('builtins.print') as mock_print:
            with self.assertRaises(ValueError):
                insect = Insects("TestInsect", "invalid_size", "01:01:2022", 2)
                mock_print.assert_called_with("Error in line 2: Недопустимый формат размера для насекомого (TestInsect)")

    def test_invalid_date(self):
        with patch('builtins.print') as mock_print:
            with self.assertRaises(ValueError):
                insect = Insects("TestInsect", "3.0", "invalid_date", 3)
                mock_print.assert_called_with("Error in line 3: Недопустимый формат даты для насекомого (TestInsect)")

if __name__ == '__main__':
    unittest.main()
