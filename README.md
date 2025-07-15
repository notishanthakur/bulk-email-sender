# bulk-email-sender
This is a simple Python script to send bulk emails using your email id and a csv sheet as input

# How to use?
## Getting credentials
### For Google
  1. Enable 2FA
  2. Go to https://myaccount.google.com/apppasswords and generate an app password
  3. Use this password in .env
  4. Accordingly select smtp in .env

### For Outlook
  1. Enable MFA
  2. Go to https://mysignins.microsoft.com/security-info, click on Add sign-in method, and generate an app password
  3. Use this password in .env
  4. Accordingly select smtp in .env
  
## On WSL/LINUX based terminal
  1. Clone the repository using `git clone https://github.com/notishanthakur/bulk-email-sender`
  2. Navigate to the folder using `cd bulk-email-sender`
  3. In .env, add your credentials
  4. According to the input.csv, fill in the data as mentioned(refer to customization)
  5. Add your certificates in a folder named `certificates`
  6. Install python-dotenv using `pip install python-dotenv`
  7. Run the script using python3 `python3 script.py`

# Customization
  Fork the repo and modify script.py according to your requirements (easy to read and modify) <br>
  Similarly, also modify input.csv

# Development Info
Made using python3 and imports libraries: 
  1. csv to parse info
  2. smtp to make a connection and send mail
  3. email to craft the message to be sent

# Future Roadmap?
GUI Interface <br>
(Avoiding online deployment due to security factors)
