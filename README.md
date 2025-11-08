# Python-Projekt-Analyse-von-Immobiliendaten-in-Berlin-April-2023
*Explorative Preisanalyse*

In diesem kleinen Projekt habe ich Immobilienanzeigen aus Berlin (April 2023, Quelle: Immowelt.de) analysiert, um zentrale Muster in Preisen, Fläche und anderen Einflussfaktoren zu erkennen.  
Dieses Projekt zeigt zeigt wie man Datenbereinigung, Visualisierung und einfache Modellierung durchführt.


## Inhalt
- `RealEstate_Analyse.py` → Hauptskript mit allen Analysen und Visualisierungen  
- [https://www.kaggle.com/datasets/mathisjander/real-estate-listings-berlin-de-april-2023] (20.09.2025, 15:21 Uhr) → Ursprungsdatensatz  
  

## Funktionen
- Datenbereinigung & Umgang mit fehlenden Werten  
- Explorative Datenanalyse: Statistiken, Boxplots, Scatterplots  
- Korrelationen (Pearson & Spearman)  
- Lineare Regression: Fläche → Preis  
 
## Nutzung
1. Lade den Datensatz herunter und speichere ihn im Projektordner  
2. Öffne `RealEstate_Analyse.py` in einer Python-Umgebung 
3. Installiere die benötigten Pakete:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
4. Stelle sicher, dass das Skript im **Working Directory** liegt oder setze das Working Directory im Skript:
   ```python
   import os
   os.chdir("Pfad/zum/Projektordner")
