# DSA — Inflação e Taxa Selic no Brasil

## Integrantes

- Gabriel De Biasi Couto | RM: 563247
- João Pedro da Silva Costa | RM: 565031
- Rodrigo Campos Cordeiro | RM: 566386

## Checkpoint 2 — Modelagem Preditiva

Este checkpoint dá continuidade à Parte 1 usando o **mesmo conjunto de dados**: IPCA (SGS 433) e Selic (SGS 1178), disponibilizados pelo Banco Central do Brasil. O recorte permanece de janeiro de 2020 até 30/08/2026.

### Problema de Machine Learning

O objetivo é prever a **variação do IPCA mensal do mês seguinte** com base no comportamento recente da inflação e da taxa Selic.

- **Tipo de problema:** regressão supervisionada
- **Target:** `target_ipca_proximo_mes`
- **Features principais:** IPCA mensal, IPCA acumulado em 12 meses, Selic média mensal, lags de 1 a 3 meses, médias móveis de 3 meses e componentes sazonais do mês

A tarefa é relevante porque complementa a análise descritiva da Parte 1 com uma visão preditiva de curto prazo. Os modelos não são usados para afirmar causalidade entre Selic e inflação.

### Pré-processamento

1. Coleta do IPCA mensal e da Selic diária.
2. Transformação da Selic em média mensal.
3. Integração das séries pela chave `ano_mes`.
4. Cálculo do IPCA acumulado em 12 meses.
5. Criação de lags de 1, 2 e 3 meses para IPCA e Selic.
6. Criação de médias móveis de 3 meses.
7. Criação de variáveis sazonais (`mes_sin` e `mes_cos`).
8. Criação do target com o IPCA deslocado em um mês para frente.
9. Remoção apenas das linhas com NaN gerados pelas transformações.
10. Separação temporal em 80% treino e 20% teste, sem embaralhamento, para evitar vazamento de informação futura.

### Modelos

Foram implementados três modelos diferentes:

- **Ridge Regression** — modelo do scikit-learn usado como baseline linear.
- **Gradient Boosting Regressor** — conjunto de árvores de decisão melhoradas por boosting.
- **MLP Regressor profunda** — rede neural com três camadas ocultas de 64, 32 e 16 neurônios, ativação ReLU e early stopping.

### Avaliação

Os modelos são comparados com **MAE**, **RMSE** e **R²**. O notebook gera automaticamente a tabela de métricas, as previsões no período de teste, o gráfico de valores reais versus previstos e identifica o modelo com menor RMSE.

### Relação com a Parte 1

Na Parte 1, os indicadores principais foram o **IPCA acumulado em 12 meses**, a **Selic média mensal** e a análise da **defasagem entre inflação e juros**. Esses indicadores descrevem o comportamento histórico do período. No Checkpoint 2, a modelagem tenta estimar o IPCA do mês seguinte usando somente informações disponíveis até o mês atual.

Dessa forma, a Parte 1 oferece a visão descritiva e o Checkpoint 2 acrescenta a visão preditiva. A interpretação continua sendo associativa, e não causal, porque inflação também depende de expectativas, câmbio, atividade econômica, preços administrados e choques externos.

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook notebooks/modelagem_preditiva.ipynb
```

O notebook da Parte 1 continua disponível em `notebooks/analise_economica.ipynb`.

## Estrutura

```text
cp4-dsa/
├── README.md
├── requirements.txt
├── src/
│   └── coleta_dados.py
├── notebooks/
│   ├── analise_economica.ipynb
│   └── modelagem_preditiva.ipynb
└── data/
    └── .gitkeep
```

## Parte 1 — Resumo

A Parte 1 investigou a relação entre inflação (IPCA) e taxa Selic no Brasil. O IPCA mensal foi obtido pela série SGS 433 e a Selic anualizada pela série SGS 1178. Como a Selic é diária, ela foi agregada pela média mensal antes da integração com o IPCA.

Os KPIs analisados foram o IPCA acumulado em 12 meses, a Selic média mensal comparada ao IPCA em 12 meses e a defasagem temporal entre o pico inflacionário e o período de maior aperto monetário.

## Fontes

- Banco Central do Brasil — Sistema Gerenciador de Séries Temporais (SGS)
- Banco Central do Brasil — Portal de Dados Abertos
- IBGE — Índice Nacional de Preços ao Consumidor Amplo (IPCA)
