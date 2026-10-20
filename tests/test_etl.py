from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "python"))
from etl_vendas import run_etl

def test_etl_produz_valores_validos():
    df = run_etl()
    assert not df.empty
    assert df["item_id"].is_unique
    assert (df["quantidade"] > 0).all()
    assert df["desconto_pct"].between(0, 1).all()
    assert (df["receita_liquida"] >= 0).all()
    assert "lucro_bruto_estimado" in df.columns
