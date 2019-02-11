import time
import datetime

import alphavantage as av
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
import pandas as pd
from pandas.io.json import json_normalize #package for flattening json in pandas df

def main():
    data = av.stock_time_series('TIME_SERIES_WEEKLY', 'BRDT3.SAO')
    date = list(data['Weekly Time Series'])
    close_val = [float(data['Weekly Time Series'][item]['4. close']) for item in date]
    date.reverse()
    close_val.reverse()
    plt.figure()
    timestamp = [datetime.datetime.strptime(item, '%Y-%m-%d')for item in date]

   
    plt.plot(timestamp, close_val) 
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == "__main__":
    main()

