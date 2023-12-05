import unittest
from unittest.mock import patch
from bird import Bird  # Замените "your_module" на имя вашего файла с классом Bird

class TestBirdClass(unittest.TestCase):
    def test_valid_speed(self):
        bird = Bird("TestBird", "10.5", 1)
        self.assertEqual(bird.speed, 10.5)

    def test_negative_speed(self):
        with patch('builtins.print') as mock_print:
            bird = Bird("TestBird", "-5.0", 2)
            self.assertEqual(bird.speed, 0.0)
            mock_print.assert_called_with("Error in line 2: Недопустимое значение скорости для птицы (TestBird). Используйте дробное число.")

    def test_invalid_speed(self):
        with patch('builtins.print') as mock_print:
            bird = Bird("TestBird", "invalid_speed", 3)
            self.assertEqual(bird.speed, 0.0)
            mock_print.assert_called_with("Error in line 3: Недопустимое значение скорости для птицы (TestBird). Используйте дробное число.")

if __name__ == '__main__':
    unittest.main()
