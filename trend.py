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
		self.sense = sense_energy.Senseable(api_timeout=10)
		self.sense.authenticate(user, passwd)


	def load_trends_for(self, when):
		self.start=when 
		asString = self.start.strftime('%Y-%m-%dT%X')
		print("Date used with sense: " + asString)
		self.data=self.sense.api_call('app/history/trends?monitor_id=50403&scale=DAY&start=' + asString )
		#print(self.data)

	def asHistorical(self):
		peak = self.get_peak_production()
		payload = {
			"c":self.get_daily_consumption(),
			"e":self.get_daily_contribution(),
			"g":self.get_daily_production(),
			"d":self.get_date_as('%Y%m%d'),
			"pp":peak['value'],
			"pt":peak['time'],
			"ip":self.get_daily_import()
		}
		return payload


	def asLive(self):
		peak = self.get_peak_production()
		payload = {
			"d":self.get_date_as('%Y%m%d'),
			"t":self.get_date_as('%H:%M'),
			"v1":self.get_daily_production(),
			#"v2":9000,
			"v3":self.get_daily_consumption()
			#"v4":800
		}
		return payload








	def get_daily_import(self):
		return self.data['from_grid']*1000


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


