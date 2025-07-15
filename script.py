import csv, smtplib

from dotenv import load_dotenv
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

input_path = os.getenv("input_path")
emailHandler = smtplib.SMTP(os.getenv("smtp"), os.getenv("port"))
email_id = os.getenv("email_id")
password = os.getenv("password")

try:
    emailHandler.starttls()

except Exception as e:
    print("Error initialising email service ", e)

emailHandler.login(email_id, password)

try:
    with open(input_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)

        count = 0

        for row in reader:
            
            
#constructing message
            msg = MIMEMultipart()            
            msg['From'] = email_id
            msg['To'] = row[0]
            
            msg['Subject'] = "Congrulations for participating at " + row[2]
            
            body = "Hi " + row[1] + "\n" + "Congratulations for " + row[3] + " in " + row[2] + " at " + row[4] + "\nThe certificate is attached below\n\nThank you"
            
            msg.attach(MIMEText(body, 'plain'))

            certificate = row[5]
            attachment = open("./certificates/" + row[5], "rb")
            new = MIMEBase('application', 'octet-stream')
            new.set_payload((attachment).read())
            encoders.encode_base64(new)
            new.add_header('Content-Disposition', "attachment; filename= %s" %certificate)
            msg.attach(new)

            text = msg.as_string()
            emailHandler.sendmail(email_id, row[0], text)
            print("Sent email to: " + row[0])
            count+=1


        print("/nTotal " + count + " emails sent")
        
        emailHandler.quit()

except FileNotFoundError:
    print("File not found on path ", input_path)

except Exception as e:
    print("Unknown error ", e)