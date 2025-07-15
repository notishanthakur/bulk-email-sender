import csv,smtplib


input_path = 'input.csv' #enter path here
emailhandler = smtplib.SMTP('',) #'smtp', port
email_id = ""  #enter email
password = ""  #enter password

try:
    emailhandler.starttls()

except Exception as e:
    print("Error initialising email service ", e)

emailhandler.login(email_id, password)

try:
    with open(input_path, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader) 
        for row in reader:
            print(row)

except FileNotFoundError:
    print("File not found on path ", input_path)

except Exception as e:
    print("Unknown error ", e)