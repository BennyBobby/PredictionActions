import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_prices(data):
    plt.figure()
    plt.plot(data['Adj Close'], label="Adjusted Close Price", color="green")
    plt.plot(data['Close'], label="Close Price", color="purple")
    plt.title("Close Price vs Adjusted Close Price of IBM")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()

