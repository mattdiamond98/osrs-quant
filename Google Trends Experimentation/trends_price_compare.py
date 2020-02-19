import pandas as pd
import os
import matplotlib

file = "abyssal whip_GoogleTrends.txt"
trendsData = pd.read_csv(file)
trendsData['date'] = pd.to_datetime(trendsData['date'], infer_datetime_format=True)
trendsData = trendsData.set_index('date')
trendsData = trendsData.rename(columns={"abyssal whip":'searchQuant'})

trendsData['searchQuant'].plot()
matplotlib.pyplot.show()

file = "whip.txt"
priceData = pd.read_csv(file, parse_dates=[0],
	                 names=['timestamp', 'itemid', 'sellAvg', 'sellQuant', 'buyAvg', 'buyQuant', 'overallAvg', 'overallQuant'])
priceData = priceData[priceData['overallAvg'] >= 1]
priceData['timestamp'] = pd.to_datetime(priceData['timestamp'], unit='ms')
priceData = priceData.set_index('timestamp')
priceData = priceData.drop(['itemid'], axis=1)

jointDataFrame = priceData.join(trendsData, how='outer').interpolate()

jointDataFrame['overallQuant'].plot(legend = True)
jointDataFrame['searchQuant'].plot(secondary_y = True, legend = True)
matplotlib.pyplot.show()
