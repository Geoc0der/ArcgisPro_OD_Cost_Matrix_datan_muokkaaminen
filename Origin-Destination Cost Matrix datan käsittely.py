# Analysoidaan OD Cost Matrix tulosaineistoja. Cost matrix-työkalu on Arcgis Pro-työkalu, joka mittaa kahden vektoritiedoston välillä kaikkien kohteiden
# väliset matka-ajat ja tekee niistä taulukkomuotoisen matriisin. Matka-ajat tuodaan raaka_cm-tiedostoon. Tässä algoritmissa mitattiin maatilojen
# etäisyydet 250m ruuduista. Tämän koodin tuloksena syntyvä csv-tiedosto liitetään alkuperäiseen ruutuaineistoon Arcgis Prossa, jossa aineisto
# myös visualisoidaan.

import pandas as pd

# Tuodaan raakadata sekä esitäytetty tulostiedosto
raaka_cm = pd.read_csv('tiedoston polku', sep=';')
tulos_cm = pd.read_csv('tiedoston polku', sep=';')

# Määritellään funktio, joka summaa halutun destination id:n omaavan ruudun arvot ja palauttaa summan
def hae_aikasumma(id):
    summa = 0.0
    for a in raaka_cm.itertuples():
        if raaka_cm['DestinationID'][a[0]] == id:
            summa = summa + float(raaka_cm['Total_Aika'][a[0]])
    return summa

# For-loopataan läpi kaikki tulostiedoston rivit
for i in tulos_cm.itertuples():
    tulos_cm['AikaSUM'][i[0]] = hae_aikasumma(tulos_cm['DestinationID'][i[0]])
#print(tulos_cm)

# Tallennetaan tulokset uutena csv-tiedostona
tulos_cm.to_csv(r'tiedoston sijainti\tulos_print.csv', sep=';', index=False, encoding='utf-8')