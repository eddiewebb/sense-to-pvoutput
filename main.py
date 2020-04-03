import sys
import datetime
import pytz
from trend import SenseTrend
from pvoutput import PvOutput


def main():
	#authenticate once
	trend = SenseTrend()

	if len(sys.argv) == 4:   
		# specific date
		process(trend, int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
	elif len(sys.argv) == 5:
		# process startng at date N times.
		start_day = datetime.datetime(year=int(sys.argv[1]), month=int(sys.argv[2]), day=int(sys.argv[3]))
		print("Loading " + sys.argv[4] + " days of data starting on " +  start_day.strftime('%Y-%m-%d'))
		for i in range(int(sys.argv[4])):
			target_day = start_day + datetime.timedelta(days = i)
			print(target_day)
			process(trend, target_day.year, target_day.month, target_day.day)
	elif len(sys.argv) == 1:
		# just yesterday
		now = datetime.datetime.now().replace(tzinfo=pytz.timezone("America/New_York"))
		yesterday = now - datetime.timedelta(days = 1)
		process(trend, yesterday.year, yesterday.month, yesterday.day)
	else:
		#invalid
		print("INvalid arguments.")
		exit(1)



def process(trend, year, month, day):
	trend.load_trends_for(year, month, day)
	pv = PvOutput()
	pv.fromSenseOutput(trend)

if __name__ == '__main__':
	print('Sense data export starting')
	main()