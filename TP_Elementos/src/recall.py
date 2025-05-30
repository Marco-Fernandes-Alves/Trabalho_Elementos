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
            print(f"Processando {file_name}...")
            
            # Detectar formato baseado no nome do arquivo
            if "PIB_per_capita" in file_name:
                value_col = '10. Valor'
                region_col = '03. Nome Região (Portugal)'
                skipfooter = 4
            else:
                value_col = '09. Valor'
                region_col = '03. Nome Região (Portugal)'
                skipfooter = 4

            # Tentar diferentes codificações
            encodings = ['utf-8', 'latin-1', 'cp1252']
            df = None
            
            for encoding in encodings:
                try:
                    df = pd.read_csv(
                        file_path,
                        encoding=encoding,
                        sep=',',
                        skipfooter=skipfooter,
                        engine='python',
                        thousands='.',
                        decimal=',',
                        dtype={'01. Ano': int}
                    )
                    print(f"Codificação bem-sucedida: {encoding}")
                    break
                except Exception as e:
                    print(f"Tentativa com {encoding} falhou: {str(e)}")
                    continue
            
            if df is None:
                print(f"Não foi possível ler {file_path}")
                continue
                
            # Verificar colunas obrigatórias
            required_cols = ['01. Ano', region_col, value_col]
            missing_cols = [col for col in required_cols if col not in df.columns]
            
            if missing_cols:
                print(f"Arquivo {file_name} não contém colunas obrigatórias: {', '.join(missing_cols)}")
                print(f"Colunas disponíveis: {', '.join(df.columns)}")
                continue
                
            dataframes[file_name] = (df, value_col, region_col)
            print(f"{file_name} carregado com sucesso ({len(df)} linhas)")

        except Exception as e:
            print(f"Erro ao carregar {file_path}: {str(e)}")
            continue

    return dataframes if dataframes else None

def process_pordata_data(data_tuple, indicator_name):
    try:
        df, value_col, region_col = data_tuple
        
        # Renomear colunas
        df = df.rename(columns={
            '01. Ano': 'Ano',
            value_col: indicator_name
        })
        
        # Filtrar apenas dados de Portugal
        if region_col in df.columns:
            df = df[df[region_col] == 'Portugal']
        else:
            print("Atenção: Coluna de região não encontrada. Usando todos os dados.")
        
        # Selecionar apenas as colunas necessárias
        df = df[['Ano', indicator_name]].copy()
        
        # Converter para numérico
        df[indicator_name] = pd.to_numeric(
            df[indicator_name].astype(str).str.replace(',', '.'), 
            errors='coerce'
        )
        
        df = df.dropna(subset=[indicator_name])
        return df

    except Exception as e:
        print(f'Erro no pré-processamento de {indicator_name}: {str(e)}')
        return None