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
st.title('VOITURES DES ANNEES 1971 - 1983 ')
st.subheader('USA / EUROPE / JAPON', divider='rainbow')
st.write("AG BONNET - 04/2024")

# Mettre du texte explicatif : 
st.write("Présentation des donnnées cars.csv :")

st.write("Le dataset fournit des spécifications techniques sur les modèles de voitures produits sur la période de 1971 à 1983.")
st.write("Description des variables :)

st.write("mpg (miles per gallon) : la consommation d'essence d'une voiture")
st.write("cylinders: le nombre de cylindres du moteur")
st.write("displacement: le volume interne du moteur à combustion (souvent en cm3)")
st.write("horsepower: la puissance du moteur en chevaux")
st.write("weight: le poids de la voiture (en pounds)")
st.write("acceleration: la durée en seconde pour passer de l'arrêt (0 km/h) à 60 mph (environ 97 km/h)")
st.write("year: l'année de production")
st.write("continent : région de production")
    


option = st.selectbox(
   "Visualisation par continent",
   ("US", "Europe", "Japon"),
   index=None,
   placeholder="choisir une origine...",
)


st.write(df_cars)

# Here we use "magic commands":
df_cars



