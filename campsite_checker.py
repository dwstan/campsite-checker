import requests
import time
from notification import send_notification, sanity_check, open_browser
import datetime
from collections import defaultdict

def avail_checker(timeout, dates, campground_ids):
    dates_by_month = defaultdict(list)
    for date in dates:
        month = date[:7]  # "YYYY-MM"
        dates_by_month[month].append(date)

    while True:
        for campground_id in campground_ids:
            for month, month_dates in dates_by_month.items():
                try:
                    start_date = month + "-01T00%3A00%3A00.000Z"  # Format start_date as "YYYY-MM-01"
                    url = f"https://www.recreation.gov/api/camps/availability/campground/{campground_id}/month?start_date={start_date}"
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                    }

                    response = requests.get(url, headers=headers)
                    data = response.json()
                except Exception as e:
                    print(f"{datetime.datetime.now()} An error occurred: {e}\nFailed to get data from {url}")
                    continue

                try:
                    for campsite_id, campsite_info in data["campsites"].items():
                        campsite_name = campsite_info["site"]
                        loop_name = campsite_info["loop"]

                        for date in month_dates:
                            print(date, month)
                            availability_key = date + "T00:00:00Z"
                            if availability_key in campsite_info["availabilities"]:
                                availabilities = campsite_info["availabilities"][availability_key]
                                if availabilities == "Available":
                                    print(f"{datetime.datetime.now()} Campsite {campsite_name} is available on {date} in loop {loop_name}")
                                    open_browser(campground_id, campsite_id)
                                # send_notification(campsite_name, date, loop_name, campground_id, campsite_id)

                except Exception as e:
                    print(f"{datetime.datetime.now()} An error occurred: {e}\nThe data received was:\nCampsiteID:{campground_id}\n{data}")

        # current_time = datetime.datetime.now().strftime("%H:%M")
        # if current_time.endswith(":00") or current_time.endswith(":15") or current_time.endswith(":30") or current_time.endswith(":45"):
        #     sanity_check()
        time.sleep(timeout * 60)


