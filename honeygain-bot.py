import json
import requests

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

while True:
    print(f">>> HoneyGainBot ran on {datetime.now()}:\n", end="")
    next_time = 60 * 60 * 24 # Every 24 hours
    try:
        ipinfo()
        main()
    except:
        print("Some sort of error occurred!")
    print(f"<<< Next time {datetime.now()+ timedelta(seconds=next_time)}:\n\n", end="")
    sleep(next_time)

