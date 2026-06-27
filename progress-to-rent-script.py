import requests
import os

from datetime import date
from dateutil.relativedelta import relativedelta

from dotenv import load_dotenv
load_dotenv()

APPL_ID = os.getenv("APPL_ID")
USER_ID = os.getenv("USER_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")

url = f"https://discord.com/api/v9/applications/{APPL_ID}/users/{USER_ID}/identities/0/profile"

def send_rent_update(dayProgress, dayMax):
    data = {
        "username":"Nilo",
        "data": {
            "dynamic": [
                {
                    "type": 2,
                    "name": "dayProgress",
                    "value": dayProgress
                },
                {
                    "type": 2,
                    "name": "dayMax",
                    "value": dayMax
                }
            ]
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {BOT_TOKEN}",
        "User-Agent": "DiscordBot (https://github.com/discord/discord-api-docs, 1.0.0)"
    }

    requests.patch(url, headers=headers, json=data)

born_year = 2008
born_month = 3

rent_age = 85

start = date(born_year, born_month, 1)
end_today = date.today()
end_rent = date(born_year + rent_age, born_month, 1)

rentProgress = relativedelta(end_today, start)
rentMax = relativedelta(end_rent, start)

monthsProgress = rentProgress.months + rentProgress.years * 12
monthsMax = rentMax.months + rentMax.years * 12

send_rent_update(monthsProgress, monthsMax)
