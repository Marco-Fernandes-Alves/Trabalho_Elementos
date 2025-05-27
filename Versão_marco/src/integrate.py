import pandas as pd
import os

def integrate_data(dataframes, output_file):
    try:
        if not dataframes:
            return None

        df_final = dataframes[0]
        for df in dataframes[1:]:
            df_final = pd.merge(
                df_final,
                df,
                on=['Ano', 'Território'],
                how='outer'
            )

        df_final = df_final.fillna(0)
        colunas_para_remover = []

        for col in df_final.columns:
            if col not in ['Ano', 'Território']:
                if (df_final[col] == 0).all() or df_final[col].isnull().all():
                    colunas_para_remover.append(col)

        df_final = df_final.drop(columns=colunas_para_remover)
        df_final = df_final.sort_values(['Ano', 'Território'])
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df_final.to_csv(output_file, index=False, encoding='utf-8')
        return df_final

    except Exception as e:
        print(f'Erro na integração: {str(e)}')
        return None
