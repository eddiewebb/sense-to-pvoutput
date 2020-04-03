import os
import datetime
import pytz
import requests
from dotenv import load_dotenv
import sense_energy
import json

class SenseTrend():

	def __init__(self):
		load_dotenv()
		user = os.getenv("SENSE_USER")
		passwd = os.getenv("SENSE_PASSWD")	
		self.sense = sense_energy.Senseable()
		self.sense.authenticate(user, passwd)

	
	def load_trends_for(self, year, month, day):
		self.start = datetime.datetime(year,month,day,tzinfo=pytz.timezone("America/New_York"))
		self.data=self.sense.api_call('app/history/trends?monitor_id=50403&scale=DAY&start=' + self.start.isoformat())



	def get_daily_production(self):
		return self.data['production']['total']*1000

	def get_daily_consumption(self):
		return self.data['consumption']['total']*1000

	def get_daily_contribution(self):
		return self.data['to_grid']*1000

	def get_peak_production(self):
		high = 0
		hour = 0
		for step_index, value in enumerate(self.data['production']['totals']):
			if value > high:
				high = value
				hour = step_index
			
		return { "time": str(hour) + ':00', "value": high*1000 }

	def get_date_as(self, format):
		return self.start.strftime(format)


