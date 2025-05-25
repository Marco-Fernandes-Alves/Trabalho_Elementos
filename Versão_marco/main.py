from src.recall import load_multiple_csv, process_pordata_data
from src.integrate import integrate_data
from src.eda import generate_eda_report
from src.limpeza_de_dados import clean_data
from src.analise_descritiva import unsupervised_analysis
from src.relatorio import generate_narrative_report
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
    analysis_dir = os.path.join(output_dir, 'analysis')
    report_dir = os.path.join(output_dir, 'relatorio')
    os.makedirs(eda_dir, exist_ok=True)
    os.makedirs(analysis_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)
    
    if not generate_eda_report(df_final, eda_dir):
        print('Falha na geração do relatório EDA.')
    
    df_clean = clean_data(df_final)
    if df_clean is None:
        print('Falha na limpeza dos dados.')
        return
    
    clean_output = output_file.replace('.csv', '_clean.csv')
    df_clean.to_csv(clean_output, index=False)
    
    df_analysis = unsupervised_analysis(df_clean, analysis_dir)
    if df_analysis is None:
        print('Falha na análise descritiva.')
        return
    
    if not generate_narrative_report(eda_dir, analysis_dir, report_dir):
        print('Falha na geração do relatório narrativo.')
    
    print('\n=== Dataset Final ===')
    print(f'Arquivo integrado: {output_file}')
    print(f'Arquivo limpo: {clean_output}')
    print(f'- Total de registros: {len(df_analysis)}')
    print(f'- Total de indicadores: {len(processed_dfs)}')
    print(f'- Período coberto: {df_analysis["Ano"].min()} a {df_analysis["Ano"].max()}')
    print(f'- Municípios incluídos: {df_analysis["Território"].nunique()}')
    print(f'Relatório narrativo salvo em: {report_dir}')

if __name__ == '__main__':
    main()
