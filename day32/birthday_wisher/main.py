##################### Hard Starting Project ######################
import random
import smtplib
import pandas
from datetime import datetime

MY_EMAIL="sasi_ch85@yahoo.co.in"
MY_PASSWD = "Generate App Password"

data = pandas.read_csv("birthdays.csv")

birthdays = {(row.month, row.day): row for (index, row) in data.iterrows()}

now = datetime.now()
today_month = now.month
today_day = now.day

data_row = birthdays[(today_month, today_day)]

random_template_index = random.randint(1, 3)
with open(f"letter_templates/letter_{random_template_index}.txt") as template_file:
    content = template_file.read()
    content = content.replace('[NAME]', data_row["name"])
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWD)
        message = f"Subject:Happy Birthday\n\n{content}"
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=data_row["email"],
                            msg=message)

