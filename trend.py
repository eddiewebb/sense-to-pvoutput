import os
import datetime
import pytz
import requests
from dotenv import load_dotenv
import sense_energy
import json

class SenseTrend():

	def __init__(self, year, month, day):
		self.start = datetime.datetime(year,month,day,tzinfo=pytz.timezone("America/New_York"))


		load_dotenv()

		user = os.getenv("SENSE_USER")
		passwd = os.getenv("SENSE_PASSWD")	
		sense = sense_energy.Senseable()
		sense.authenticate(user, passwd)

		self.data=sense.api_call('app/history/trends?monitor_id=50403&scale=DAY&start=' + self.start.isoformat())
		

	def get_daily_production(self):
		return self.data['production']['total']*1000

	def get_daily_consumption(self):
		return self.data['consumption']['total']*1000

	def get_daily_contribution(self):
		return self.data['to_grid']*1000


