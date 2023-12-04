from enum import Enum
import datetime
import logging
import math
from fish import Fish

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
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next and current.next != self.head:
                # Изменение здесь: добавим объект, даже если его имя уже существует
                if current.data.name == data.name:
                    break
                current = current.next
            else:
                current.next = new_node
                new_node.next = self.head

    def remove(self, condition_func):
        if not self.head or self.head.next == self.head:
            self.head = None
            return

        current = self.head
        prev = None

        while True:
            if condition_func(current.data):
                if prev:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next if current.next != self.head else None
                else:
                    if current.next == self.head:
                        self.head = current.next.next if current.next.next != self.head else None
                    else:
                        self.head = current.next

            if current.next == self.head:
                break

            prev = current
            current = current.next

    def __str__(self):
        result = []
        current = self.head

        while current is not None:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        return '\n'.join(result)


class ContainerProgram:
    def __init__(self):
        self.container = CircularLinkedList()
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("container_program")
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        return logger

    def add_object(self, data):
        try:
            self.container.append(data)
        except ValueError as e:
            error_message = f"Недопустимая команда: {str(data)} - {str(e)}"
            self.logger.error(error_message)
            print(error_message)

    def remove_objects_permanently(self, condition_func, condition_value=None, name_condition=None):
        current = self.container.head
        prev = None

        while True:
            should_remove = False

            if (condition_value is not None and condition_func(current.data, condition_value)) or \
                    (condition_value is None and name_condition is not None and condition_func(current.data,
                                                                                               name_condition)):
                should_remove = True

            if should_remove:
                if prev:
                    prev.next = current.next
                    if current == self.container.head:
                        self.container.head = current.next if current.next != self.container.head else None
                else:
                    if current.next == self.container.head:
                        self.container.head = current.next.next if current.next.next != self.container.head else None
                    else:
                        self.container.head = current.next
            else:
                prev = current

            if current.next == self.container.head:
                break

            current = current.next
    def remove_objects(self, condition_func):
        if not self.container.head or self.container.head.next == self.container.head:
            self.container.head = None
            return

        current = self.container.head
        prev = None

        while True:
            if condition_func(current.data):
                if prev:
                    prev.next = current.next
                    if current == self.container.head:
                        self.container.head = current.next if current.next != self.container.head else None
                else:
                    if current.next == self.container.head:
                        self.container.head = current.next.next if current.next.next != self.container.head else None
                    else:
                        self.container.head = current.next

            if current.next == self.container.head:
                break

            prev = current
            current = current.next

    def __str__(self):
        result = []
        current = self.container.head

        while current is not None:
            result.append(str(current.data))
            current = current.next
            if current == self.container.head:
                break

        return '\n'.join(result)

    def remove_objects_by_name(self, name):
        def condition_func(obj, name=name):
            return obj.name == name

        self.container.remove(condition_func)
    def print_container(self):
        print(self.container)
        self.logger.info("Выведено содержимое контейнера")

    def process_file(self, file_name):
        with open(file_name, "r") as file:
            for line_number, line in enumerate(file, start=1):
                parts = line.strip().split(' ', 1)
                command = parts[0]
                try:
                    if command == "ADD":
                        if len(parts) < 2:
                            raise ValueError(f"Ошибка в строке {line_number}: Недостаточно параметров для команды ADD")

                        data = parts[1].split(', ')
                        if len(data) < 3:
                            raise ValueError(
                                f"Ошибка в строке {line_number}: Неверное количество параметров для команды ADD")

                        if data[0] == "FISH":
                            obj = Fish(data[1], data[2])
                        elif data[0] == "BIRD":
                            if len(data) != 3:
                                raise ValueError(
                                    f"Ошибка в строке {line_number}: Неверное количество параметров для команды ADD")
                            speed = data[2].replace(',', '.')
                            obj = Bird(data[1], speed, line_number)
                        elif data[0] == "INSECTS":
                            if len(data) != 4:
                                raise ValueError(
                                    f"Ошибка в строке {line_number}: Неверное количество параметров для команды ADD")
                            insects_obj = Insects(data[1], data[2], data[3], line_number)
                            if insects_obj.size is not None and insects_obj.date is not None:
                                self.add_object(insects_obj)
                            else:
                                print(f"Error in line {line_number}: Недопустимые данные для насекомого ({data[1]})")
                        else:
                            raise ValueError(f"Ошибка в строке {line_number}: Недопустимая команда ADD")

                        self.add_object(obj)
                    elif command == "REM":
                        condition = parts[1].strip()
                        condition_value = None

                        if ">" in condition or "<" in condition or "=" in condition:
                            condition_parts = condition.split()
                            condition = condition_parts[0]
                            condition_value = float(condition_parts[1].replace(',', '.'))

                        self.remove_objects_by_name(condition)

                        def remove_condition(obj, condition=condition, condition_value=condition_value):
                            if condition_value is not None:
                                if ">" in condition:
                                    return hasattr(obj, 'speed') and obj.speed > condition_value
                                elif "<" in condition:
                                    return hasattr(obj, 'speed') and obj.speed < condition_value
                                elif "=" in condition:
                                    return hasattr(obj, 'speed') and math.isclose(obj.speed, condition_value)
                                else:
                                    return obj.name == condition
                            elif condition_value is None:
                                return obj.name == condition
                            else:
                                return False

                        self.remove_objects(remove_condition)



                    elif command == "PRINT":
                        self.print_container()
                    else:
                        name_to_remove = condition
                        self.remove_objects_by_name(name_to_remove)
                        self.remove_objects(remove_condition)
                except ValueError as e:
                    error_message = f"Ошибка в строке {line_number}: {str(e)}"
                    self.logger.error(error_message)
                    print(error_message)

if __name__ == "__main__":
    program = ContainerProgram()

    while True:
        command = input("Введите команду (FILE для обработки файла, или EXIT для выхода): ").strip()

        if command == "FILE":
            file_name = input("Введите имя файла: ")
            program.process_file(file_name)
        elif command == "EXIT":
            break
        else:
            print("Неверная команда. Попробуйте снова.")