import pandas as pd
import numpy as np

def load_data(file_path):
    data = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    data = data[['Adj Close', 'Close']] 
    data = data.ffill()
    data['MA_5'] = data['Adj Close'].rolling(window=5).mean()
    data['MA_30'] = data['Adj Close'].rolling(window=30).mean()
    data["Price Change"] = data["Adj Close"].pct_change()
    data = data.dropna()
    return data
