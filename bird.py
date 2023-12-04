import logging

class Bird:
    invalid_speed_values = set()

    def __init__(self, name, speed, line_number):
        self.name = name
        try:
            parsed_speed = float(speed)
            if parsed_speed < 0.0:
                raise ValueError("Скорость птицы не может быть отрицательной")
            self.speed = parsed_speed
        except ValueError:
            self.speed = 0.0
            if speed not in Bird.invalid_speed_values:
                Bird.invalid_speed_values.add(speed)
                logging.error(f"Error in line {line_number}: Недопустимое значение скорости для птицы ({name}). Используйте дробное число.")
                print(f"Error in line {line_number}: Недопустимое значение скорости для птицы ({name}). Используйте дробное число.")

    def __str__(self):
        if self.speed != 0.0:
            return f"BIRD, {self.name}, {self.speed}"
        else:
            return f"Error in line: {self.name}"