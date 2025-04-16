import pandas as pd
import os
from utils import load_data, save_predictions

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def naive_forecast(series, periods=30):
    last_value = series.iloc[-1]
    forecast = [last_value for _ in range(periods)]
    return forecast

def run_naive_model():
    processed_path = os.path.join(BASE_DIR, '1_data', 'processed', 'brent_prices_processed.csv')
    output_path = os.path.join(BASE_DIR, '1_data', 'output', 'brent_forecast.csv')

    data = load_data(processed_path)
    predictions = naive_forecast(data['price'], periods=30)
    predictions_df = pd.DataFrame({
        'date': pd.date_range(start=data['date'].iloc[-1], periods=30, freq='D')[1:],
        'forecast': predictions
    })

    save_predictions(predictions_df, output_path)
    print("Previsões naive salvas com sucesso.")

if __name__ == "__main__":
    run_naive_model()
