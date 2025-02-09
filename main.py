from Data_preprocessing import load_data
from Model import train_model
from Data_prediction import predict_future_prices
from Data_visualisation import plot_stock_prices

data = load_data("IBM.csv")


plot_stock_prices(data)


model = train_model(data)


predicted_price = predict_future_prices(data, model)
print(f"Predicted price for next day: {predicted_price}")
