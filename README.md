# pvoutput.org loader for Sense users.

## Setup
1) Create a `.env` file or environment vairables containing API keys for sense and pvoutput.org
2) use pipenv to install dependencies in pipfile.
3) Run commands below


## Live Status Loads

**NOTE:** live data (current watts generated, consumed, to/from grid, voltage) can be sent every 5 or 15 minutes.
**Daily Totals are only updated hourly** this is a limitation of sense, and will match their API/UI.

### Via Cron
The live.py file will load generation and consumpotion currents and totals, along with line voltage.

```
*/15 * * * * /usr/bin/python3 /WHEREVERYOUSAVETHIS/live.py 
```

![Live Status at 5 Minute Interval](/assets/live.png)



## Backfilling

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


![Backfille months of data](/assets/backfill.png)



## Authentication

```
SENSE_USER="YOUR EMAIL"
SENSE_PASSWD="SENSE PASSWORD"
PVOUTPUT_KEY="API KE FROM PV"
PVOUTPUT_ID="SITE ID FROM PV"
```
