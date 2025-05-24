from src.recall import load_multiple_csv, process_pordata_data
from src.integrate import integrate_data
import os
def main():
    input_dir = "data/raw"
    output_dir = "data/processed"
    output_file = os.path.join(output_dir, "data_integrada.csv")
    dataframes = load_multiple_csv(input_dir)
    if not dataframes:
        print(" Nenhum arquivo válido encontrado.")
    processed_dfs = []
    for name, df in dataframes.items():
        df_processed = process_pordata_data(df, name)
        if df_processed is not None:
            processed_dfs.append(df_processed)
    if not processed_dfs:
        return
    df_final = integrate_data(processed_dfs, output_file)
    if df_final is None:
        return
    print(f"Arquivo gerado: {output_file}")
    print("\nEstatísticas do dataset final:")
    print(f"- Total de registros: {len(df_final)}")
    print(f"- Total de indicadores: {len(processed_dfs)}")
    print(f"- Período coberto: {df_final['Ano'].min()} a {df_final['Ano'].max()}")
    print(f"- Municípios incluídos: {df_final['Território'].nunique()}")
    print('\n Ainda a trabalhar o resto :)')


if __name__ == "__main__":
    main()