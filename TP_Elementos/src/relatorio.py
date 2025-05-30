import os
from datetime import datetime

def generate_narrative_report(eda_dir, analysis_dir, output_dir):
    try:
        report = [
            f'# Relatório Econômico de Portugal\nData: {datetime.now().strftime("%Y-%m-%d")}\n',
            '## Análise Exploratória de Dados\n'
        ]
        
        # Adicionar estatísticas descritivas
        eda_report_path = os.path.join(eda_dir, 'eda_report.md')
        if os.path.exists(eda_report_path):
            with open(eda_report_path, 'r', encoding='utf-8') as f:
                report.append(f.read())
        
        # Adicionar análise econômica
        report.append('\n## Análise Econômica Nacional\n')
        
        # Listar todos os gráficos de evolução
        evolution_plots = [f for f in os.listdir(analysis_dir) if f.endswith('_evolution.png')]
        for plot in evolution_plots:
            var_name = plot.replace('_evolution.png', '')
            report.append(f'### Evolução de {var_name}\n')
            report.append(f'![Evolução de {var_name}]({os.path.join(analysis_dir, plot)})\n')
            
            # Adicionar gráfico de crescimento correspondente
            growth_plot = plot.replace('_evolution.png', '_growth.png')
            if os.path.exists(os.path.join(analysis_dir, growth_plot)):
                report.append(f'### Taxa de Crescimento de {var_name}\n')
                report.append(f'![Crescimento de {var_name}]({os.path.join(analysis_dir, growth_plot)})\n')
        
        # Adicionar relação entre variáveis
        relationship_plot = os.path.join(analysis_dir, 'economic_relationship.png')
        if os.path.exists(relationship_plot):
            report.append('### Relação entre Variáveis Econômicas\n')
            report.append(f'![Relação Econômica]({relationship_plot})\n')
        
        # Conclusões
        report.append('\n## Conclusões\n')
        report.append('- A economia portuguesa mostrou diferentes fases de crescimento ao longo das décadas\n')
        report.append('- Os indicadores econômicos analisados apresentam tendências claras de evolução\n')
        report.append('- Períodos de recessão são identificáveis pelas taxas de crescimento negativas\n')
        
        # Salvar relatório
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, 'relatorio_economico.md'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        
        return True
    
    except Exception as e:
        print(f'Erro ao gerar relatório: {str(e)}')
        return False