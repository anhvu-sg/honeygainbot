import os
import json
import requests
import schedule

from pyHoneygain import HoneyGain
from datetime import datetime, timedelta
from time import sleep

def ipinfo():
    # Show current IP address
    try:
        res = requests.get('https://ipinfo.io')
        status = res.status_code
        if int(status) in (204, 404):  # Page not found, no response
            response = False
        else:
            # Some answers return empty content
            response = res.content and res.json() or {}
            print(f"{response}\n", end="")
    except:
        pass

def get_account_datas():
    return json.loads(open("./accounts/accounts.json", 'r').read())

def main():
    accounts_datas = get_account_datas()
    for username, password in accounts_datas.items():
        print(f"##- Account {username[:3]}***")
        try:
            user = HoneyGain()
            user.login(username, password)
            honeypot = user.open_honeypot()
            print(f">-> {honeypot}")
        except Exception as e:
            print(f"### Exception honeypot_by_account: %s" % (e))
        sleep(60*5)

def job():
    print(f">>> START - HoneyGainBot ran on {datetime.now()}:\n\n", end="")
    try:
        main()
    except:
        print("Some sort of error occurred!")
    print(f"<<< END HoneyGainBot ran on {datetime.now()}:\n\n", end="")
    return

HOUR_MIN = os.getenv('HOUR_MIN', '00:30')
STR_HOUR_MIN = "%s" % HOUR_MIN
print(f"Scheduler run everyday at {HOUR_MIN}")
schedule.every().day.at(STR_HOUR_MIN).do(job)
# https://schedule.readthedocs.io/en/stable/examples.html

while True:
    print(f'>> NOW: {datetime.now()}')
    ipinfo()
    schedule.run_pending()
    sleep(60*60)
