import unittest

import configuration
import my_test_runner as runner

direction = '/Users/anfisa/test'


class TestMyRunner(unittest.TestCase):

    def test_no_allure(self):
        self.assertEqual(runner.create_test_command(direction, False, False),
                         'pytest /Users/anfisa/test'
                         )

    def test_no_allure_stdout_to_file(self):
        self.assertEqual(runner.create_test_command(direction, False, True),
                         'pytest /Users/anfisa/test > {}'.format(runner.txt_file)
                         )

    def test_use_allure(self):
        self.assertEqual(runner.create_test_command(direction, True, False),
                         'pytest /Users/anfisa/test --alluredir={}'.format(
                             configuration.allure_result_dir)
                         )

    def test_allure_creation(self):
        self.assertEqual(runner.create_report_command('test_all'),
                         'allure serve test_all'
                         )
