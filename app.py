from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from jinja2 import Environment, PackageLoader, select_autoescape
import smtplib

from config import ID, PASSWORD

env = Environment(
    loader=PackageLoader('app', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

EMAIL_USER = ID
EMAIL_PASSWORD = PASSWORD

def make(sender, receiver, title, content, files=[]):
  msg = MIMEMultipart('alternative')
  msg['Subject'] = "%s"%(title)
  msg['From'] = sender
  msg['To'] = receiver
  html = MIMEText(content, 'html')
  
  msg.attach(html)

  # for file in files:
  #   with open(file, 'rb') as fp:
  #     print(fp.read())
  #     img = MIMEImage(fp.read(), 'txt')
      
  #     msg.attach(img)

  return msg.as_string()

def template(payload, html_template='index.html'):
  t = env.get_template(html_template)
  return t.render(text1=payload['text1'], text2=payload['text2'])

def send(receiver, title, payload, html_template='index.html',  files=[]):
  print(receiver, payload)
  # server = smtplib.SMTP_SSL('smtp.naver.com', 465)
  # server.login(EMAIL_USER, EMAIL_PASSWORD)

  html_message = template(payload, html_template)
  body = make(EMAIL_USER, receiver, title, html_message, files)
  print(body)
  # server.sendmail(EMAIL_USER, [receiver], body)
  # server.quit()

  return True

if __name__ == '__main__':
  reveiver_email = "pjt3591oo@gmail.com"
  title = "[공지사항] 멍개 존멋"
  html_template = 'index.html'
  payload = {
    "text1": "t1",
    "text2": "t2"
  }
  files=['test.txt', 'test1.txt']
  email_res = send(reveiver_email, title, payload, html_template, files)
  print(email_res)

