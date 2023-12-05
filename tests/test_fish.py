import unittest
from fish import Fish, Habitat

class TestFish(unittest.TestCase):
    def test_valid_habitat(self):
        # Проверяем, что рыба создается с допустимым ареалом
        fish = Fish("Какая-то рыба", "OCEAN")
        self.assertEqual(fish.name, "Какая-то рыба")
        self.assertEqual(fish.habitat, "OCEAN")

    def test_invalid_habitat(self):
        with self.assertRaises(ValueError):
            Fish("InvalidFish", "INVALID_HABITAT")

    def test_str_representation(self):
        fish = Fish("Какая-то рыба", "SEA")  # Используем "SEA" вместо Habitat.SEA
        self.assertEqual(str(fish), "FISH, Какая-то рыба, SEA")


if __name__ == "__main__":
    unittest.main()
