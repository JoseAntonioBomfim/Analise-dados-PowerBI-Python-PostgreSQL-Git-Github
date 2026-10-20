"""ETL de vendas para o projeto VendasBR Analytics.

Uso: python python/etl_vendas.py
Os dados são simulados e destinados a fins didáticos.
"""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "dados" / "brutos"
OUT = ROOT / "dados" / "processados"
OUT.mkdir(parents=True, exist_ok=True)

def run_etl():
    vendas = pd.read_csv(RAW / "vendas.csv", sep=";")
    produtos = pd.read_csv(RAW / "produtos.csv")
    clientes = pd.read_csv(RAW / "clientes.csv")

    #print("Colunas carregadas:")
   #for coluna in vendas.columns:
  #          print(repr(coluna))

    linhas_entrada = len(vendas)
    duplicadas = int(vendas.duplicated(subset=["item_id"]).sum())
    vendas = vendas.drop_duplicates(subset=["item_id"]).copy()

    vendas["data_pedido"] = pd.to_datetime(vendas["data_pedido"], format="%d/%m/%Y", errors="coerce")
    numeric_cols = ["quantidade", "preco_unitario", "desconto_pct"]
    for col in numeric_cols:
        vendas[col] = pd.to_numeric(vendas[col], errors="coerce")

    nulos_criticos = int(vendas[["pedido_id", "data_pedido", "cliente_id", "produto_id"]].isna().any(axis=1).sum())
    vendas = vendas.dropna(subset=["pedido_id", "data_pedido", "cliente_id", "produto_id",
                                   "quantidade", "preco_unitario", "desconto_pct"])
    vendas = vendas[(vendas["quantidade"] > 0) & (vendas["preco_unitario"] >= 0)]
    vendas = vendas[vendas["desconto_pct"].between(0, 1)]

    # Enriquecimento com atributos do produto.
    vendas = vendas.merge(produtos, on="produto_id", how="left", validate="many_to_one")
    vendas = vendas.rename(columns={"custo_unitario_y": "custo_unitario"})
    vendas = vendas.merge(clientes[["cliente_id", "segmento"]], on="cliente_id",
                          how="left", validate="many_to_one")

    vendas["receita_bruta"] = vendas["quantidade"] * vendas["preco_unitario"]
    vendas["valor_desconto"] = vendas["receita_bruta"] * vendas["desconto_pct"]
    vendas["receita_liquida"] = vendas["receita_bruta"] - vendas["valor_desconto"]
    vendas["custo_total"] = vendas["quantidade"] * vendas["custo_unitario"]
    vendas["lucro_bruto_estimado"] = vendas["receita_liquida"] - vendas["custo_total"]
    vendas["ano_mes"] = vendas["data_pedido"].dt.to_period("M").astype(str)

    # Rejeita chaves sem correspondência: esses registros exigem investigação.
    sem_produto = int(vendas["produto"].isna().sum())
    sem_segmento = int(vendas["segmento"].isna().sum())

    vendas.to_csv(OUT / "vendas_tratadas.csv", index=False, encoding="utf-8-sig")
    produtos.to_csv(OUT / "dim_produtos.csv", index=False, encoding="utf-8-sig")
    clientes.to_csv(OUT / "dim_clientes.csv", index=False, encoding="utf-8-sig")

    quality = {
        "linhas_entrada": linhas_entrada,
        "linhas_saida": int(len(vendas)),
        "duplicadas_por_item_id_removidas": duplicadas,
        "linhas_com_chaves_ou_data_critica_nula_removidas": nulos_criticos,
        "linhas_sem_correspondencia_produto": sem_produto,
        "linhas_sem_correspondencia_segmento_cliente": sem_segmento,
        "receita_liquida_total": round(float(vendas["receita_liquida"].sum()), 2),
        "lucro_bruto_estimado_total": round(float(vendas["lucro_bruto_estimado"].sum()), 2),
        "observacao": "Dados simulados; lucro bruto estimado não é lucro líquido."
    }
    (OUT / "relatorio_qualidade.json").write_text(
        json.dumps(quality, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(quality, ensure_ascii=False, indent=2))
    return vendas

if __name__ == "__main__":
    run_etl()
