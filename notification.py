import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import datetime
import webbrowser


load_dotenv(override=True)

sender_email = os.getenv('SENDEREMAIL')
gateway_address_str = os.getenv('GATEWAYADDRESS')
gateway_address_list = gateway_address_str.split(',')
appkey = os.getenv('APPKEY')

def send_notification(campsite_name, date, loop_name, campground_id, campsite_id):
    
    if sender_email and gateway_address_list and appkey:
        for gateway_address in gateway_address_list:
            msg = EmailMessage()
            msg.set_content(f"https://www.recreation.gov/camping/campgrounds/{campground_id}\nhttps://www.recreation.gov/camping/campsites/{campsite_id}\nCamp {campsite_name} is avail {date}, loop {loop_name}\nunsubscribe at dereks.xyz\n{datetime.datetime.now()}")
            msg['From'] = sender_email
            msg['To'] = gateway_address
            msg['Subject'] = f"Campsite available!"

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, appkey)

                server.send_message(msg)
                server.quit()
                print(f"{datetime.datetime.now()} Email sent successfully to {gateway_address}")
            except Exception as e:
                print(f"Failed to send email: {str(e)}")
    else:
        print("Environment variables not properly set.")

def open_browser(campground_id, campsite_id):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(f"https://www.recreation.gov/camping/campsites/{campsite_id}")


def sanity_check():
    if sender_email and gateway_address_list and appkey:
        
        msg = EmailMessage()
        msg.set_content(f"System is online and running\nunsubscribe at dereks.xyz")
        msg['From'] = sender_email
        msg['To'] = gateway_address_list[0]
        msg['Subject'] = f"Sanity check passed"

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, appkey)

            server.send_message(msg)
            server.quit()
            print(f"{datetime.datetime.now()} Sanity email sent successfully to {gateway_address_list[0]}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
    else:
        print("Environment variables not properly set.")
    