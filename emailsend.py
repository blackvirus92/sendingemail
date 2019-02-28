import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

insyntax = response_text.split()
insyntax2 = insyntax[1]
insyntax3 = insyntax2.split(",")
emailsyntax = insyntax3[0]

email_user = 'email - addres'
email_password = 'Password'
email_send = emailsyntax

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hello Iam djayu how are you?'
msg.attach(MIMEText(body,'plain'))

#if You want to attatch files
'''filename='filename'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
'''
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()