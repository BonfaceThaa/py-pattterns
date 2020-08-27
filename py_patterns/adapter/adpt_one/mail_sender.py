import csv
import smtplib
from email.mime.text import MIMEText


class Mailer(object):
    def send(sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = [recipients]

        s = smtplib.SMTP('localhost')
        s.send_message(recipients)
        s.quit()


if __name__ == "__main__":
    user
