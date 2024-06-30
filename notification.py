import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os



def send_notification(campsite_name, date):
    load_dotenv()

    sender_email = os.getenv('SENDEREMAIL')
    gateway_address = os.getenv('GATEWAYADDRESS')
    appkey = os.getenv('APPKEY')
    
    if sender_email and gateway_address and appkey:
        msg = EmailMessage()
        msg.set_content(f"Campsite {campsite_name} is available on {date}")

        msg['From'] = sender_email
        msg['To'] = gateway_address
        msg['Subject'] = f"Campsite available!"

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, appkey)

            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    else:
        print("Environment variables not properly set.")

    