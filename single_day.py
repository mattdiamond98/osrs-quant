import pandas as pd
from datetime import datetime, timedelta, time
import numpy as np
import matplotlib.pyplot as plt
import sys
from util import read_item

def analysis(item, year, month, day):
	"""
	Plot the buy and sell price and quanitities on two side by side
	graphs for a single day.
	:param item: the name of the item to draw the data from
	:param year, month, day: the date to analyze
	"""
	df = read_item(item)
	df = df.truncate(before=datetime(year, month, day), after=datetime(year, month, day + 1)).dropna()
	df.index = df.index.time
	plt.subplot(2, 1, 1)
	plt.title(f'{item} {year}-{month}-{day}')
	plt.plot(df['buyAvg'].loc[df['buyAvg'] != 0], label='buyAvg')
	plt.plot(df['sellAvg'].loc[df['sellAvg'] != 0], label='sellAvg')
	plt.xticks([time(n) for n in [2, 6, 10, 14, 18, 22]])
	plt.legend()
	plt.subplot(2, 1, 2)
	plt.plot(df['buyQuant'], label='buyQuant')
	plt.plot(df['sellQuant'], label='sellQuant')
	plt.xticks([time(n) for n in [2, 6, 10, 14, 18, 22]])
	plt.legend()
	plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print('usage: python single_day.py <item> <year> <month> <day>')
	analysis(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))