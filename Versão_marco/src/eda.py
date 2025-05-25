import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_eda_report(df, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        report = []
        
        # Estatísticas básicas
        report.append('=== Estatísticas Descritivas ===')
        report.append(str(df.describe().transpose()))
        
        # Valores ausentes
        missing_values = df.isnull().sum()
        report.append('\n=== Valores Ausentes ===')
        report.append(str(missing_values[missing_values > 0]))
        
        # Correlações (apenas colunas numéricas)
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 1:
            correlation = df[numeric_cols].corr()
            plt.figure(figsize=(12, 8))
            sns.heatmap(correlation, annot=True, cmap='coolwarm')
            plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
            plt.close()
        
        # Boxplot para outliers
        if len(numeric_cols) > 0:
            plt.figure(figsize=(10, 6))
            df[numeric_cols].boxplot()
            plt.xticks(rotation=45)
            plt.savefig(os.path.join(output_dir, 'outliers_boxplot.png'))
            plt.close()
        
        # Salvar relatório
        with open(os.path.join(output_dir, 'eda_report.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
            
        return True
        
    except Exception as e:
        print(f'Erro na EDA: {str(e)}')
        return False