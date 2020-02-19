import pandas as pd

def read_item(item):
	return pd.read_excel('data/' + item + '.xlsx', parse_dates=[0], index_col=0)