import pandas as pd
import os

def load_data(path):
    ext = os.path.splitext(path)[1].lower()

    # Leitura do Excel ou CSV
    if ext in ['.xls', '.xlsx']:
        df = pd.read_excel(path)
    elif ext == '.csv':
        df = pd.read_csv(path)
    else:
        raise ValueError("Formato de arquivo não suportado.")

    # Padroniza nomes das colunas
    df.columns = df.columns.str.strip().str.lower()

    # Converte 'date' com meses em português — usa locale-aware parsing
    meses_pt = {
        'jan': 'jan', 'fev': 'feb', 'mar': 'mar', 'abr': 'apr',
        'mai': 'may', 'jun': 'jun', 'jul': 'jul', 'ago': 'aug',
        'set': 'sep', 'out': 'oct', 'nov': 'nov', 'dez': 'dec'
    }
    df['date'] = df['date'].astype(str).str.lower()
    for pt, en in meses_pt.items():
        df['date'] = df['date'].str.replace(pt, en)

    df['date'] = pd.to_datetime(df['date'], format="%b %d, %Y", errors='coerce')

    # Corrige separador decimal e converte para float
    df['price'] = df['price'].astype(str).str.replace(',', '.').astype(float)

    # Remove qualquer linha inválida
    return df.dropna(subset=['date', 'price'])

def save_predictions(df, path):
    df.to_csv(path, index=False)
