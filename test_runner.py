import unittest
import my_test_runner as runner

direction = '/Users/anfisa/PycharmProjects/pythonProject/kata'


class TestMyRunner(unittest.TestCase):

    def test_no_allure(self):
        self.assertEqual(runner.create_test_command(direction, False, False),
                         'pytest /Users/anfisa/PycharmProjects/pythonProject/kata'
                         )

    def test_no_allure_stdout_to_file(self):
        self.assertEqual(runner.create_test_command(direction, False, True),
                         'pytest /Users/anfisa/PycharmProjects/pythonProject/kata > {}'.format(runner.txt_file)
                         )

    def test_use_allure(self):
        self.assertEqual(runner.create_test_command(direction, True, False),
                         'pytest /Users/anfisa/PycharmProjects/pythonProject/kata --alluredir={}'.format(
                             runner.allure_result_dir)
                         )

    def test_allure_creation(self):
        self.assertEqual(runner.create_report_command('test_all'),
                         'allure serve test_all'
                         )
