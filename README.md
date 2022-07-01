# Automatic Honeygain Lucky Jar

## Requirements

1. Linux or Mac
2. docker

### Setup

#### 1. Create folder + file `accounts/accounts.json` -> add your username/password in the json file

#### 2. Run App

1. Get to your linux/mac system with docker installed.
2. Run this command `docker-compose up -d`

##### Results

```result
>>> HoneyGainBot ran on 2022-07-01 05:09:17.290136:
{'ip': '193.116.*.*136*', 'hostname': 'pc.ztv.ne.jp', 'city': 'Ayabe', 'region': 'Kyoto', 'country': 'JP', 'loc': '35.1678,135.4214', 'org': 'AS9351 ZTV CO.,LTD', 'postal': '622-0214', 'timezone': 'Asia/Tokyo', 'readme': 'https://ipinfo.io/missingauth'}
##- Account demo1***
>-> {'success': True, 'credits': {'credits': 10.0}}
##- Account demo2***
>-> {'success': True, 'credits': {'credits': 100.0}}
##- Account demo3***
>-> {'success': False, 'credits': {'credits': 20.0}}
<<< Next time 2022-07-02 05:24:57.407121:
```
