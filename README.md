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

Os dados utilizados são reais, públicos e estruturados, disponibilizados pelo Banco Central do Brasil por meio do Sistema Gerenciador de Séries Temporais (SGS). O IPCA é originalmente produzido pelo IBGE.

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

## 4. Perguntas de análise e KPIs

### Pergunta 1 — Como a inflação brasileira evoluiu desde 2020?

**KPI:** IPCA acumulado em 12 meses.

**Justificativa:** a variação de 12 meses reduz o efeito de oscilações isoladas e permite acompanhar a tendência inflacionária de forma mais adequada do que observar somente um mês.

### Pergunta 2 — Como a taxa Selic reagiu aos períodos de maior inflação?

**KPI:** Selic média mensal (% a.a.) comparada ao IPCA acumulado em 12 meses.

**Justificativa:** a comparação temporal permite visualizar os ciclos de aperto e flexibilização monetária e verificar se períodos de inflação mais elevada foram acompanhados por juros maiores.

### Pergunta 3 — Existe uma defasagem entre o aumento da inflação e a reação dos juros?

**KPI:** diferença temporal entre o pico do IPCA acumulado em 12 meses e o momento em que a Selic atingiu o patamar de 13,75% a.a. em 2022.

**Justificativa:** a política monetária não reage de forma instantânea e também produz efeitos com defasagem. Medir a distância entre os momentos de maior inflação e de maior aperto monetário ajuda a interpretar melhor a dinâmica econômica.

## 5. Análise exploratória e resultados

A análise dos dados mostra um ciclo econômico bastante claro no período estudado.

### Resultado 1 — Pico da inflação

Em abril de 2022, o IPCA acumulado em 12 meses atingiu **12,13%**, um dos pontos mais elevados do recorte analisado. No mesmo mês, o IPCA mensal foi de **1,06%**. Em março de 2022, a inflação mensal havia sido ainda maior, chegando a **1,62%**.

Esses números mostram a forte aceleração inflacionária observada principalmente entre 2021 e o primeiro semestre de 2022.

### Resultado 2 — Reação da taxa Selic

O Banco Central respondeu ao ambiente inflacionário com um ciclo de elevação dos juros. Em **agosto de 2022**, o Copom elevou a meta da Selic para **13,75% ao ano**.

A comparação temporal mostra que o período de inflação elevada foi acompanhado por forte aperto monetário. A Selic permaneceu em patamar elevado mesmo depois do início da desaceleração do IPCA, evidenciando que a política monetária atua com defasagem.

### Resultado 3 — Defasagem entre inflação e juros

O pico de **12,13% do IPCA em 12 meses ocorreu em abril de 2022**, enquanto a Selic chegou a **13,75% a.a. em agosto de 2022**.

Assim, o indicador de defasagem entre esses dois marcos foi de aproximadamente **4 meses**.

Esse resultado não significa que a Selic de agosto tenha sido causada exclusivamente pelo IPCA de abril. As decisões do Copom também consideram expectativas futuras de inflação, atividade econômica, cenário internacional e outros riscos. Entretanto, o indicador ajuda a visualizar que a resposta monetária e seus efeitos não são instantâneos.

### Situação mais recente disponível na análise

Em **junho de 2026**, o IPCA foi de **0,16% no mês**, acumulando **3,36% no ano** e **4,64% nos últimos 12 meses**. Isso representa uma redução expressiva em relação aos 12,13% registrados em abril de 2022.

A série diária de juros, por sua vez, continuava indicando juros elevados em 2026. Dessa forma, o cenário recente combina inflação significativamente menor que a observada no pico de 2022 com uma política monetária ainda restritiva.

## 6. Síntese dos indicadores

| Indicador | Resultado observado | Interpretação |
|---|---:|---|
| Pico do IPCA em 12 meses | **12,13% — abr/2022** | Período de maior pressão inflacionária identificado |
| IPCA mensal em abr/2022 | **1,06%** | Forte alta de preços no mês |
| Selic após o ciclo de alta de 2022 | **13,75% a.a. — ago/2022** | Forte aperto da política monetária |
| Defasagem entre os marcos | **aprox. 4 meses** | A reação monetária não ocorre de forma instantânea |
| IPCA em 12 meses em jun/2026 | **4,64%** | Inflação muito abaixo do pico de 2022 |
| IPCA acumulado em 2026 até junho | **3,36%** | Pressão inflacionária acumulada no ano |

## 7. O que os dados revelam sobre a situação atual?

Os dados revelam que o Brasil passou por uma forte aceleração inflacionária entre 2021 e 2022. O IPCA acumulado em 12 meses atingiu 12,13% em abril de 2022 e foi seguido por um período de juros elevados.

Posteriormente ocorreu um processo de desinflação. Em junho de 2026, o IPCA acumulado em 12 meses estava em 4,64%, diferença de **7,49 pontos percentuais** em relação ao pico de abril de 2022.

A análise conjunta reforça a importância de não observar inflação ou juros isoladamente: os dois indicadores fazem parte de um mesmo ambiente macroeconômico, embora a relação entre eles não seja imediata nem exclusivamente causal.

## 8. Quais indicadores representam melhor o problema?

Os indicadores que melhor representam o problema são o **IPCA acumulado em 12 meses**, por mostrar a tendência da inflação; a **taxa Selic**, por representar a postura da política monetária; e a **defasagem temporal entre os movimentos dos indicadores**, que ajuda a interpretar a resposta dos juros às pressões inflacionárias.

## 9. Como os indicadores apoiam a tomada de decisão?

Para famílias, a inflação ajuda a avaliar a perda de poder de compra, enquanto a Selic influencia financiamentos, empréstimos e investimentos. Para empresas, os indicadores ajudam no planejamento de custos, preços e decisões de investimento. Para investidores, inflação e juros são fundamentais na comparação entre classes de ativos. Para formuladores de políticas públicas, os indicadores ajudam a acompanhar a estabilidade de preços e os efeitos das decisões de política monetária.

> **Observação:** associação temporal não implica causalidade. A Selic responde principalmente às perspectivas para a inflação futura e seus efeitos sobre a economia também acontecem com defasagem.

## 10. Notebook e reprodutibilidade

O notebook `notebooks/analise_economica.ipynb` contém o código para coleta, tratamento, integração e visualização das séries. Ele permite atualizar a análise quando novos dados forem divulgados.

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analise_economica.ipynb
```

Também é possível gerar a base integrada executando:

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
- Banco Central do Brasil — Comitê de Política Monetária (Copom).
- Banco Central do Brasil — Portal de Dados Abertos.
- IBGE — Índice Nacional de Preços ao Consumidor Amplo (IPCA).