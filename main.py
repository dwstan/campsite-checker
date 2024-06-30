import requests
from campsite_checker import avail_checker
from dotenv import load_dotenv
import os

timeout = 1 # how many minutes between checks
dates = ["2024-07-06", "2024-07-13", "2024-07-20", "2024-07-27"] # the start date you want to check availability for
campground_ids = {"10004152", "232450", "232449", "232447"} # the campground ids you want to check availability for

avail_checker(timeout, dates, campground_ids)