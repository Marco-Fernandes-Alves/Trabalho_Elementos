import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_eda_report(df, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        report = []
        
        # Estatísticas básicas
        stats = df.describe().transpose()
        report.append('## Estatísticas Descritivas\n')
        report.append(stats.to_markdown())
        
        # Histogramas para variáveis econômicas
        economic_vars = [col for col in df.columns if col != 'Ano']
        for var in economic_vars:
            plt.figure(figsize=(10, 6))
            sns.histplot(df[var], kde=True, bins=15)
            plt.title(f'Distribuição de {var}')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'histogram_{var}.png'))
            plt.close()
            
            # Análise de outliers
            q1 = df[var].quantile(0.25)
            q3 = df[var].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = df[(df[var] < lower_bound) | (df[var] > upper_bound)]
            report.append(f'\n**{var}** - Outliers: {len(outliers)}')
        
        # Salvar relatório
        with open(os.path.join(output_dir, 'eda_report.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
            
        return True
        
    except Exception as e:
        print(f'Erro na EDA: {str(e)}')
        return False