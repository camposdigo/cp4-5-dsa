# Checkpoint 1 — DSA | Inflação e Taxa Selic no Brasil

## Integrantes

- Gabriel De Biasi Couto | RM: 563247
- João Pedro da Silva Costa | RM: 565031
- Rodrigo Campos Cordeiro | RM: 566386

## Definição do problema, obtenção dos dados e construção dos indicadores

**Tema:** Economia  
**Recorte:** Relação entre inflação (IPCA) e taxa básica de juros (Selic) no Brasil, de janeiro de 2020 até o dado mais recente disponível.  
**Data de acesso às fontes:** 30/08/2026

## 1. Problema investigado

A inflação reduz o poder de compra da população e influencia decisões de consumo, investimento e política econômica. Um dos principais instrumentos utilizados para controlar a inflação é a taxa básica de juros.

Este trabalho investiga a evolução recente do IPCA e da taxa Selic e busca verificar como os juros se comportaram diante das mudanças da inflação brasileira.

## 2. Fontes de dados

Os dados utilizados são reais, públicos e estruturados, disponibilizados pelo Banco Central do Brasil por meio do Sistema Gerenciador de Séries Temporais (SGS).

### IPCA — série SGS 433

- Indicador: Índice Nacional de Preços ao Consumidor Amplo (IPCA)
- Unidade: variação percentual mensal
- Periodicidade: mensal
- Fonte original do indicador: IBGE
- Consulta oficial: https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarSeries&series=433
- API utilizada: https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados

### Taxa Selic — série SGS 1178

- Indicador: taxa de juros Selic anualizada, base 252 dias úteis
- Unidade: percentual ao ano
- Periodicidade: diária
- Fonte: Banco Central do Brasil
- Portal oficial: https://dadosabertos.bcb.gov.br/dataset/1178-taxa-de-juros---selic-anualizada-base-252
- API utilizada: https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados

### Integração das fontes

Como o IPCA é mensal e a Selic é diária, a série da Selic é transformada em uma média mensal. Em seguida, os conjuntos são integrados pela chave `ano_mes`. Dessa forma, cada mês possui a inflação observada e a taxa média de juros correspondente.

## 3. Principais variáveis

| Variável | Descrição | Unidade |
|---|---|---|
| `data` | Data de referência | data |
| `ipca_mensal` | Variação mensal do IPCA | % ao mês |
| `selic_anual` | Taxa Selic observada | % ao ano |
| `selic_media_mensal` | Média das observações diárias da Selic no mês | % ao ano |
| `ipca_12m` | Inflação acumulada em 12 meses | % |
| `ano_mes` | Chave utilizada para integrar as séries | AAAA-MM |

## 4. Perguntas de análise

### Pergunta 1 — Como a inflação brasileira evoluiu desde 2020?

**KPI:** IPCA acumulado em 12 meses.

**Justificativa:** a variação de 12 meses reduz o efeito de oscilações isoladas e permite acompanhar a tendência inflacionária de forma mais adequada do que observar somente um mês.

### Pergunta 2 — Como a taxa Selic reagiu aos períodos de maior inflação?

**KPI:** Selic média mensal (% a.a.) comparada ao IPCA acumulado em 12 meses.

**Justificativa:** a comparação temporal permite visualizar os ciclos de aperto e flexibilização monetária e verificar se períodos de inflação mais elevada foram acompanhados por juros maiores.

### Pergunta 3 — Qual foi a intensidade da relação entre inflação e juros no período?

**KPI:** correlação de Pearson entre IPCA acumulado em 12 meses e Selic média mensal.

**Justificativa:** a correlação resume numericamente a associação linear entre as duas variáveis. Ela não demonstra causalidade, mas ajuda a identificar se elas tenderam a se movimentar na mesma direção no recorte analisado.

## 5. Análise exploratória

O notebook `notebooks/analise_economica.ipynb` executa automaticamente:

- coleta dos dados oficiais via API;
- conversão e validação das datas;
- verificação de valores ausentes e duplicados;
- estatísticas descritivas;
- transformação da Selic diária em média mensal;
- integração das duas fontes;
- cálculo do IPCA acumulado em 12 meses;
- cálculo dos KPIs;
- identificação de máximos e mínimos;
- gráficos de evolução temporal;
- análise da relação entre inflação e juros.

## 6. O que os dados permitem revelar?

A análise permite identificar períodos de aceleração e desaceleração da inflação, observar os movimentos da taxa básica de juros e comparar os dois ciclos. O resultado quantitativo é produzido diretamente a partir dos dados oficiais no notebook, evitando conclusões baseadas apenas em percepção.

## 7. Quais indicadores representam melhor o problema?

Os três indicadores principais são:

1. **IPCA acumulado em 12 meses**, para medir a intensidade da inflação;
2. **Selic média mensal**, para representar a postura dos juros ao longo do tempo;
3. **Correlação IPCA × Selic**, para resumir a associação entre os ciclos das duas variáveis.

## 8. Como os indicadores apoiam a tomada de decisão?

Esses indicadores ajudam famílias, empresas, investidores e formuladores de políticas a compreender o ambiente econômico. Inflação e juros influenciam poder de compra, custo do crédito, financiamento, investimentos e decisões empresariais. O acompanhamento conjunto permite avaliar se a economia está em um cenário de maior ou menor pressão inflacionária e monetária.

> **Observação:** correlação não implica causalidade. A taxa de juros afeta a economia com defasagens e também responde a expectativas de inflação, atividade econômica e outros fatores.

## Como executar

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analise_economica.ipynb
```

Também é possível executar a coleta e gerar a base integrada:

```bash
python src/coleta_dados.py
```

## Estrutura

```text
cp4-dsa/
├── README.md
├── requirements.txt
├── src/
│   └── coleta_dados.py
├── notebooks/
│   └── analise_economica.ipynb
└── data/
    └── .gitkeep
```

## Referências

- Banco Central do Brasil — Sistema Gerenciador de Séries Temporais (SGS).
- Banco Central do Brasil — Portal de Dados Abertos.
- IBGE — Índice Nacional de Preços ao Consumidor Amplo (IPCA).