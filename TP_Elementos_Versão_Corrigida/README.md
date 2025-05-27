# Análise de Dados Municipais (PORDATA)

Projeto desenvolvido no âmbito da disciplina de Elementos de Inteligência Artificial e Ciência de Dados.  
**Autores**: Marco Fernandes Alves, Afonso Pina Claro, Ana Rita Carvalho Beleza Gomes  
**Professor**: João C. Neves  
**Instituição**: Universidade da Beira Interior (2024/25)

## Objetivo
Integrar, analisar e extrair conhecimento de dados estatísticos municipais da [PORDATA](https://www.pordata.pt/), utilizando técnicas de ciência de dados e aprendizagem não supervisionada.

## Estrutura do Projeto

├── data/
│ ├── raw/ # Dados brutos (CSVs da PORDATA)
│ ├── processed/ # Resultados processados
│ ├── data_integrada.csv
│ ├── eda/ # Relatórios e gráficos da análise exploratória
│ ├── analysis/ # Resultados da análise descritiva (clusters, PCA)
│ └── relatorio/ # Relatório narrativo em Markdown
│
├── src/
│ ├── recall.py # Carregamento e pré-processamento de dados
│ ├── integrate.py # Integração de datasets
│ ├── eda.py # Análise exploratória (EDA)
│ ├── limpeza_de_dados.py # Limpeza e tratamento de outliers
│ ├── analise_descritiva.py # Análise com K-means e PCA
│ └── relatorio.py # Geração do relatório narrativo
│
├── main.py # Pipeline principal
│
├── requirements.txt
└── README.md

## Requisitos
- Python
- Bibliotecas:  
  pandas
  numpy
  scipy
  scikit-learn
  matplotlib
  seaborn

## Como Executar

1. **Instale as bibliotecas presentes no ficheiro:**
    - requirements.txt

2. **Coloque os ficherios CSV que deseja analizar na pasta:**
    - data/raw

3. **Execute o ficheiro main.py da seguintes forma:**
    - Abra o CMD e digite:
        - python ../caminho/main.py