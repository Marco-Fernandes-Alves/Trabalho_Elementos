from src.recall import load_multiple_csv, process_pordata_data
from src.integrate import integrate_data
from src.eda import generate_eda_report
from src.limpeza_de_dados import clean_data
from src.analise_descritiva import national_economic_analysis
from src.relatorio import generate_narrative_report
import os

def main():
    input_dir = 'data/raw'
    output_dir = 'data/processed'
    output_file = os.path.join(output_dir, 'data_integrada.csv')
    
    # Carregar e processar dados
    data_tuples = load_multiple_csv(input_dir)
    if not data_tuples:
        print('Nenhum arquivo válido encontrado.')
        return
    
    processed_dfs = []
    for name, data_tuple in data_tuples.items():
        df_processed = process_pordata_data(data_tuple, name)
        if df_processed is not None:
            processed_dfs.append(df_processed)
    
    if not processed_dfs:
        print('Nenhum dado válido após pré-processamento.')
        return
    
    # Integrar dados
    df_final = integrate_data(processed_dfs, output_file)
    if df_final is None:
        print('Falha na integração dos dados.')
        return
    
    # Criar diretórios de saída
    eda_dir = os.path.join(output_dir, 'eda')
    analise_dir = os.path.join(output_dir, 'analise')
    report_dir = os.path.join(output_dir, 'relatorio')
    os.makedirs(eda_dir, exist_ok=True)
    os.makedirs(analise_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)
    
    # Análise exploratória
    if not generate_eda_report(df_final, eda_dir):
        print('Falha na geração do relatório EDA.')
    
    # Limpeza de dados
    df_clean = clean_data(df_final)
    if df_clean is None:
        print('Falha na limpeza dos dados.')
        return
    
    clean_output = output_file.replace('.csv', '_clean.csv')
    df_clean.to_csv(clean_output, index=False)
    
    # Análise econômica
    if not national_economic_analysis(df_clean, analise_dir):
        print('Falha na análise econômica.')
        return
    
    # Relatório final
    if not generate_narrative_report(eda_dir, analise_dir, report_dir):
        print('Falha na geração do relatório narrativo.')
    
    # Resumo final
    print(f'\nProcessamento concluído com sucesso!')
    print(f'- Total de anos analisados: {len(df_clean)}')
    print(f'- Período: {df_clean["Ano"].min()} a {df_clean["Ano"].max()}')
    print(f'- Indicadores integrados: {", ".join([col for col in df_clean.columns if col != "Ano"])}')
    print(f'\nRelatório narrativo salvo em: {os.path.join(report_dir, "relatorio_economico.md")}')

if __name__ == '__main__':
    main()