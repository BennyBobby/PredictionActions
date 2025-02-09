import pandas as pd

def predict_future_prices(new_data, model):
    future_data = pd.DataFrame({
        'MA_5': [new_data['Adj Close'][-5:].mean()],
        'MA_30': [new_data['Adj Close'][-30:].mean()],
        'Price Change': [new_data['Adj Close'].pct_change().iloc[-1]]
    })
    
    predicted_price = model.predict(future_data)  # model est bien un modèle entraîné ici
    return predicted_price[0]
