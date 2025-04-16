import pandas as pd
import os
from utils import load_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def process_data():
    raw_path = os.path.join(BASE_DIR, '1_data', 'raw', 'brent_prices.xls')
    processed_path = os.path.join(BASE_DIR, '1_data', 'processed', 'brent_prices_processed.csv')

    df = load_data(raw_path)
    df.dropna(inplace=True)  # limpeza simples
    df.sort_values('date', inplace=True)

    df.to_csv(processed_path, index=False)
    print("Dados processados salvos com sucesso.")

if __name__ == "__main__":
    process_data()
