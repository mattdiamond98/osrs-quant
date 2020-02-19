import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import sys
from util import read_item

def analysis(item, days):
	"""
	Perform a comparison of overallAvg prices, smoothed by a rolling mean.
	Plots multiple days of data on top of eachother to help identify trends.
	:param item: the name of the item to draw the data from
	:param days: the number of days to look back.
	"""

	df = read_item(item)

	roll = df['overallAvg'].rolling(10, center=False, closed='left').mean()
	df['rollingOverallAvg'] = roll

	start_date = datetime(2020, 2, 18 - days)
	end_date = datetime(2020, 2, 18)

	df = df.truncate(before = start_date, after = end_date)

	for single_date in (start_date + timedelta(days = n) for n in range(days)):
		daily_data = df.loc[df.index.date == single_date.date()]['rollingOverallAvg']
		averagePrice = daily_data.mean()
		stdPrice = daily_data.std()
		plt.plot(daily_data.index.time, (daily_data - averagePrice) / stdPrice)
	plt.show()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('usage: python daytime_average.py <item> <days> ...')
	analysis(sys.argv[1], int(sys.argv[2]))
