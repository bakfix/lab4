import datetime
import logging

class Insects:
    def __init__(self, name, size, date, line_number):
        self.name = name
        self.line_number = line_number

        if not self.is_valid_size(size):
            self.handle_invalid_data(f"Недопустимый формат размера для насекомого ({name})")

        if not self.is_valid_date(date):
            self.handle_invalid_data(f"Недопустимый формат даты для насекомого ({name})")

        self.size = float(size)
        self.date = datetime.datetime.strptime(date, "%d:%m:%Y")

    def is_valid_size(self, size):
        try:
            float(size)
            return True
        except ValueError:
            return False

    def is_valid_date(self, date):
        try:
            datetime.datetime.strptime(date, "%d:%m:%Y")
            return True
        except ValueError:
            return False

    def handle_invalid_data(self, error_message):
        logging.error(f"Error in line {self.line_number}: {error_message}")
        print(f"Error in line {self.line_number}: {error_message}")
        self.size = None
        self.date = None

    def __str__(self):
        if self.size is not None and self.date is not None:
            return f"INSECTS, {self.name}, {self.size}, {self.date.strftime('%d:%m:%Y')}"
        else:
            return f"Error in line {self.line_number}. Неправильная дата или размер"
