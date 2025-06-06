import os
from datetime import datetime

def generate_narrative_report(eda_dir, analysis_dir, output_dir):
    try:
        report = [
            f'# Relatório de Análise de Dados\nData: {datetime.now().strftime("%Y-%m-%d")}\n',
            '## Análise Exploratória de Dados (EDA)\n',
            '### Distribuição de Variáveis\n'
        ]
        
        # Adicionar histogramas
        for file in os.listdir(eda_dir):
            if file.startswith('histograma_'):
                var_name = file.replace('histograma_', '').replace('.png', '')
                report.append(f'![Distribuição de {var_name}]({os.path.join(eda_dir, file)})\n')
        
        # Adicionar clusters
        report.extend([
            '\n## Análise Descritiva\n',
            '### Agrupamento de Municípios\n',
            f'![Clusters]({os.path.join(analysis_dir, "clustering_analysis.png")})\n'
        ])
        
        # Salvar relatório
        with open(os.path.join(output_dir, 'relatorio.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        return True
    
    except Exception as e:
        print(f'Erro ao gerar relatório: {str(e)}')
        return False