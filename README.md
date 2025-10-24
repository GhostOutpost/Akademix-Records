Akademix Attendance QR Emailer
This project allows you to send attendance QR codes to students via email automatically. It uses Python, Gmail SMTP, and Pillow to handle image attachments.
________________________________________
Features
•	Automatically sends an email to a student with their attendance QR code.
•	Supports QR images in PNG or JPEG format.
•	Securely stores email credentials using a .env file.
•	Easy to integrate into any student attendance system.
________________________________________
Setup Instructions
1.	Clone the repository:
2.	git clone https://github.com/GhostOutpost/Akademix-Records.git
cd akademix-main
3.	Install dependencies:
    pip install -r requirements.txt
3.	Create a .env file Use the provided .env.example as a template:
SENDER_EMAIL=your-email@gmail.com
APP_PASSWORD=your-app-password
Important:
SENDER_EMAIL should be your Gmail address.
APP_PASSWORD should be an App Password generated for your Gmail account (not your normal Gmail password).

