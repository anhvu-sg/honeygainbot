import json

from pyHoneygain import HoneyGain
from datetime import datetime, timedelta
from time import sleep

def get_account_datas():
    return json.loads(open("./accounts/accounts.json", 'r').read())

def main():
    accounts_datas = get_account_datas()
    for username, password in accounts_datas.items():
        print(f"##- Account {username}")
        try:
            user = HoneyGain()
            user.login(username, password)
            honeypot = user.open_honeypot()
            print(f">>-> {honeypot}")
        except Exception as e:
            print(f"### Exception honeypot_by_account: %s" % (e))
        waiting_time = 60*5 # Waiting 5 minutes for each account
        print(f"** Next account: {datetime.now()+ timedelta(seconds=waiting_time)}:\n", end="")
        sleep(waiting_time)

while True:
    print(f">>> HoneyGainBot ran on {datetime.now()}:\n", end="")
    try:
        main()
    except:
        print("Some sort of error occurred!")
    next_time = 60 * 60 * 24 # Every 24 hours
    print(f"<<< Next time {datetime.now()+ timedelta(seconds=next_time)}:\n\n", end="")
    sleep(next_time)

