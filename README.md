# campsite-checker

Make a .env file in the root directory of this project

It should have the following 3 fields:

```
SENDEREMAIL = 'email@gmail.com'
GATEWAYADDRESS = '1234567890@txt.att.net'
APPKEY = '16 digit gmail appkey here'
```

Replace the email with a gmail account of your choice, gateway address is the phone number you want the text sent to, and appkey is the google appkey

appkeys can be acquired [here](https://myaccount.google.com/apppasswords)

list of gateways for phone numbers can be found [here](https://avtech.com/articles/138/list-of-email-to-sms-addresses/)

In the `main.py` there are a few fields:

dates: list of dates you want to check

campground_ids: dictionary of campgrounds and the corresponding campsite

timeout: how many minutes it waits before checking again
