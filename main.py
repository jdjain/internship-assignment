import pandas as pd
import numpy as np
from alpha_vantage.timeseries import TimeSeries as TS
import matplotlib.pyplot as plt

key = 'AYYQ1UCKBMWZAMI1'
class ScriptData():
    def fetch_intraday_data(self,script):
        timeseries_object = TS(key,output_format='pandas')
        data = timeseries_object.get_intraday(script,'60min')
        self.data = data
        self.script = script
    
    def convert_intraday_data(self,script):
        self.data = pd.DataFrame(self.data[0]).reset_index(level=0)
        self.data.columns  = ['timestamp','open','high','low','close','volume'] 
        
    def print_intraday_data(self):
        print('\n')
        print('-'*65)
        print('\t\t\t\t\t\tAll Intraday Data')
        print('-'*65,'\n')
        print(self.data)
        return self.data
    
    def line_plot_data(self):
        plt.plot(self.data['open'],label='open data')
        plt.plot(self.data['close'],label='close data')
        plt.xlabel('time series')
        plt.ylabel('rate of the stock')
        plt.legend()
        plt.title('Stock Data')
        plt.show()
        
    def signal(self):
        series = np.where((self.data['open']<self.data['close']),'BUY','SELL')
        self.data['signal'] = series
        print('\n')
        print('-'*65)
        print('\t\t\t\t\t\tSignals')
        print('-'*65,'\n')
        print(self.data[['timestamp','signal']])
    
    
        
def indicator1(data,timeperiod):
    i = 100
    lst = []
    avg = 0
    for i in range(99,-1,-1):
        if i-timeperiod>=0 :
            for j in range(i,i-timeperiod,-1):
                avg += data['close'][j]
            lst.append(round(avg/timeperiod,3))
            avg = 0
        else:
            lst.append(np.NaN)
            
    lst = pd.Series(lst[::-1])  
    dataframe = pd.DataFrame()
    dataframe['timestamp'] = data['timestamp']
    dataframe['indicator'] = lst
    print('\n')
    print('-'*65)
    print('\t\t\t\t\t\t Indicating Data')
    print('-'*65,'\n')
    print(dataframe)
    
    

    
script_data = ScriptData()
script_data.fetch_intraday_data('GOOGL')
script_data.convert_intraday_data('GOOGL')
script_data.print_intraday_data()
script_data.line_plot_data()
indicator1(script_data.print_intraday_data(),timeperiod=5)
script_data.signal()
