import logging
import datetime
class Insects:
    def __init__(self, name, size, date, line_number):
        self.name = name
        self.line_number = line_number

        if self.is_valid_size(size):
            self.size = float(size)
        else:
            error_message = f"Error in line {self.line_number}: Недопустимый формат размера для насекомого ({name})"
            print(error_message)
            logging.error(error_message)
            self.size = None

        if self.is_valid_date(date):
            self.date = date
        else:
            error_message = f"Error in line {self.line_number}: Недопустимый формат даты для насекомого ({name})"
            print(error_message)
            logging.error(error_message)
            self.date = None

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

    def __str__(self):
        if self.size is not None and self.date is not None:
            return f"INSECTS, {self.name}, {self.size}, {self.date}"
        else:
            return f"Error in line {self.line_number}. Неправильная дата или размер"
