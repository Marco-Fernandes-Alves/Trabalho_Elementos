import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def ranking_caixa(df):
    """
    Analisa e retorna os rankings de municípios
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['caixas_automaticas_multibanco'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'caixas_automaticas_multibanco')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'caixas_automaticas_multibanco')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['caixas_automaticas_multibanco'].to_dict(),
        'bottom10': bottom10.set_index('Território')['caixas_automaticas_multibanco'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['caixas_automaticas_multibanco'].mean()
    }
    print(f"\n TOP 10 Municípios com mais Caixas Multibanco em {ultimo_ano}:")
    print(top10[['Território', 'caixas_automaticas_multibanco']].to_string(index=False))

    print(f"\n BOTTOM 10 Municípios com menos Caixas Multibanco em {ultimo_ano}:")
    print(bottom10[['Território', 'caixas_automaticas_multibanco']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de caixas por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])

        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='caixas_automaticas_multibanco', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em Caixas Multibanco ({ultimo_ano})')
        plt.xlabel('Número de Caixas Multibanco')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()

    return resultados

def ranking_estrangeiro(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade'].to_dict(),
        'bottom10': bottom10.set_index('Território')['populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade'].mean()
    }
    print(f"\n TOP 10 Municípios com mais Estrangeiros Legais em {ultimo_ano}:")
    print(top10[['Território', 'populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com menos Estrangeiros Legais em {ultimo_ano}:")
    print(bottom10[['Território', 'populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de caixas por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='populacao_estrangeira_com_estatuto_legal_de_residente_por_nacionalidade', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em Estrangeiros ({ultimo_ano})')
        plt.xlabel('Número de Estrangeiros')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados

def ranking_postes(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['postos_telefonicos_analogicos_principais_por_tipo'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'postos_telefonicos_analogicos_principais_por_tipo')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'postos_telefonicos_analogicos_principais_por_tipo')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['postos_telefonicos_analogicos_principais_por_tipo'].to_dict(),
        'bottom10': bottom10.set_index('Território')['postos_telefonicos_analogicos_principais_por_tipo'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['postos_telefonicos_analogicos_principais_por_tipo'].mean()
    }
    print(f"\n TOP 10 Municípios com mais Postes Telefonicos Analogicos em {ultimo_ano}:")
    print(top10[['Território', 'postos_telefonicos_analogicos_principais_por_tipo']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com Postes Telefonicos Analogicos em {ultimo_ano}:")
    print(bottom10[['Território', 'postos_telefonicos_analogicos_principais_por_tipo']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de caixas por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='postos_telefonicos_analogicos_principais_por_tipo', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em Postes Telefonicos ({ultimo_ano})')
        plt.xlabel('Número de Postes Telefonicos')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados

def ranking_azeitonas(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['producao_azeitona'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'producao_azeitona')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'producao_azeitona')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['producao_azeitona'].to_dict(),
        'bottom10': bottom10.set_index('Território')['producao_azeitona'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['producao_azeitona'].mean()
    }
    print(f"\n TOP 10 Municípios com uma maior Produção de Azeitona em {ultimo_ano}:")
    print(top10[['Território', 'producao_azeitona']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com uma menor Produção de Azeitona em {ultimo_ano}:")
    print(bottom10[['Território', 'producao_azeitona']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de caixas por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='producao_azeitona', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em Produção de Azeitona ({ultimo_ano})')
        plt.xlabel('Número de Produtores de Azeitona')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados
def ranking_abstencao(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais'].to_dict(),
        'bottom10': bottom10.set_index('Território')['taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais'].mean()
    }
    print(f"\n TOP 10 Municípios com uma maior taixa de abstenção durante as eleições em {ultimo_ano}:")
    print(top10[['Território', 'taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com uma menor taixa de abstenção durante as eleições em {ultimo_ano}:")
    print(bottom10[['Território', 'taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de caixas por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='taxa_de_abstecao_nas_eleicoes_para_as_camaras_municipais', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em Taxa de Abstenção para as câmaras municipais ({ultimo_ano})')
        plt.xlabel('Número de Abstinentes')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados

