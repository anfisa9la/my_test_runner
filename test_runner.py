import unittest
import my_test_runner

direction = '/Users/anfisa/PycharmProjects/pythonProject/kata'


class TestMyRunner(unittest.TestCase):

    def test_no_allure(self):
        self.assertEqual(my_test_runner.create_test_command(direction, False),
                         'pytest /Users/anfisa/PycharmProjects/pythonProject/kata'
                         )

    def test_use_allure(self):
        self.assertEqual(my_test_runner.create_test_command(direction, True),
                         'pytest /Users/anfisa/PycharmProjects/pythonProject/kata --alluredir=results'
                         )

    def test_allure_creation(self):
        self.assertEqual(my_test_runner.create_report_command('test_all'),
                         'allure serve test_all'
                         )
