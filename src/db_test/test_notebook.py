# %%
# vous devez installer pip et ipykernel avec le terminal
import plotly.express as px
from dbnomics import fetch_series

# %%
"""Télécharger les données 
lien des données : db.nomics.world/ECD/SSI
"""
data = fetch_series(
    "ECB",
    "SSI",
    dimensions={
        "FREQ": ["A"],
        "REF_AREA": ["AT", "CY", "GB", "GR"],
        "REF_SECTOR": ["122C"],
        "SSI_INDICATOR": ["H20"],
        "DATA_TYPE": ["X"],
        "COUNT_AREA": ["U6"],
        "CURRENCY_TRANS": ["Z0Z"],
        "SERIES_DENOM": ["Z"],
    },
)

# %%
"""Faire un nouveau dataframe avec les colonnes qui nous intéressent 
Grâce au notebook vous pouvez facilement visualer les données sans avoir à passer par debug
cliquer sur view data
très pratique quand on manipule des données 
"""
df = data[["original_period", "value", "Reference area"]]

# %%
# Plot les données : là je vais faire le truc le plus basique -> regardez la documentation
fig = px.line(
    df,
    x="original_period",
    y="value",
    color="Reference area",
    title="Banking Structural Statistical Indicators",
)


fig.update_layout(
    height=650,
    xaxis_title="Years",
    yaxis_title="Herfindhal index for total credit)",
)

fig.show()

# %%
