import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
st.title('Courbe des Taux Nominaux à 10 ans US bonds')
st.write("""Cette courbe affiche la courbe des taux nominaux des obligations du trésor américains à 10 ans.
    Les données sont disponibles sur DBnomics, pour une période allant de 1963 à 2024 (Source : FED).""")
url = "https://api.db.nomics.world/v22/series/FED/H15/RIFLGFCY10_N.B?observations=1"
st.write("Extraire les données depuis DBnomics")
try:
 response = requests.get(url)
data = response.json()
st.write("Données dispo")
except Exception as e:
st.write(f"données non dispo : {e}")
data = None
if data:
try:observations = data['series']['docs'][0]['observations']
dates = [obs['period'] for obs in observations]
values = [obs['value'] for obs in observations]    
        df = pd.DataFrame({
            'Date': pd.to_datetime(dates),
            'Rate': values
        })
        df = df.set_index('Date')
        st.write("data dispo")
        st.write(df.head())
    except Exception as e:
        st.write(f"Erreur data : {e}")
        df = None
else:
    st.write("Pas de data")
if df is not None:
    try:
        fig, ax = plt.subplots()
        ax.plot(df.index, df['Rate'], label='Taux Nominal – 10-year US bonds')
        ax.set_xlabel('Date')
        ax.set_ylabel('Rate (%)')
        ax.set_title('Courbe des Taux Nominaux – 10-year US bonds')
        ax.legend()       
        st.pyplot(fig)
        st.write("Graphique dispo")
    except Exception as e:
        st.write(f"Erreur graph: {e}")
else:
st.write("data non dispo")

st.write("Période des taux à définir :")
start_date = st.date_input('Date de début', df.index.min() if df is not None else None)
end_date = st.date_input('Date de fin', df.index.max() if df is not None else None)

if df is not None:
    try:
filtered_df = df.loc[start_date:end_date]
        
        fig, ax = plt.subplots()
        ax.plot(filtered_df.index, filtered_df['Rate'], label='Taux Nominal – 10-year US bonds')
        ax.set_xlabel('Date')
        ax.set_ylabel('Rate (%)')
        ax.set_title(f'Courbe des Taux Nominal – 10-year US bonds ({start_date} - {end_date})')
        ax.legend()
        
        st.pyplot(fig)

streamlit run dashboard.py