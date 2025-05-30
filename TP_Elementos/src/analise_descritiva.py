import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def national_economic_analysis(df, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        
        # Verificar se temos os dados necessários
        economic_vars = [col for col in df.columns if col != 'Ano']
        if len(economic_vars) < 1:
            print('Erro: Dados insuficientes para análise.')
            return False
        
        # Gerar gráficos para cada variável econômica
        for var in economic_vars:
            # Evolução temporal
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x='Ano', y=var, marker='o')
            plt.title(f'Evolução de {var} em Portugal')
            plt.xlabel('Ano')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'{var}_evolution.png'))
            plt.close()
            
            # Taxa de crescimento anual
            df[f'Crescimento {var}'] = df[var].pct_change() * 100
            
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x='Ano', y=f'Crescimento {var}', marker='o')
            plt.title(f'Taxa de Crescimento Anual de {var}')
            plt.xlabel('Ano')
            plt.ylabel('Crescimento (%)')
            plt.axhline(0, color='gray', linestyle='--')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f'{var}_growth.png'))
            plt.close()
        
        # Relação entre variáveis (se houver mais de uma)
        if len(economic_vars) > 1:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                data=df, 
                x=economic_vars[0], 
                y=economic_vars[1], 
                hue='Ano',
                palette='viridis',
                size='Ano',
                sizes=(20, 200)
            )
            plt.title(f'Relação entre {economic_vars[0]} e {economic_vars[1]}')
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'economic_relationship.png'))
            plt.close()
        
        # Salvar dados com cálculos de crescimento
        df.to_csv(os.path.join(output_dir, 'dados_economicos.csv'), index=False)
        
        return True
    
    except Exception as e:
        print(f'Erro na análise econômica: {str(e)}')
        return False