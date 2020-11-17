import smtplib
from email.message import EmailMessage
from decouple import config

def email_alert(subject, body):
    user = config('USER_EMAIL')
    password = config('PASSWORD')
    receiver_email = config('RECEIVER_EMAIL')

    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = receiver_email
    msg['from'] = user

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    email_alert('Shopping list', 'Shopping list contains of: 1. eggs 2. Milk')
