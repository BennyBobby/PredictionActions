import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from Data_preprocessing import load_data

def train_model(data):
    train_size = int(len(data) * 0.5)
    train_data = data[:train_size]
    test_data = data[train_size:]

    X_train = train_data[['MA_5', 'MA_30', 'Price Change']]
    y_train = train_data['Adj Close']
    X_test = test_data[['MA_5', 'MA_30', 'Price Change']]
    y_test = test_data['Adj Close']

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f'RMSE: {rmse}')
    print(f'R²: {r2}')
    return model 
