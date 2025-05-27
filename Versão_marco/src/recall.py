import pandas as pd
import os
import glob

def load_multiple_csv(input_dir):
    dataframes = {}
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))

    if not csv_files:
        print(f"Nenhum arquivo CSV encontrado em {input_dir}")
        return None
    for file_path in csv_files:
        try:
            file_name = os.path.basename(file_path).replace('.csv', '')

            df = pd.read_csv(
                file_path,
                encoding='UTF-16LE',
                skipfooter=4,
                engine='python',
                dtype={'01. Ano': int}
            )

            required_cols = ['01. Ano', '02. Nome Região (Portugal)', '03. Âmbito Geográfico', '09. Valor']

            if not all(col in df.columns for col in required_cols):
                print(f"Arquivo {file_name} não contém colunas obrigatórias. Ignorando...")
                continue

            dataframes[file_name] = df
            print(f" {file_name} carregado com sucesso ({len(df)} linhas)")

        except Exception as e:
            print(f"Erro ao carregar {file_path}: {str(e)}.")
            continue

    return dataframes if dataframes else None

def process_pordata_data(df, indicator_name):
    try:
        df = df.rename(columns={
            '01. Ano': 'Ano',
            '02. Nome Região (Portugal)': 'Território',
            '03. Âmbito Geográfico': 'Tipo_Território',
            '09. Valor': indicator_name
        })
        
        df = df[df['Tipo_Território'] == 'Município']
        df = df[['Ano', 'Território', indicator_name]]
        df = df.dropna()

        df[indicator_name] = pd.to_numeric(df[indicator_name], errors='coerce')
        df = df.dropna(subset=[indicator_name])

        return df

    except Exception as e:
        print(f'Erro no pré-processamento de {indicator_name}: {str(e)}')
        return None
