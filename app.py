from email.mime.multipart import MIMEMultipart
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

message = MIMEMultipart()
message["from"] = "Mosh Hamedani"
message["to"] = "testuser@codewithmosh.com"
message["subject"] = "This is a test"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("car.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("onyangofredrickoguya@gmail.com", "weijods392io3892iw;l,.")
    smtp.send_message(message)
    print("sent ...")
