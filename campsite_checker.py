import requests

def avail_checker(timeout, dates, campground_ids):
    for campsite_id in campground_ids:
        campground_id = campground_ids[campsite_id]
        url = f"https://www.recreation.gov/api/camps/availability/campground/{campsite_id}/month?start_date=2024-07-01T00%3A00%3A00.000Z"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        campsite_name = data["campsites"][campground_id]["site"]

        for date in dates:
            availabilities = data["campsites"][campground_id]["availabilities"][date + "T00:00:00Z"]
            if availabilities == "Open":
                print(f"Campsite {campsite_name} is available on {date}")

