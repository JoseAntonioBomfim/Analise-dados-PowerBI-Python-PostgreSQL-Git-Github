-- 1. Indicadores gerais
SELECT
    ROUND(SUM(receita_liquida), 2) AS faturamento_liquido,
    ROUND(SUM(custo_total), 2) AS custo_total,
    ROUND(SUM(lucro_bruto_estimado), 2) AS lucro_bruto_estimado,
    ROUND(100.0 * SUM(lucro_bruto_estimado) / NULLIF(SUM(receita_liquida), 0), 2) AS margem_bruta_pct,
    COUNT(DISTINCT pedido_id) AS pedidos,
    ROUND(SUM(receita_liquida) / NULLIF(COUNT(DISTINCT pedido_id), 0), 2) AS ticket_medio
FROM fato_vendas;

-- 2. Evolução mensal
SELECT
    DATE_TRUNC('month', data_pedido)::date AS mes,
    ROUND(SUM(receita_liquida), 2) AS faturamento,
    ROUND(SUM(lucro_bruto_estimado), 2) AS lucro_bruto_estimado,
    COUNT(DISTINCT pedido_id) AS pedidos
FROM fato_vendas
GROUP BY 1
ORDER BY 1;

-- 3. Desempenho por categoria e produto
SELECT p.categoria, p.produto,
       SUM(f.quantidade) AS unidades,
       ROUND(SUM(f.receita_liquida), 2) AS faturamento,
       ROUND(SUM(f.lucro_bruto_estimado), 2) AS lucro_bruto_estimado
FROM fato_vendas f
JOIN dim_produtos p USING (produto_id)
GROUP BY p.categoria, p.produto
ORDER BY faturamento DESC;

-- 4. Vendas por estado
SELECT c.uf,
       ROUND(SUM(f.receita_liquida), 2) AS faturamento,
       COUNT(DISTINCT f.pedido_id) AS pedidos,
       ROUND(SUM(f.receita_liquida) / NULLIF(COUNT(DISTINCT f.pedido_id), 0), 2) AS ticket_medio
FROM fato_vendas f
JOIN dim_clientes c USING (cliente_id)
GROUP BY c.uf
ORDER BY faturamento DESC;

-- 5. Desconto médio ponderado pelo valor bruto
SELECT ROUND(100.0 * SUM(valor_desconto) / NULLIF(SUM(receita_bruta), 0), 2)
       AS desconto_ponderado_pct
FROM fato_vendas;

-- 6. Clientes por segmento
SELECT c.segmento,
       COUNT(DISTINCT c.cliente_id) AS clientes,
       ROUND(SUM(f.receita_liquida), 2) AS faturamento
FROM fato_vendas f
JOIN dim_clientes c USING (cliente_id)
GROUP BY c.segmento
ORDER BY faturamento DESC;


SELECT
ROUND(SUM(preco_unitario * quantidade), 2) AS venda_bruta,
ROUND(SUM(custo_unitario * quantidade), 2) AS custo_bruto

FROM vendas