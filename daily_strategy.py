import pandas as pd
from datetime import datetime, timedelta, time
import numpy as np
import matplotlib.pyplot as plt
import sys
from util import read_item

def analysis():
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

if __name__ == '__main__':
	if len(sys.argv) < 1:
		print('usage: python single_day.py <item>')
	analysis(sys.argv[1])