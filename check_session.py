
import smtplib
from email.message import EmailMessage
from datetime import datetime, time, timedelta



EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use App Passwords if 2FA enabled
TO_EMAIL = "your_email@gmail.com"
URL = "https://tedo.app/"
URL_SESSION = "https://api.tedo.app/web-api/sessions/38"



import requests
import json
from datetime import datetime



def check_and_save():
    url = URL_SESSION
    response = requests.get(url)

    if response.status_code != 404:
        data = response.json()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"session_37_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Session available and saved to {filename}")
    else:
        print("Session not available (404)")







end_time = datetime.now() + timedelta(minutes=6)

while datetime.now() < end_time:
    check_and_save()
    time.sleep(30)






def send_email():
    msg = EmailMessage()
    msg.set_content("B2 Complet is now Disponible.")
    msg["Subject"] = "B2 Complet Available!"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)