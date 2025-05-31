import pandas as pd
import os

def integrate_data(dataframes, output_file):
    try:
        if not dataframes:
            return None

        # Juntar dataframes por ano com left join
        df_final = dataframes[0]
        for df in dataframes[1:]:
            df_final = pd.merge(
                df_final,
                df,
                on='Ano',
                how='left'
            )

        # Ordenar por ano
        df_final = df_final.sort_values('Ano')
        
        # Preencher valores ausentes
        df_final = df_final.ffill().bfill()
        
        # Remover possíveis duplicados
        df_final = df_final.drop_duplicates(subset=['Ano'])
        
        # Garantir nomes consistentes
        df_final = df_final.rename(columns={
            'PIB': 'PIB (em milhões)',
            'PIB_per_capita': 'PIB_per_capita'
        })
        
        # Salvar ficheiro
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df_final.to_csv(output_file, index=False)
        return df_final

    except Exception as e:
        print(f'Erro na integração: {str(e)}')
        return None