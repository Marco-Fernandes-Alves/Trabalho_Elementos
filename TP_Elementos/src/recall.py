import pandas as pd
import os
import glob

def load_multiple_csv(input_dir):
    dataframes = {}
    csv_files = glob.glob(os.path.join(input_dir, "*.csv"))

    if not csv_files:
        print(f"Nenhum ficheiro CSV encontrado em {input_dir}")
        return None
        
    for file_path in csv_files:
        try:
            file_name = os.path.basename(file_path).replace('.csv', '')
            print(f"Processando {file_name}...")
            
            # Determinar formato baseado no nome do ficheiro
            if "PIB_per_capita" in file_name:
                value_col = '10. Valor'
                skipfooter = 4
            else:
                value_col = '09. Valor'
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
                        dtype={'01. Ano': str}  # Manter como string para tratamento
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
            required_cols = ['01. Ano', '03. Nome Região (Portugal)', value_col]
            missing_cols = [col for col in required_cols if col not in df.columns]
            
            if missing_cols:
                print(f"Ficheiro {file_name} não contém colunas obrigatórias: {', '.join(missing_cols)}")
                print(f"Colunas disponíveis: {', '.join(df.columns)}")
                continue
                
            dataframes[file_name] = (df, value_col)
            print(f"{file_name} carregado com sucesso ({len(df)} linhas)")

        except Exception as e:
            print(f"Erro ao carregar {file_path}: {str(e)}")
            continue

    return dataframes if dataframes else None

def process_pordata_data(data_tuple, indicator_name):
    try:
        df, value_col = data_tuple
        
        # Definir nomes descritivos para as colunas
        name_mapping = {
            'PIB': 'PIB (em milhões)',
            'PIB_per_capita': 'PIB_per_capita'
        }
        
        new_name = name_mapping.get(indicator_name, indicator_name)
        
        # Renomear colunas
        df = df.rename(columns={
            '01. Ano': 'Ano',
            value_col: new_name
        })
        
        # Filtrar apenas dados de Portugal
        if '03. Nome Região (Portugal)' in df.columns:
            df = df[df['03. Nome Região (Portugal)'] == 'Portugal']
        else:
            print("Atenção: Coluna de região não encontrada. Usando todos os dados.")
        
        # Selecionar apenas as colunas necessárias
        df = df[['Ano', new_name]].copy()
        
        # Converter ano para numérico
        df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce')
        
        # Tratamento numérico avançado
        df[new_name] = (
            df[new_name]
            .astype(str)
            .str.replace(r'\.(\d{3})', r'\1', regex=True)
            .str.replace(',', '.', regex=False)
            .apply(pd.to_numeric, errors='coerce')
        )
        
        # Remover duplicados mantendo primeiro valor
        df = df.drop_duplicates(subset=['Ano'], keep='first')
        
        df = df.dropna(subset=[new_name])
        return df

    except Exception as e:
        print(f'Erro no pré-processamento de {indicator_name}: {str(e)}')
        return None