import pandas as pd
import glob
import os

def cleaner(file):
	df = pd.read_csv(file, parse_dates=[0],
	                 names=['timestamp', 'itemid', 'sellAvg', 'sellQuant', 'buyAvg', 'buyQuant', 'overallAvg', 'overallQuant'])
	df = df[df['overallAvg'] >= 1]
	df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
	df = df.set_index('timestamp')
	df = df.drop(['itemid'], axis=1)
	df.to_excel('data/' + file.replace('.txt', '') + '.xlsx')

if __name__ == '__main__':
	text_files = glob.glob('*.txt')
	print("found", text_files)
	for file in text_files:
		cleaner(file)
		os.remove(os.getcwd() + "\\" + file)
	print('files cleaned')