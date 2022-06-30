import smtplib

import requests
from datetime import datetime

# 1XX - Hold On
# 2XX: Here You Go
# 3xx: Go Away
# 4XX: You Screwed up
# 5XX: I Screwed Up

# EMAIL
MY_EMAIL = "sasi_ch85@yahoo.co.in"
MY_PASSWD = "wmhkwhvkbmqbaceu"

# Bangalore Email
MY_LAT = 12.971599
MY_LNG = 77.594566


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    ENDPOINT = "http://api.sunrise-sunset.org/json"
    params = {
        # Bangalore Lat/Long
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }

    response = requests.get(ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.utcnow().hour
    print(time_now,sunset, sunrise)
    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: ISS Located above \n\n"
                "ISS is above our location in the sky"
        )
else:
    if not is_night():
        print("Its not night")
    else:
        print("It is night")
    if not is_iss_overhead():
        print("ISS Not located")
