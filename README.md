# VendasBR Analytics — Análise de Vendas e Business Intelligence

> **portfólio.** A base ficticia de dados foi gerada artificialmente para fins de estudo prático. Não representa uma empresa real nem deve ser usada como evidência de desempenho comercial real.

## Objetivo
Construir um fluxo analítico de ponta a ponta para investigar faturamento, custos, lucro bruto, ticket médio, produtos e desempenho regional, usando Python, SQL, PostgreSQL e Power BI.

## Tecnologias
- Python 3.10+
- pandas, numpy
- PostgreSQL
- SQL
- Power BI Desktop, Power Query e DAX
- Git e GitHub

## Perguntas de negócio
1. Como o faturamento evolui ao longo do tempo?
2. Quais categorias e produtos mais contribuem para receita e lucro bruto?
3. Quais estados têm maior participação nas vendas?
4. Qual é o ticket médio por pedido?
5. Qual é a taxa média de desconto?
6. Existem problemas de qualidade nos dados?

## Estrutura
```text
VendasBR_Analise_dados/
├── dados/
│   ├── brutos/              # CSVs simulados originais
│   └── processados/         # gerados pelo script ETL
├── python/
│   └── etl_vendas.py
├── sql/
│   ├── schema.sql
│   └── consultas_analiticas.sql
├── powerbi/
│   ├── medidas_dax.md
│   └── guia_dashboard.md
├── docs/
│   └── dicionario_dados.md
├── tests/
│   └── test_etl.py
├── requirements.txt
└── README.md
```

## Modelo de dados
O modelo sugerido para Power BI é um **esquema estrela**:
- `fato_vendas`: uma linha por item de pedido.
- `dim_produtos`: atributos de produto e categoria.
- `dim_clientes`: atributos do cliente e localização.
- `dim_calendario`: calendário contínuo para análises de tempo.

> O CSV de vendas inclui UF e cidade para facilitar a primeira exploração. No modelo final, prefira usar a dimensão de clientes como fonte oficial dessas informações.

## Como executar localmente

### 1. Baixe ou clone o repositório
```bash
git clone https://github.com/SEU-USUARIO/VendasBR-Analise_dados.git
cd VendasBR-Analytics
```

### 2. Crie um ambiente virtual
Windows:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```
Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o ETL
```bash
python python/etl_vendas.py
```
O script valida os dados, calcula receita e custo por item e grava arquivos limpos em `dados/processados/`.

### 5. Valide a saída
Confira `dados/processados/relatorio_qualidade.json` e execute:
```bash
pytest
```

## Banco de dados PostgreSQL
1. Crie um banco chamado `vendasbr`.
2. Execute `sql/schema.sql` no banco.
3. Importe os CSVs processados para as tabelas correspondentes. Para um projeto de portfólio, documente se o carregamento foi feito pelo assistente de importação do pgAdmin/DBeaver ou por `COPY`.
4. Rode `sql/consultas_analiticas.sql` e inclua capturas de tela dos resultados no repositório.

Não coloque senhas, tokens ou strings de conexão com credenciais no GitHub.

## Power BI — construção do dashboard
1. Abra o Power BI Desktop.
2. Use **Obter dados > Texto/CSV** e importe os CSVs em `dados/processados/`.
3. No Power Query, confira tipos de dados, nomes de colunas e valores nulos.
4. Crie as relações descritas em `powerbi/guia_dashboard.md`.
5. Crie as medidas de `powerbi/medidas_dax.md`.
6. Monte as páginas e os visuais seguindo o guia.
7. Salve o arquivo `.pbix` em `powerbi/` se o tamanho e as políticas do repositório permitirem; caso contrário, publique imagens do painel e explique como reproduzi-lo.

## Indicadores sugeridos
- Faturamento bruto após desconto
- Custo total dos produtos vendidos
- Lucro bruto estimado
- Margem bruta
- Pedidos distintos
- Unidades vendidas
- Ticket médio
- Desconto médio ponderado por valor bruto

**Definições:** faturamento líquido de descontos = quantidade × preço unitário × (1 − desconto). Lucro bruto estimado = faturamento líquido de descontos − custo unitário × quantidade. Não inclui frete, impostos, despesas operacionais, devoluções ou custo financeiro.

## Limitações
- Dados inteiramente simulados.
- Margem é uma estimativa simplificada e não equivale ao lucro líquido contábil.
- Não há informação de devoluções, impostos, frete, estoque ou despesas operacionais.
- A sazonalidade e a distribuição geográfica foram geradas artificialmente; não tire conclusões sobre o mercado brasileiro real.

## Próximas melhorias
- Criar testes de qualidade mais abrangentes.
- Automatizar o carregamento no PostgreSQL.
- Adicionar tabela calendário e análise YoY/MoM.
- Implementar previsão temporal com validação fora da amostra.
- Publicar uma versão do dashboard com dados anonimizados/simulados.
- Configurar GitHub Actions para executar testes.

## Como apresentar em uma entrevista
Explique o problema de negócio, as decisões tomadas na limpeza, as métricas escolhidas, as limitações dos dados e como cada insight poderia apoiar uma decisão. Diferencie sempre resultados calculados de hipóteses.
