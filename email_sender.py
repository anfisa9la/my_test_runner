import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import configuration

sender = configuration.sender
password = configuration.password
recipient = configuration.recipient
file = configuration.txt_name


def send_mail(sender, password, recipient, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = 'test run results'
    html = open("mail.html").read()
    html_part = MIMEText(html, "html")
    msg.attach(html_part)

    with open(file, "rb") as f:
        data = f.read()
        attach_part = MIMEBase("application", "octet-stream")
        attach_part.set_payload(data)
        encoders.encode_base64(attach_part)
        attach_part.add_header("Content-Disposition", f"attachment; filename= {file}")
        msg.attach(attach_part)
