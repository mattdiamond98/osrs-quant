import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import sys
from util import read_item

def analysis(item):
	df = read_item(item)

	df = df.truncate(before=datetime(2020, 1, 1))

	abs_mean = df['overallAvg'].mean()

	roll = df['overallAvg'].rolling(240, center=False, closed='left').mean()
	norm = (df['overallAvg'] - roll).dropna()

	buckets = [[] for i in range(240)]

	for index, value in norm.items():
		time = index.time()
		b = int((time.hour * 60 + time.minute) / 6)
		buckets[b].append(value)

	daily_data = np.array([np.array(xi) for xi in buckets])

	data_mean = []
	data_std = []

	for data in daily_data:
		data_mean.append(np.mean(data))
		data_std.append(np.std(data))

	data_mean = np.array(data_mean)
	data_std = np.array(data_std)

	plt.plot(data_mean / abs_mean, label=item)
	# plt.plot(data_mean + data_std)
	# plt.plot(data_mean - data_std)

	# plt.plot(data_std)

def multi_analysis(items):
	for item in items:
		analysis(item)
	plt.xticks([0, 60, 120, 180, 240], ['00:00', '6:00', '12:00', '18:00', '24:00'])
	plt.legend()
	plt.title(items)
	plt.show()

if __name__ == '__main__':
	if len(sys.argv) < 1:
		print('usage: python daytime_average.py <item names> ...')
	multi_analysis(sys.argv[1:])

