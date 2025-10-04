import smtplib
from email.message import EmailMessage
from PIL import Image
import os
from dotenv import load_dotenv
load_dotenv()

def sendQR(studentID, studentEmail):
    Sender_Email = os.getenv("SENDER_EMAIL")
    Password = os.getenv("APP_PASSWORD")
    Reciever_Email = studentEmail

    newMessage = EmailMessage()
    newMessage['Subject'] = "Your Attendance QR Code"
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content(
        "Scan the QR to mark your attendance for the day."
    )

    file_path = f"./QR/QR_STUDENT_{studentID}.png"

    with open(file_path, 'rb') as f:
        image_data = f.read()
        # Use Pillow instead of imghdr
        with Image.open(file_path) as img:
            image_type = img.format.lower()   # e.g. "png", "jpeg"
        image_name = f.name

    newMessage.add_attachment(
        image_data,
        maintype='image',
        subtype=image_type,
        filename=image_name
    )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)
        smtp.send_message(newMessage)
