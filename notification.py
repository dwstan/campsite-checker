import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os


load_dotenv(override=True)

sender_email = os.getenv('SENDEREMAIL')
gateway_address = os.getenv('GATEWAYADDRESS')
appkey = os.getenv('APPKEY')

def send_notification(campsite_name, date, loop_name, campground_id):

    
    if sender_email and gateway_address and appkey:
        msg = EmailMessage()
        msg.set_content(f"Campsite {campsite_name} is available on {date} in loop {loop_name}\n\nhttps://www.recreation.gov/camping/campgrounds/{campground_id}")

        msg['From'] = sender_email
        msg['To'] = gateway_address
        msg['Subject'] = f"Campsite available!"

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, appkey)

            server.send_message(msg)
            server.quit()
            print(f"Email sent successfully to {gateway_address}!")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    else:
        print("Environment variables not properly set.")

    