##############################################################################################
#
# Ma PREMIERE APPLICATION WEB
# Challenge :
#
# A partir du dataset des voitures, tu afficheras :
#
# Une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.
# Des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon).
# L'application doit être disponible sur la plateforme de partage.
#
# Publie ensuite ici le lien de ton application. Le lien doit ressembler à https://share.streamlit.io/wilder/streamlit_app/#my_streamlit_app.py.
##############################################################################################

import streamlit as st
#import numpy as np
import pandas as pd
import seaborn as sns
## 

# Ecriture des entetes de la page WEB Application
st.title('Voitures : USA vs EUROPE vs JAPON')
st.subheader(' ', divider='rainbow')
st.write("AG BONNET - 04/2024")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

option = st.selectbox(
   "Origine des voitures",
   ("US", "Europe", "Japan"),
   index=None,
   placeholder="Select contact method...",
)

df_cars = pd.read_csv(link)

st.write(df_cars)

# Here we use "magic commands":
df_cars



