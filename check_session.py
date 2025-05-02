
import os
import smtplib
from datetime import datetime,  timedelta
import time 
# from dotenv import load_dotenv







# load_dotenv() 
APP_KEY = os.getenv("APP_KEY") 
FROM_EMAIL = os.getenv("FROM_EMAIL") 
TO_EMAIL = os.getenv("FROM_EMAIL") 

URL = os.getenv("URL")
URL_SESSION = os.getenv("URL_SESSION")



def send_email(subject, body, timestamp):

    
    
    content = f"Subject: {subject}\n\n{timestamp}{body}"

    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()

    server.login(FROM_EMAIL , APP_KEY)

    
    try:
        server.sendmail(FROM_EMAIL, TO_EMAIL, content)
        print("mail sent succesfully" , flush= True)

    except Exception as e:
        print(f" Error sending email: {e}")




PAYLOAD = os.getenv("PAYLOAD")

def create_the_post_request(data):
    payload =  json.loads(PAYLOAD)
    payload["session"] = data
    return payload




import requests
import json
from datetime import datetime




def check_and_save():
    url = URL_SESSION
    response = requests.get(url)

    if response.status_code != 404:
        data = response.json()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        data = create_the_post_request(data)
        filename = f"session_37_{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        # print(data)

        send_email("Boosteno" , data, timestamp)
    else:
        print("Session not available (404)")







end_time = datetime.now() + timedelta(minutes=6)

print(f" Script started at {datetime.now()}", flush=True)

while datetime.now() < end_time:

    if not check_and_save():
        break
    
    print(f" Waiting for 30 seconds... Current time: {datetime.now()}", flush=True)
    time.sleep(30)




