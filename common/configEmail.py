# coding:utf-8

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import threading
import read_config as readConfig
from common.Log import MyLog

localReadConfig = readConfig.ReadConfig()
locallog = MyLog.get_log()


class Email:
    def __init__(self):
        global host, user, password, port, sender, title
        host = localReadConfig.get_email("mail_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_email("subject")
        content = localReadConfig.get_email("content")

        # get receiver list
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        for n in self.value.split("|"):
            self.receiver.append(n)

        # defined email subject
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "UI测试报告" + " " + date

        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('related')

    def config_header(self):
        """
        defined email header include subject, sender and receiver
        :return:
        """
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_content(self):
        """
        write the content of email
        :return:
        """
        f = open(os.path.join(readConfig.proDir, 'testfile', 'emailStyle.txt'))
        content = f.read()
        f.close()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)
        self.config_image()

    def config_image(self):
        """
        config image that be used by content
        :return:
        """
        # defined image path
        image1_path = os.path.join(readConfig.proDir, 'testfile', 'img', '1.jpg')
        fp1 = open(image1_path, 'rb')
        msgImage1 = MIMEImage(fp1.read())
        # self.msg.attach(msgImage1)
        fp1.close()

        # defined image id
        msgImage1.add_header('Content-ID', '<image1>')
        self.msg.attach(msgImage1)

        image2_path = os.path.join(readConfig.proDir, 'testfile', 'img', 'logo.jpeg')
        fp2 = open(image2_path, 'rb')
        msgImage2 = MIMEImage(fp2.read())
        # self.msg.attach(msgImage2)
        fp2.close()

        # defined image id
        msgImage2.add_header('Content-ID', '<image2>')
        self.msg.attach(msgImage2)

    def config_file(self):
        """
        config email file
        :return:
        """

        # if the file content is not null, then config the email file
        if self.check_file():
            reportfile = locallog.get_report_path()
            filehtml = MIMEText(open(reportfile).read(), 'base64', 'utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="report.html"'
            self.msg.attach(filehtml)

    def check_file(self):
        """
        check test report
        :return:
        """
        reportpath = self.log.get_report_path()
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        """
        send email
        :return:
        """

        self.config_header()
        self.config_content()
        self.config_file()
        try:
            # smtp = smtplib.SMTP(host, port)
            # smtp.set_debuglevel(1)
            smtp = smtplib.SMTP_SSL(host, port)
            smtp.connect(host, port)
            smtp.login(user, password)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            self.logger.info("The test report has send to developer by email.")
        except Exception as ex:
            self.logger.error(str(ex))


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()
