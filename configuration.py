from email.mime.multipart import MIMEMultipart

# use allure or save test results to txt file
use_allure = False
stdout_to_file = True

# tests path
direction = '/Users/anfisa/PycharmProjects/pythonProject/kata'

# txt file path
txt_path = '/Users/anfisa/Desktop/'
txt_name = 'test_log.txt'

# path to save allure reports
allure_result_dir = 'results'

# email service
sender = "from_address@mail.com"
password = "pass"
recipient = "to_address@mail.com"
msg = MIMEMultipart("alternative")

