from src.recall import load_multiple_csv, process_pordata_data
from src.integrate import integrate_data
from src.eda import generate_eda_report
from src.limpeza_de_dados import clean_data
from src.analise_descritiva import unsupervised_analysis
from src.relatorio import generate_narrative_report
from src.analise import ranking_desemprego, ranking_empregados, ranking_ensino, ranking_desistentes
import os

def main():
    input_dir = 'data/raw'
    output_dir = 'data/processed'
    output_file = os.path.join(output_dir, 'data_integrada.csv')
    
    dataframes = load_multiple_csv(input_dir)
    if not dataframes:
        print('Nenhum arquivo válido encontrado.')
        return
    
    processed_dfs = []
    for name, df in dataframes.items():
        df_processed = process_pordata_data(df, name)
        if df_processed is not None:
            processed_dfs.append(df_processed)
    
    if not processed_dfs:
        print('Nenhum dado válido após pré-processamento.')
        return
    
    df_final = integrate_data(processed_dfs, output_file)
    if df_final is None:
        print('Falha na integração dos dados.')
        return
    
    eda_dir = os.path.join(output_dir, 'eda')
    analise_dir = os.path.join(output_dir, 'analise')
    report_dir = os.path.join(output_dir, 'relatorio')
    os.makedirs(eda_dir, exist_ok=True)
    os.makedirs(analise_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)
    
    if not generate_eda_report(df_final, eda_dir):
        print('Falha na geração do relatório EDA.')
    
    df_clean = clean_data(df_final)
    if df_clean is None:
        print('Falha na limpeza dos dados.')
        return
    
    clean_output = output_file.replace('.csv', '_clean.csv')
    df_clean.to_csv(clean_output, index=False)
    df_final_clean = integrate_data(processed_dfs, clean_output)
    df_analise = unsupervised_analysis(df_final_clean, analise_dir)
    if df_analise is None:
        print('Falha na análise descritiva.')
        return
    
    if not generate_narrative_report(eda_dir, analise_dir, report_dir):
        print('Falha na geração do relatório narrativo.')
    print(f'\nArquivo integrado: {output_file}')
    print(f'Arquivo limpo: {clean_output}')
    ranking_empregados(df_final_clean)
    ranking_ensino(df_final_clean)
    ranking_desemprego(df_final_clean)
    ranking_desistentes(df_final_clean)
    print(f'\n- Total de registos: {len(df_analise)}')
    print(f'- Total de indicadores: {len(processed_dfs)}')
    print(f'- Período percorrido: {df_analise["Ano"].min()} a {df_analise["Ano"].max()}')
    print(f'- Municípios incluídos: {df_analise["Território"].nunique()}')
    print(f'\nRelatório narrativo salvo em: {report_dir}\n')

if __name__ == '__main__':
    main()