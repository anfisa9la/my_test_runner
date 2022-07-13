import command_runner
import scheduler

direction = '/Users/anfisa/PycharmProjects/pythonProject/kata'
allure_result_dir = 'results'
use_allure = True


def create_test_command(direction: str, use_allure: bool):
    allure = ' --alluredir={}'.format(allure_result_dir) if use_allure else ''
    return 'pytest {}{}'.format(direction, allure)


def create_report_command(allure_result_dir):
    return 'allure serve {}'.format(allure_result_dir)


def run_tests():
    command_runner.run_command(create_test_command(direction, use_allure))


def create_report():
    command_runner.run_command(create_report_command(allure_result_dir))


def run():
    if use_allure:
        run_tests()
        create_report()
    else:
        run_tests()


def schedule_run():
    scheduler.main(run, '21:00')

