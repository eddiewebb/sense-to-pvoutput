import os
import requests
from dotenv import load_dotenv
import json


class PvOutput():
	def __init__(self):		
		load_dotenv()
		key = os.getenv("PVOUTPUT_KEY")
		site_id = os.getenv("PVOUTPUT_ID")	
		self.headers = {"X-Pvoutput-Apikey": key, "X-Pvoutput-SystemId": site_id}

	def postOutput(self, payload):
		url = "https://pvoutput.org/service/r2/addoutput.jsp"
		print("sending payload as:")
		print(payload)
		r=requests.post(url=url,headers=self.headers,data=payload)
		print r.text

	def postLive(self, payload):
		url = "https://pvoutput.org/service/r2/addstatus.jsp"
		print("sending payload as:")
		print(payload)
		r=requests.post(url=url,headers=self.headers,data=payload)
		print r.text

	