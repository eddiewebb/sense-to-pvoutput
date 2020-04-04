import os
import time
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
		asString = self.get_sense_start().strftime('%Y-%m-%dT%X')
		print("Date used with sense: " + asString)
		self.data=self.sense.api_call('app/history/trends?monitor_id=' + str(self.sense.sense_monitor_id) + '&scale=DAY&start=' + asString )
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

	#
	# Sense api errors with UTC offset, you have to muck the start time to incorpoarte TC offset.
	def get_sense_start(self):
		is_dst = time.daylight and time.localtime().tm_isdst > 0
		utc_offset =  (time.altzone if is_dst else time.timezone)
		print("Local utc offset including DST imapct is : " + str(utc_offset))
		return self.start + datetime.timedelta(seconds = utc_offset)

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


