from pytrends.request import TrendReq
from pandas import DataFrame
import matplotlib
import os

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ['abyssal whip'] #update this array with whichever keyword(s) you want to query
payload = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
data = pytrends.get_historical_interest(kw_list, year_start=2020, month_start=2, day_start=12, hour_start=0,
                                 year_end=2020, month_end=2, day_end=19, hour_end=0, cat=0, geo='', gprop='', sleep=5)
print(data.to_csv()) #debug

#uncomment the below lines to save the data
#f = open(kw_list[0]+"_GoogleTrends.txt", "a+") #writes the data to a text file in csv format (it has headers)
#f.write(data.to_csv())
#f.close()

data.plot()
matplotlib.pyplot.show()
