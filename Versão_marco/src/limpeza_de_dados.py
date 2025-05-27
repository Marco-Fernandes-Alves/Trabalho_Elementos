import pandas as pd
from scipy.stats import mstats

def clean_data(df):
    try:
        if df.empty:
            print("DataFrame vazio.")
            return None

        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if 'Ano' in numeric_cols:
            numeric_cols.remove('Ano')
        if 'Território' in numeric_cols:
            numeric_cols.remove('Território')

        colunas_com_dados = []
        for col in numeric_cols:
            if not (df[col] == 0).all():
                colunas_com_dados.append(col)
        df = df[['Ano', 'Território'] + colunas_com_dados]

        if len(colunas_com_dados) > 0:
            for col in colunas_com_dados:
                df[col] = mstats.winsorize(df[col], limits=[0.05, 0.05])

        return df

    except Exception as e:
        print(f'Erro na limpeza: {str(e)}')
        return None
