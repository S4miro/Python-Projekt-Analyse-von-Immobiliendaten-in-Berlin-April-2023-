# Python-Projekt-Analyse-von-Immobiliendaten-in-Berlin-April-2023
*Explorative Preisanalyse*

In diesem kleinen Projekt habe ich Immobilienanzeigen aus Berlin (April 2023, Quelle: Immowelt.de) analysiert, um zentrale Muster in Preisen, Fläche und anderen Einflussfaktoren zu erkennen.  
Dies ist mein erstes Python-Projekt im Bereich Data Science und zeigt Datenbereinigung, Visualisierung und einfache Modellierung.
Dieses Projekt ist eine erste Explorationsanalyse mit Python und diente mir als Training im Umgang mit Datenanalyse-Tools (Pandas, Seaborn, scikit-learn).

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
