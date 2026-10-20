# Guia de construção do dashboard no Power BI

## Preparação e relacionamentos
1. Execute o ETL e importe `vendas_tratadas.csv`, `dim_produtos.csv` e `dim_clientes.csv`.
2. Renomeie as tabelas para `fato_vendas`, `dim_produtos` e `dim_clientes`.
3. Crie relações 1:*:
   - `dim_produtos[produto_id]` → `fato_vendas[produto_id]`
   - `dim_clientes[cliente_id]` → `fato_vendas[cliente_id]`
   - `dim_calendario[Data]` → `fato_vendas[data_pedido]`
4. Prefira direção de filtro única das dimensões para a fato.
5. Crie as medidas DAX de `medidas_dax.md`.

## Página 1 — Visão geral
- Cartões: Faturamento Líquido, Lucro Bruto Estimado, Margem Bruta %, Pedidos, Ticket Médio.
- Linha: Faturamento por Ano-Mês.
- Colunas: Faturamento por categoria.
- Barras: Top 10 produtos por faturamento.
- Segmentadores: período, UF, categoria e segmento do cliente.

## Página 2 — Produtos e rentabilidade
- Matriz: categoria > produto com faturamento, unidades, lucro estimado e margem.
- Barras: produtos ordenados por lucro bruto estimado.
- Segmentador de categoria.

## Página 3 — Geografia e clientes
- Barras por UF e tabela por cidade.
- Faturamento e pedidos por segmento.
- Use mapa somente se os dados geográficos estiverem corretamente categorizados; para este projeto, barras por UF são mais simples e reproduzíveis.

## Princípios de design
- Fundo claro ou escuro consistente.
- Limite o número de cores; reserve destaque para alertas.
- Títulos que respondam perguntas de negócio.
- Unidades e período sempre explícitos.
- Não use 3D; evite gráficos de pizza com muitas categorias.
- Inclua data de atualização e nota de que os dados são simulados.

## Evidências para o GitHub
Salve imagens nítidas em `powerbi/` ou `docs/`:
- `dashboard_visao_geral.png`
- `dashboard_produtos.png`
- `dashboard_regioes.png`

O arquivo `.pbix` precisa ser criado no Power BI Desktop; este repositório fornece a base, as medidas e o guia, mas não contém um arquivo PBIX pré-construído.
