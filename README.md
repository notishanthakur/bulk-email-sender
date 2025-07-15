# bulk-email-sender
This is a simple Python script to send bulk emails using your email id and a csv sheet as input

# How to use?
## On WSL/LINUX based terminal
  1. Clone the repository using `git clone https://github.com/notishanthakur/bulk-email-sender`
  2. Navigate to the folder using `cd bulk-email-sender`
  3. In config.env, add your credentials
  4. According to the input.csv, fill in the data (refer to customization)
  5. Run the script using python3 `python3 script.py`

# Customization
  Fork the repo and modify script.py according to your requirements (easy to read and modify) <br>
  Similarly, also modify input.csv

# Development Info
Made using python3 and imports libraries: csv to parse info, smtp to make a connection and send mail

# Future Roadmap?
GUI Interface
(Avoiding online deployment due to security factors)
