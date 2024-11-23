# Keylogger

This repository contains a basic keylogger implementation in Python using the `pynput` and `smtplib` libraries. It captures keystrokes, stores them in a log, and periodically sends the log via email.

---

## Features

- **Keystroke Logging**: Captures user keystrokes in real time.
- **Periodic Emailing**: Sends the log to a specified email address every 30 seconds.
- **Customizable Inputs**: Supports user-specified email and password through command-line arguments.

---

## Requirements

- Python 3.x
- Libraries: 
  - `pynput`
  - `smtplib`
  - `optparse`
  - `threading`

To install dependencies, run:
```bash
pip install pynput
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/FurkanRecber/Keylogger.git
   cd Keylogger
   ```
   
2. Run the keylogger:

  ```bash
  python keylogger.py -e <your-email@gmail.com> -p <your-email-password>
  ```
Replace `your-email@gmail.com` and `your-email-password` with your Gmail credentials. Ensure you have "Less secure app access" enabled for the Gmail account.

The script will:

- Capture all keystrokes.
- Send the log to the specified email every 30 seconds.

## Disclaimer
This keylogger is for educational purposes only. Unauthorized use of this software for malicious purposes is illegal and strictly prohibited. The creator is not responsible for any misuse of this program.
