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
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# Ecriture des entetes de la page WEB Application
st.title('VOITURE : USA vs EUROPE vs JAPON')
st.subheader('Modele de voiture de 1971 à 1983', divider='rainbow')
st.write("AG BONNET - 04/2024")



option = st.selectbox(
   "Visualisation par origine",
   ("US", "Europe", "Japon"),
   index=None,
   placeholder="choisir une origine...",
)


st.write(df_cars)

# Here we use "magic commands":
df_cars



