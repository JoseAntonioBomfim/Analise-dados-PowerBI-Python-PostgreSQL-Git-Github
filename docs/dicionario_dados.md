# Dicionário de dados

## `vendas.csv` (dados brutos)
| Coluna | Descrição |
|---|---|
| `item_id` | Identificador único do item de pedido |
| `pedido_id` | Identificador do pedido; pode ter vários itens |
| `data_pedido` | Data do pedido, formato ISO `AAAA-MM-DD` |
| `cliente_id` | Chave do cliente |
| `produto_id` | Chave do produto |
| `quantidade` | Unidades vendidas |
| `preco_unitario` | Preço efetivo unitário antes do desconto |
| `desconto_pct` | Desconto como fração entre 0 e 1 |
| `uf`, `cidade` | Localização associada ao pedido |
| `custo_unitario` | valor de custo unitario por produto |
| `ano_mes` | registro de `AAAA-MM`|

## `produtos.csv`
- `produto_id`: chave primária.
- `produto`: nome do produto.
- `categoria`: categoria comercial.
- `custo_unitario`: custo simulado por unidade.
- `preco_lista`: preço de referência simulado.

## `clientes.csv`
- `cliente_id`: chave primária.
- `cliente`: identificador fictício, sem nome real.
- `cidade`, `uf`: localização simulada.
- `segmento`: grupo comercial simulado.

## Métricas calculadas
- `receita_bruta = quantidade × preco_unitario`.
- `valor_desconto = receita_bruta × desconto_pct`.
- `receita_liquida = receita_bruta − valor_desconto`.
- `custo_total = quantidade × custo_unitario`.
- `lucro_bruto_estimado = receita_liquida − custo_total`.

Essas métricas não incluem impostos, frete, devoluções ou despesas operacionais.
