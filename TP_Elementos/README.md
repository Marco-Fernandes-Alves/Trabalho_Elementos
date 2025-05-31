# Análise de Dados Municipais (PORDATA)

Projeto desenvolvido no âmbito da disciplina de Elementos de Inteligência Artificial e Ciência de Dados.  

**Autores**: Marco Fernandes Alves, Afonso Pina Claro, Ana Rita Carvalho Beleza Gomes  
**Professor**: João C. Neves  
**Instituição**: Universidade da Beira Interior (2024/25)

## Objetivo

Este projeto realiza uma análise econômica de Portugal utilizando dados da Pordata, focando em indicadores como PIB e PIB per capita.

## Estrutura do Projeto

TP_Elementos/
├── data/
│   └── raw/                    # Dados brutos da Pordata
│       ├── PIB.csv
│       └── PIB_per_capita.csv
├── src/
│   ├── recall.py               # Carregamento dos dados
│   ├── integrate.py            # Integração dos datasets
│   ├── eda.py                  # Análise exploratória de dados
│   ├── limpeza_de_dados.py     # Limpeza de dados
│   ├── analise_descritiva.py   # Análise econômica
│   ├── relatorio.py            # Geração de relatório
│   └── main.py                 # Script principal
├── requirements.txt
└── README.md

## Requisitos
- Python
- Bibliotecas:  
    pandas
    scikit-learn
    matplotlib
    seaborn
    scipy
    openpyxl

## Como Executar

1. **Instale as bibliotecas presentes no ficheiro:**
    - bibliotecas.txt

2. **Execute o ficheiro main.py da seguintes forma:**
    - Abra o CMD e digite:
        - python ../caminho/main.py

3. **Reexecução caso desejado**
    - Em caso de desejar voltar a executar o programa, basta apagar a pasta processed/ dentro da pasta data/
    - Não apagar a pasta leva à substituição dos ficherios nela presentes caso os ficheiros analizados sejam os mesmos.