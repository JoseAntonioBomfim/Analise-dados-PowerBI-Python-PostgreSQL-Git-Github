# Medidas DAX

> Ajuste os nomes das tabelas/colunas conforme o modelo criado no Power BI. Formate as medidas monetárias como moeda (R$).

```DAX
Faturamento Líquido =
SUM ( fato_vendas[receita_liquida] )

Custo Total =
SUM ( fato_vendas[custo_total] )

Lucro Bruto Estimado =
SUM ( fato_vendas[lucro_bruto_estimado] )

Margem Bruta % =
DIVIDE ( [Lucro Bruto Estimado], [Faturamento Líquido] )

Pedidos =
DISTINCTCOUNT ( fato_vendas[pedido_id] )

Unidades Vendidas =
SUM ( fato_vendas[quantidade] )

Ticket Médio =
DIVIDE ( [Faturamento Líquido], [Pedidos] )

Valor de Desconto =
SUM ( fato_vendas[valor_desconto] )

Desconto Ponderado % =
DIVIDE ( [Valor de Desconto], SUM ( fato_vendas[receita_bruta] ) )

Faturamento Mês Anterior =
CALCULATE (
    [Faturamento Líquido],
    DATEADD ( dim_calendario[Data], -1, MONTH )
)

Variação Mensal % =
DIVIDE (
    [Faturamento Líquido] - [Faturamento Mês Anterior],
    [Faturamento Mês Anterior]
)
```

## Calendário
Crie uma tabela de datas contínua e marque-a como tabela de datas:

```DAX
dim_calendario =
ADDCOLUMNS (
    CALENDAR ( MIN ( fato_vendas[data_pedido] ), MAX ( fato_vendas[data_pedido] ) ),
    "Ano", YEAR ( [Date] ),
    "Mês Número", MONTH ( [Date] ),
    "Mês", FORMAT ( [Date], "mmmm" ),
    "Ano-Mês", FORMAT ( [Date], "yyyy-MM" )
)
```

Renomeie `[Date]` para `Data` se preferir e relacione `dim_calendario[Data]` a `fato_vendas[data_pedido]` (1:*). Classifique o nome do mês por `Mês Número`. Em modelos com múltiplos anos, use `Ano-Mês` no eixo para manter a ordem cronológica.

**Atenção:** `DATEADD` exige uma tabela calendário adequada, com relação ativa e datas contínuas. Confirme a sintaxe de separadores conforme a configuração regional do Power BI.
