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
        
        # Correlações
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 1:
            correlation = df[numeric_cols].corr()
            plt.figure(figsize=(14, 10))  # Aumentado para 14x10
            sns.heatmap(correlation, annot=True, cmap='coolwarm', annot_kws={'size': 8})
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
            plt.close()
        
        # Boxplot para outliers
        if len(numeric_cols) > 0:
            plt.figure(figsize=(14, 8))  # Aumentado para 14x8
            df[numeric_cols].boxplot()
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'outliers_boxplot.png'))
            plt.close()
        
        # Histogramas para distribuição
        for col in numeric_cols:
            plt.figure(figsize=(10, 6))  # Aumentado para 10x6
            sns.histplot(df[col], kde=True)
            plt.title(f'Distribuição de {col}', fontsize=12)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'histogram_{col}.png'))
            plt.close()
        
        # Análise textual de outliers
        report.append('\n=== Análise de Outliers ===')
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            outliers = df[(df[col] < lower) | (df[col] > upper)]
            report.append(f'{col}: {len(outliers)} outliers detectados')
        
        # Salvar relatório
        with open(os.path.join(output_dir, 'eda_report.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
            
        return True
        
    except Exception as e:
        print(f'Erro na EDA: {str(e)}')
        return False
