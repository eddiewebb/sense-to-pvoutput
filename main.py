import sys
import datetime
from trend import SenseTrend
from pvoutput import PvOutput


def main():
	#authenticate once
	trend = SenseTrend()

	if len(sys.argv) == 4:   
		# specific date
		day = datetime.datetime(year=int(sys.argv[1]), month=int(sys.argv[2]), day=int(sys.argv[3]))
		process(trend, day)
	elif len(sys.argv) == 5:
		# process startng at date N times.
		start_day = datetime.datetime(year=int(sys.argv[1]), month=int(sys.argv[2]), day=int(sys.argv[3]))
		print("Loading " + sys.argv[4] + " days of data starting on " +  start_day.strftime('%Y-%m-%d'))
		for i in range(int(sys.argv[4])):
			target_day = start_day + datetime.timedelta(days = i)
			print(target_day)
			process(trend, target_day)
	elif len(sys.argv) == 1:
		# just yesterday
		now = datetime.datetime.now()
		yesterday = now - datetime.timedelta(days = 1)
		process(trend, yesterday)
	else:
		#invalid
		print("INvalid arguments.")
		exit(1)



def process(trend, when):
	trend.load_trends_for(when)
	pv = PvOutput()
	pv.postOutput(trend.asHistorical())

if __name__ == '__main__':
	print('Sense data export starting')
	main()