import pandas as pd

def clean_data(df):
    try:
        if df.empty:
            print("DataFrame vazio.")
            return None

        # Remover colunas completamente vazias
        df = df.dropna(axis=1, how='all')
        
        # Preencher valores ausentes com a média do indicador
        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if 'Ano' in numeric_cols:
            numeric_cols.remove('Ano')
            
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
            
        return df

    except Exception as e:
        print(f'Erro na limpeza: {str(e)}')
        return None