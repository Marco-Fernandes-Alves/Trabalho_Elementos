import pandas as pd
import numpy as np

def clean_data(df):
    try:
        # Preencher NaNs com mediana
        numeric_cols = df.select_dtypes(include='number').columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())
        
        # Remover outliers usando IQR correto
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)  # Quartil correto
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            
        return df
        
    except Exception as e:
        print(f'Erro na limpeza: {str(e)}')
        return None