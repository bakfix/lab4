import logging

class Bird:
    def __init__(self, name, speed, line_number):
        self.name = name
        self.speed = self.parse_speed(speed, line_number)

    def parse_speed(self, speed, line_number):
        try:
            parsed_speed = float(speed)
            if parsed_speed < 0.0:
                raise ValueError("Скорость птицы не может быть отрицательной")
            return parsed_speed
        except ValueError:
            logging.error(f"Error in line {line_number}: Недопустимое значение скорости для птицы ({self.name}). Используйте дробное число.")
            print(f"Error in line {line_number}: Недопустимое значение скорости для птицы ({self.name}). Используйте дробное число.")
            return 0.0

    def __str__(self):
        return f"BIRD, {self.name}, {self.speed}"
