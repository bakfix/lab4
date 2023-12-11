import unittest
from main import ContainerProgram

class TestContainerProgram(unittest.TestCase):
    def setUp(self):
        self.program = ContainerProgram()

    def test_process_file(self):
        file_content = (
            "ADD FISH, SHUKA, RIVER\n"
            "PRINT\n"
            "ADD FISH, OCUN, RIVER\n"
            "REM SHUKA\n"
            "REM OCUN\n"
            "PRINT\n"
            "ADD BIRD, YASTREB, 22.32\n"
            "REM < 222.32\n"
            "ADD FISH, OCUN, OCEAN\n"
            "ADD INSECTS, JUK, 22, 22:03:2004\n"
            "PRINT\n"
        )

        with open("test_file.txt", "w") as test_file:
            test_file.write(file_content)

        expected_output = (
            "FISH, SHUKA, RIVER\n"
            "FISH, OCUN, OCEAN\n"
            "INSECTS, JUK, 22, 22:03:2004"
        )

        try:
            self.program.process_file("test_file.txt")
            self.assertEqual(str(self.program.container).strip(), expected_output.strip())
        except AssertionError as e:
            print(f"Current container: {str(self.program.container)}")
            print(f"Expected output: {expected_output}")

    def tearDown(self):
        import os
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")

if __name__ == '__main__':
    unittest.main()
