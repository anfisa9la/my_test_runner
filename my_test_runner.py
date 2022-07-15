import command_runner
import configuration
import email_sender
import scheduler
import sys

direction = configuration.direction

txt_file = '{}{}'.format(configuration.txt_path, configuration.txt_name)
result_dir = configuration.allure_result_dir

use_allure = configuration.use_allure
stdout_to_file = configuration.stdout_to_file


def create_test_command(direction, use_allure: bool, stdout_to_file: bool):
    allure = ' --alluredir={}'.format(result_dir) if use_allure else ''
    stdout = ' > {}'.format(txt_file) if stdout_to_file else ''
    return 'pytest {}{}{}'.format(direction, allure, stdout)


def create_report_command(allure_result_dir):
    return 'allure serve {}'.format(allure_result_dir)


def run_tests():
    command_runner.run_command(create_test_command(direction, use_allure, stdout_to_file))


def create_report():
    command_runner.run_command(create_report_command(result_dir))


def run():
    if use_allure:
        run_tests()
        create_report()
    elif stdout_to_file:
        sys.stdout = open(txt_file, "w")
        print(run_tests())
        email_sender.send_mail(
            configuration.sender,
            configuration.password,
            configuration.recipient,
            configuration.msg
        )
    else:
        run_tests()


def schedule_run():
    scheduler.main(run, '21:00')


run()

