from trend import SenseTrend

def main():
	trend = SenseTrend(2020,03,31)
	print("trend consumption: " + str(trend.get_daily_consumption()))

if __name__ == '__main__':
	print('Sense data export starting')
	main()