import smtplib
from pathlib2 import Path
import re
from email.mime.text import MIMEText


class EmailClient:
    host = ''
    login_user = ''
    login_password = ''

    def __init__(self, host='', login_user='', login_password=''):
        self.host = host
        self.login_user = login_user
        self.login_password = login_password

    def load_config_file(self, config_path):
        try:
            content = Path(config_path).read_text()
            pattern_host = re.compile(r'(?<!#)(?<=email_host=).+')
            pattern_user = re.compile(r'(?!#)(?<=email_login_user=).+')
            pattern_password = re.compile(r'(?!#)(?<=email_login_password=).+')
            self.host = pattern_host.search(content)[0]
            self.login_user = pattern_user.search(content)[0]
            self.login_password = pattern_password.search(content)[0]
        except Exception as e:
            raise AttributeError("loading config file failed.", e)

    def send_text_email(self, sender_address, tos, subject, body):
        msg = MIMEText(body, _subtype='plain', _charset='gb2312')
        msg['Subject'] = subject
        msg['From'] = sender_address
        msg['To'] = tos
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.login(self.login_user, self.login_password)
            server.sendmail(sender_address, tos, msg.as_string())
            server.close()
        except Exception as e:
            print(str(e))
            raise


if __name__ == '__main__':
    client = EmailClient()
    client.load_config_file(r'd:\email.cfg')
    client.send_text_email('narcissusdubot@sina.com',
                           'duxiaobo@sina.com;william.du@activenetwork.com',
                           'Email Client Test Subject',
                           'Email Client Test Body')
