import pandas as pd
import numpy as np
from scipy.stats import mstats

def clean_data(df):
    try:
        # Preencher NaNs com mediana
        numeric_cols = df.select_dtypes(include='number').columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())
        
        # Winsorization para outliers
        for col in numeric_cols:
            df[col] = mstats.winsorize(df[col], limits=[0.05, 0.05])
        
        return df
        
    except Exception as e:
        print(f'Erro na limpeza: {str(e)}')
        return None
