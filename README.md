# 🎯 Akademix Attendance QR Emailer

This project allows you to **send attendance QR codes to students via email automatically**.  
It uses **Python**, **Gmail SMTP**, and **Pillow** to handle image attachments seamlessly.

---

## 🚀 Features

- 📧 Automatically sends an email to each student with their attendance QR code  
- 🖼️ Supports QR images in **PNG** or **JPEG** format  
- 🔐 Securely stores email credentials using a **.env file**  
- ⚙️ Easy to integrate into any student attendance system  

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/GhostOutpost/Akademix-Records.git
cd Akademix-Records
2️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Create a .env file
Use the provided .env.example as a template and fill it like this:

ini
Copy code
SENDER_EMAIL=your-email@gmail.com
APP_PASSWORD=your-app-password
Important Notes:

SENDER_EMAIL → your Gmail address

APP_PASSWORD → a Gmail App Password (not your normal Gmail password)
How to generate one

🧩 Technologies Used
Python 3

Pillow (PIL)

smtplib

email.message

dotenv

📂 Folder Structure
css
Copy code
Akademix-Records/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
📧 Example Usage
Once set up, running the script will automatically email each student their respective attendance QR code image.

bash
Copy code
python main.py
🧑‍💻 Author
GhostOutpost
https://github.com/GhostOutpost

⭐ If you find this project useful, consider giving it a star on GitHub!
