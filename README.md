# pvoutput.org loader for Sense users.

This is intended to *backfill* missing data in PVOutput from Sense Energy Monitor.

**For live updates, use (sense-show)[https://github.com/eddiewebb/sense-show/blob/master/pvoutput.py] instead.**


## Setup
1) Create a `.env` file or environment vairables containing API keys for sense and pvoutput.org
2) use pipenv to install dependencies in pipfile.
3) Run commands below


## Commands

### Backfill one day

```
# main.py YYYY MM DD
pipenv run python main.py 2020 02 01
```

### Backfill many days
Just be aware of your API limits!

```
# main.py YYYY MM DD DAYS
pipenv run python main.py 2020 02 01 29 #leap year!
> Loading 29 days of data starting on 2020-02-01
```

### Backfil yesterday

```
# no argument run
pipenv run python main.py
```


## Authentication

```
SENSE_USER="YOUR EMAIL"
SENSE_PASSWD="SENSE PASSWORD"
PVOUTPUT_KEY="API KE FROM PV"
PVOUTPUT_ID="SITE ID FROM PV"
```