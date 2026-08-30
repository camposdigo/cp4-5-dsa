from pathlib import Path
import requests
import pandas as pd

BASE_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"
DATA_INICIAL = "01/01/2020"
DATA_FINAL = "30/08/2026"


def buscar_serie(codigo, data_inicial=DATA_INICIAL, data_final=DATA_FINAL):
    params = {
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final,
    }
    resposta = requests.get(BASE_URL.format(codigo=codigo), params=params, timeout=30)
    resposta.raise_for_status()
    dados = pd.DataFrame(resposta.json())
    dados["data"] = pd.to_datetime(dados["data"], format="%d/%m/%Y")
    dados["valor"] = pd.to_numeric(dados["valor"], errors="coerce")
    return dados.dropna().drop_duplicates().sort_values("data")


def preparar_base():
    ipca = buscar_serie(433).rename(columns={"valor": "ipca_mensal"})
    selic = buscar_serie(1178).rename(columns={"valor": "selic_anual"})

    ipca["ano_mes"] = ipca["data"].dt.to_period("M")
    selic["ano_mes"] = selic["data"].dt.to_period("M")

    selic_mensal = (
        selic.groupby("ano_mes", as_index=False)["selic_anual"]
        .mean()
        .rename(columns={"selic_anual": "selic_media_mensal"})
    )

    base = ipca[["data", "ano_mes", "ipca_mensal"]].merge(
        selic_mensal, on="ano_mes", how="inner"
    )

    base["ipca_12m"] = (
        (1 + base["ipca_mensal"] / 100)
        .rolling(12)
        .apply(lambda valores: valores.prod(), raw=True)
        .sub(1)
        .mul(100)
    )

    return ipca, selic, base


def main():
    _, _, base = preparar_base()
    destino = Path(__file__).resolve().parents[1] / "data"
    destino.mkdir(exist_ok=True)
    arquivo = destino / "economia_ipca_selic.csv"
    base.to_csv(arquivo, index=False)

    validos = base.dropna(subset=["ipca_12m"])
    correlacao = validos["ipca_12m"].corr(validos["selic_media_mensal"])

    print(f"Base salva em: {arquivo}")
    print(f"Observações integradas: {len(base)}")
    print(f"Correlação IPCA 12m x Selic: {correlacao:.3f}")


if __name__ == "__main__":
    main()
