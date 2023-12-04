from enum import Enum


class Habitat(Enum):
    OCEAN = "OCEAN"
    RIVER = "RIVER"
    SEA = "SEA"


class Fish:
    def __init__(self, name, habitat):
        self.name = name
        if habitat in [item.value for item in Habitat]:
            self.habitat = habitat
        else:
            raise ValueError(f"Невозможный ареал обитания для рыбы ({name})")

    def __str__(self):
        return f"FISH, {self.name}, {self.habitat}"
