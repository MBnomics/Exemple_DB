from dbnomics import fetch_series
import pandas as pd
import polars as pl 
import streamlit as st 
import plotly.express as px

#téléchargement des données
data = fetch_series("ECB", "SSI", dimensions ={ 
    "FREQ": ["A"],
    "REF_AREA": ["AT", "CY", "GB", "GR"],
    "REF_SECTOR": ["122C"],
    "SSI_INDICATOR": ["H20"],
    "DATA_TYPE": ["X"],
    "COUNT_AREA": ["U6"], 
    "CURRENCY_TRANS": ["Z0Z"],
    "SERIES_DENOM": ["Z"], 
})



#Créer un dataframe avec les données qui nous intéressent 
df = data[["original_period", "value", "Reference area"]]


#Créer la page streamlit 
st.title("Exemple avec Herfindahl")

st.write(df)

fig = px.line(
            df,
            x="original_period",
            y="value",
            color = "Reference area",
            title="Banking Structural Statistical Indicators",
        )


fig.update_layout(
height=650, 
xaxis_title="Years",
yaxis_title="Herfindhal index for total credit)",
)

st.plotly_chart(fig)

