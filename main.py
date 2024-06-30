import requests
from campsite_checker import avail_checker


timeout = 1 # how many minutes between checks
dates = ["2024-07-06", "2024-07-13"] # the start date you want to check availability for
campground_ids = {"10004152": "10046502"} # the campground ids you want to check availability for

avail_checker(timeout, dates, campground_ids)