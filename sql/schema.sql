-- PostgreSQL: execute no banco vendasbr.
-- O modelo usa uma linha por item de pedido na fato_vendas.
CREATE TABLE IF NOT EXISTS produtos (
    produto_id INTEGER PRIMARY KEY,
    produto TEXT NOT NULL,
    categoria TEXT NOT NULL,
    custo_unitario NUMERIC(12,2) NOT NULL,
    preco_lista NUMERIC(12,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS clientes (
    cliente_id INTEGER PRIMARY KEY,
    cliente TEXT NOT NULL,
    cidade TEXT NOT NULL,
    uf CHAR(2) NOT NULL,
    segmento TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS vendas (
    item_id INTEGER PRIMARY KEY,
    pedido_id TEXT NOT NULL,
    data_pedido DATE NOT NULL,
    cliente_id INTEGER NOT NULL REFERENCES clientes(cliente_id),
    produto_id INTEGER NOT NULL REFERENCES produtos(produto_id),
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario NUMERIC(12,2) NOT NULL CHECK (preco_unitario >= 0),
    desconto_pct NUMERIC(5,4) NOT NULL CHECK (desconto_pct BETWEEN 0 AND 1),
    custo_unitario NUMERIC(12,2) NOT NULL CHECK (custo_unitario >= 0),
    ano_mes DATE
);

CREATE INDEX IF NOT EXISTS idx_fato_vendas_data ON vendas(data_pedido);
CREATE INDEX IF NOT EXISTS idx_fato_vendas_cliente ON vendas(cliente_id);
CREATE INDEX IF NOT EXISTS idx_fato_vendas_produto ON vendas(produto_id);
