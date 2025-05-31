import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def ranking_ensino(df):
    """
    Analisa e retorna os rankings de municípios
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['Estabelecimentos_de_ensino'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'Estabelecimentos_de_ensino')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'Estabelecimentos_de_ensino')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['Estabelecimentos_de_ensino'].to_dict(),
        'bottom10': bottom10.set_index('Território')['Estabelecimentos_de_ensino'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['Estabelecimentos_de_ensino'].mean()
    }
    print(f"\n TOP 10 Municípios com mais Estabelecimentos de Ensino em {ultimo_ano}:")
    print(top10[['Território', 'Estabelecimentos_de_ensino']].to_string(index=False))

    print(f"\n BOTTOM 10 Municípios com menos Estabelecimentos de Ensino em {ultimo_ano}:")
    print(bottom10[['Território', 'Estabelecimentos_de_ensino']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de estabelecimentos por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])

        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='Estabelecimentos_de_ensino', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em termos de estabelecimentos de ensino ({ultimo_ano})')
        plt.xlabel('Número de estabelecimentos de ensino')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()

    return resultados

def ranking_desemprego(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['População_desempregada_por_nivel_de_escolaridade'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'População_desempregada_por_nivel_de_escolaridade')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'População_desempregada_por_nivel_de_escolaridade')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['População_desempregada_por_nivel_de_escolaridade'].to_dict(),
        'bottom10': bottom10.set_index('Território')['População_desempregada_por_nivel_de_escolaridade'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['População_desempregada_por_nivel_de_escolaridade'].mean()
    }
    print(f"\n TOP 10 Municípios com mais desempregados em {ultimo_ano}:")
    print(top10[['Território', 'População_desempregada_por_nivel_de_escolaridade']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com menos desempregados em {ultimo_ano}:")
    print(bottom10[['Território', 'População_desempregada_por_nivel_de_escolaridade']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de desemprego por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='População_desempregada_por_nivel_de_escolaridade', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em desemprego por nivel de escolaridade ({ultimo_ano})')
        plt.xlabel('Número de desempregados')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados

def ranking_empregados(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['População_empregada'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'População_empregada')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'População_empregada')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['População_empregada'].to_dict(),
        'bottom10': bottom10.set_index('Território')['População_empregada'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['População_empregada'].mean()
    }
    print(f"\n TOP 10 Municípios com uma maior População Empregada em {ultimo_ano}:")
    print(top10[['Território', 'População_empregada']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com uma menor População Empregada em {ultimo_ano}:")
    print(bottom10[['Território', 'População_empregada']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de empregados por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='População_empregada', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em termos de população empregada ({ultimo_ano})')
        plt.xlabel('Número de populares empregados')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados

def ranking_desistentes(df):
    """
    Analisa e retorna os rankings de municípios:
    """
    ultimo_ano = df['Ano'].max()
    dados_ultimo_ano = df[df['Ano'] == ultimo_ano].copy()
    dados_ultimo_ano = dados_ultimo_ano.drop_duplicates(subset='Território')
    dados_ultimo_ano = dados_ultimo_ano[dados_ultimo_ano['Taxa_de_retencao'] > 0]
    if len(dados_ultimo_ano) < 10:
        print("\n Não há municípios suficientes para rankings completos.")
        return None
    top10 = dados_ultimo_ano.nlargest(10, 'Taxa_de_retencao')
    bottom10 = dados_ultimo_ano.nsmallest(10, 'Taxa_de_retencao')
    resultados = {
        'ano': ultimo_ano,
        'top10': top10.set_index('Território')['Taxa_de_retencao'].to_dict(),
        'bottom10': bottom10.set_index('Território')['Taxa_de_retencao'].to_dict(),
        'total_municipios': len(dados_ultimo_ano),
        'media_nacional': dados_ultimo_ano['Taxa_de_retencao'].mean()
    }
    print(f"\n TOP 10 Municípios com uma maior taxa de retenção em {ultimo_ano}:")
    print(top10[['Território', 'Taxa_de_retencaoa']].to_string(index=False))
    print(f"\n BOTTOM 10 Municípios com uma menor taxa de retenção em {ultimo_ano}:")
    print(bottom10[['Território', 'Taxa_de_retencao']].to_string(index=False))

    print(f"\n Estatísticas Nacionais em {ultimo_ano}:")
    print(f"- Total de municípios: {resultados['total_municipios']}")
    print(f"- Média de caixas por município: {resultados['media_nacional']:.1f}")
    if not top10.empty and not bottom10.empty:
        top10['Tipo'] = 'Top 10'
        bottom10['Tipo'] = 'Bottom 10'
        combined = pd.concat([top10, bottom10])
        plt.figure(figsize=(12, 8))
        sns.barplot(data=combined, x='Taxa_de_retencao', y='Território', hue='Tipo',
                    palette={'Top 10': 'green', 'Bottom 10': 'red'})
        plt.title(f'Comparação: Top 10 vs Bottom 10 Municípios em desistentes ({ultimo_ano})')
        plt.xlabel('Número de desistentes')
        plt.ylabel('Município')
        plt.tight_layout()
        plt.show()
    return resultados
