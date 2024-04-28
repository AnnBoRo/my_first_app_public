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
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import plotly.express as px
##
sns.set_style("whitegrid")

st.title('Voitures Modèles 1971-1983 comparaison US vs EUROPE vs JAPAN')
st.subheader("*AG BONNET - 04/2024*", divider='blue')

# Mettre du texte explicatif : 


st.write("**Le dataset utilisé pour cette analyse contient des spécifications techniques sur les modèles de voitures produits en US/EUROPE/JAPON sur la période de 1971-1983.**")


DATE_COLUMN = 'year'
DATA_URL = ('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv') 


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#data_load_state = st.text('Loading data...')
data = load_data(10000)
#data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Dataset'):
    st.subheader('cars.csv')
    st.write(data)
    st.markdown("***Description des variables :***")

    st.markdown("*   **mpg** (miles per gallon) : la consommation d'essence d'une voiture. \n  \n   Attention, **en France**, nous comptons la consommation en nombre de litres pour 100 km. Plus une voiture consomme et plus elle a une valeur élevée de litres pour faire 100 km.  **Aux USA**, ils comptent la consommation en miles (environ 1.6 km) par gallon (environ 4.55 litres). Plus une voiture consomme et moins elle a une valeur élevée de mpg.  \n *   **cylinders** : le nombre de cylindres du moteur.  \n *   **cubicinches** (cylindrée): le volume interne du moteur à combustion (souvent en cm3).  \n *    **hp (horsepower)** : la puissance du moteur en chevaux.  \n *    **weightlbs** : le poids de la voiture.  \n *    **time-to-60** (accélération) : la durée en seconde pour passer de l'arrêt (0 km/h) à 60 mph (environ 97 km/h). \n *    **year** : l'année de production du modèle. \n *    **continent** : origine des constructeurs.")

st.subheader("", divider='blue')
st.subheader(' ')

# HISTOGRAMME nb de modele par region:
######################################
st.subheader("*Répartition de la production des véhicules*", divider='green')
fig, ax = plt.subplots(figsize=(6,1.5))

ax1 = sns.histplot(data, y='continent')
ax1.set_xlabel('')
ax1.set_ylabel('')
ax1 = plt.title('Nb de modèles produits')

st.pyplot(fig)

st.markdown("Sur cette période, les constructeurs US ont été largement plus prolifiques que les autres constructeurs.  \n En effet, en Europe et au Japon, la production de modèle de voiture est globalement 3 fois plus faible.\n")

# BOXPLOT pour la puissance :
#############################
st.subheader("*Puissance des véhicules*", divider='green')

fig, ax = plt.subplots(1,2,figsize=(10,3))

ax1 = plt.subplot(1,2,1)
ax1 = sns.kdeplot(data, x="hp", hue="continent") 
ax1 = plt.title('Histogramme des Puissances')

ax2 = plt.subplot(1,2,2)
ax2 = sns.boxplot(data, x="hp",y= "continent", fliersize=0 )
ax2 = plt.title('Boxplot des Puissances')

st.pyplot(fig)

st.markdown("La puissance est plus dispersée aux USA qu'en Europe.   \n Aux USA, la majorité des voitures a une puissance supérieure à 100.   \n En Europe, la moitié des véhicules ont une puissance entre 70 et 90 chevaux.")

#########################################################
# Selection de la region:
option = st.selectbox(
   "**Choisir l'origine du constructeur pour une meilleure visualisation**",
   (" US.", " Europe.", " Japan."),
   index=None,
   placeholder="Toutes",
)

if option == None : 
  data_option = data
else:
  data_option = data[data["continent"] == option]

clear_figure = True
fig, ax = plt.subplots(figsize=(6,1.5))
ax=sns.kdeplot(data_option, x="hp")
plt.title("Histogramme des Puissances suivant l'origine")
st.pyplot(fig)

st.markdown("Pour l'Europe, l'histogramme présente une courbe de Gauss, cela indique une quasi homogénéité des puissances des voitures.  \n En revanche, pour les USA et le Japon, il semble y avoir une combinaison de 2 courbes de Gauss ce qui pourrait correspondre à des sous catégories : citadines et SUV ?")

# HEATMAP Correlations :
#############################
st.subheader("*Recherche de corrélation*", divider='green')
clear_figure = True
fig, ax = plt.subplots(figsize=(10,3))

ax1 = sns.heatmap(data.corr(numeric_only=True),
                  cmap=sns.diverging_palette(h_neg=0, h_pos=275, s=70, l=55,as_cmap=True),
                  center = 0,
                  annot=True) 
ax1 = plt.title('Heatmap')
st.pyplot(fig)

st.markdown("Les variables corrélées positivement sont : cylindrée/horsepower, cylindrée/poids, .  \nLes variables corrélées négativement sont : mpg/puissance, mpg/poids.  \nLes variables qui ne semblent pas ou très peu corrélées sont : poids/année du modèle, acceleration/année du modèle.")

# Nuages de points :
##############################
option2 = st.selectbox(
   "**Choisir une corrélation**",
   ("Poids/mpg", "Poids/Puissance", "Accélération/Puissance"),
   index=None,
   placeholder="Vide",
)

if option2 == "Poids/mpg":
  x1 = "mpg"
  y1 = "weightlbs"
  titre = "Corrélation Poids/mpg"
  texte = "Sans surprise, les voitures les plus puissantes qui ont également été produites aux US sont celles qui consomment le plus.  \n  Rappel : **mpg** (miles per gallon) : la consommation d'essence d'une voiture aux US.  \n  **Aux USA**, ils comptent la consommation en miles (environ 1.6 km) par gallon (environ 4.55 litres) : plus une voiture consomme et moins elle a une valeur élevée de mpg.  \n "
elif option2 == "Poids/Puissance":
  x1 = "hp"
  y1 = "weightlbs"
  titre = "Corrélation Poids/Puissance"
  texte = "Les voitures les plus puissantes sont les plus lourdes et ont pour origine les constructeurs US  \n "
elif option2 == "Accélération/Puissance":
  x1 = "hp"
  y1 = "time-to-60"
  titre = "Corrélation Accélération/Puissance"
  texte = "Les voitures les plus puissantes sont celles qui accélèrent le plus rapidement et ont pour origine les constructeurs US  \n "

if option2 != None :
  clear_figure = True
  fig, ax = plt.subplots(figsize=(10,3))
  ax = sns.scatterplot(
            data,
            x = x1,
            y = y1,
            hue="continent",
            )
  ax = plt.title(titre)
  st.pyplot(fig)
  st.markdown(texte)
