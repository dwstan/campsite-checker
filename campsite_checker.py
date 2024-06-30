import requests
import time
from notification import send_notification
import datetime

def avail_checker(timeout, dates, campground_ids):
    while True:
        for campground_id in campground_ids:
            
            url = f"https://www.recreation.gov/api/camps/availability/campground/{campground_id}/month?start_date=2024-07-01T00%3A00%3A00.000Z"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            response = requests.get(url, headers=headers)
            data = response.json()

            try:
                for campsite_id, campsite_info in data["campsites"].items():

                    campsite_name = campsite_info["site"]
                    loop_name = campsite_info["loop"]

                    for date in dates:
                        availability_key = date + "T00:00:00Z"
                        if availability_key in campsite_info["availabilities"]:
                            availabilities = campsite_info["availabilities"][availability_key]
                            if availabilities == "Available":
                                print(f"{datetime.datetime.now()} Campsite {campsite_name} is available on {date} in loop {loop_name}")
                                send_notification(campsite_name, date, loop_name, campground_id)
            except Exception as e:
                print(f"An error occurred: {e}")
        time.sleep(timeout * 60)

