'Analyse von Immobiliendaten in Berlin im April 2023 aus Immowelt.de'
#Ziel: Einfache Preisanalyse


import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from sklearn.linear_model import LinearRegression   

#os.chdir("D:/R") # Arbeitsverzeichnis setzen


df = pd.read_csv("real_estate_listings_clean.csv", na_values=["na"])    # "na" als NaN interpretieren

print(df.head())          # Erste 5 Zeilen anzeigen
print(df.info())          # Überblick über die Daten
print(df.describe())      # Statistische Übersicht

print(df.isnull().sum())  # Zeigt die Anzahl der fehlenden Werte pro Spalte
print(df.isnull().any())  # Zeigt, ob es in einer Spalte überhaupt NaNs gibt

df["energy"] = df["energy"].fillna("Unbekannt")   # Fehlende Werte in "energy" mit "Unbekannt" füllen
df["heating"] = df["heating"].fillna("Unbekannt") # Fehlende Werte in "heating" mit "Unbekannt" 




numeric_df = df.select_dtypes(include=[np.number]) # Nur numerische Spalten auswählen

correlation_matrix = numeric_df.corr() # Korrelationsmatrix berechnen
print(correlation_matrix)              # Korrelationsmatrix anzeigen


plt.figure(figsize=(10, 8))                                  # Optional: Größe der Grafik
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm") # Heatmap erstellen
plt.title("Korrelationsmatrix Heatmap")                      # Titel hinzufügen
plt.show()                                                   # Grafik anzeigen



plt.figure(figsize=(8, 6))                                # Optional: Größe der Grafik
sns.boxplot(x=df["price"])                                # Boxplot erstellen
plt.title("Boxplot der Immobilienpreise in Berlin")       # Titel hinzufügen
plt.xlabel("Preis (€)")                                   # x-Achsenbeschriftung hinzufügen

ax = plt.gca() 
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"{int(x):,} €")) # Tausendertrennzeichen und Euro-Zeichen hinzufügen
plt.show()                                                                        # Grafik anzeigen

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["area"], y=df["price"])               # Scatterplot erstellen
plt.title("Preis vs. Fläche")
plt.xlabel("Fläche (m²)")
plt.ylabel("Preis (€)")
ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f"{int(x):,} €")) # Tausendertrennzeichen und Euro-Zeichen hinzufügen
plt.show()

spearman_corr = numeric_df.corr(method="spearman")
print(spearman_corr)


X = numeric_df[["area"]]               # Unabhängige Variable
y = numeric_df.loc[X.index, "price"]   # Abhängige Variable 

model = LinearRegression()  # Lineares Regressionsmodell erstellen
model.fit(X, y)             # Modell an die Daten anpassen

R_squared = model.score(X, y)  # Bestimmtheitsmaß (R²) berechnen
print(f"Erklärte Varianz (R^2) Fläche → Preis: {R_squared:.2f}")
Intercept = model.intercept_   # Achsenabschnitt
Slope = model.coef_[0]         # Steigung
print(f"Preis = {Intercept:.2f} + {Slope:.2f} * Fläche")



print("\n--- Zusammenfassung ---")
print("Die Analyse zeigt, dass die Wohnfläche einen starken Einfluss auf den Immobilienpreis hat.")
print("Das lineare Modell schätzt: Preis = {:.2f} + {:.2f} * Fläche".format(Intercept, Slope))
print("Weitere Einflussfaktoren könnten in einer erweiterten Analyse betrachtet werden und dem Modell hinzugefügt werden. Da die Variablen sehr ähnlich sind, sollte man auf Multikollinearität prüfen.")


