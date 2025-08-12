# Finanzdaten-Erfassung und Zeitreihenanalyse

**Version:** 1.0  
**Lizenz:** Forschungsnutzung – keine kommerzielle Anwendung, keine Haftung

---

## 1. Einleitung

Dieses Projekt dokumentiert den Aufbau, die Funktionsweise und die Ergebnisse eines Systems zur **automatisierten Erfassung von Aktienkursen** ausgewählter Unternehmen, ihrer **Speicherung in Zeitreihenform** sowie der **wissenschaftlichen Analyse**.

Die Zielsetzung umfasst:
- **Kontinuierliche Beobachtung** definierter Wertpapiere
- **Strukturierte Datenhaltung** für Zeitreihenanalysen
- **Ermittlung von Korrelationen** und Abhängigkeiten zwischen Titeln
- **Vorbereitung von ML-Features** für Prognosemodelle

Die Daten werden **ausschließlich** zu Forschungs- und Lehrzwecken verwendet.  
Es erfolgt **keine** Finanzberatung.

---

## 2. Hintergrund und Zielsetzung

Die Analyse von Preisbewegungen mehrerer Aktien über die Zeit ermöglicht:
- Identifikation potenzieller **Abhängigkeiten** (z. B. innerhalb einer Branche)
- **Quantifizierung von Korrelationen** und deren Stabilität
- Erkennung **gemeinsamer Preistreiber** und Markteinflüsse
- Aufbau von **Prognosemodellen** (z. B. Regressions-, Klassifikations- oder Deep-Learning-Modelle)

Das System ist als **Proof of Concept (PoC)** angelegt und kann erweitert werden.

---

## 3. Methodik

### 3.1 Datenerhebung
- **Quelle:** [`yahoo_fin`](https://theautomatic.net/yahoo_fin-documentation/)
- **Konfiguration:** über `aktien.json`:
    ```json
    [
      { "otc": "ddaif", "name": "DAIMLER" },
      { "otc": "baba",  "name": "ALIBABA" },
      { "otc": "tyekf", "name": "Thyssen Krupp" }
    ]
    ```
- **Ablauf:** 
  1. JSON einlesen
  2. Live-Preis für jeden Ticker abrufen
  3. Datensatz mit Zeitstempel in `stock_values_record.csv` anhängen

**Datenmodell:**

| Spalte     | Typ           | Beschreibung                                   |
|------------|---------------|------------------------------------------------|
| `datetime` | datetime64[ns] | Zeitstempel (UTC empfohlen)                   |
| `otc`      | string        | OTC-Ticker                                     |
| `names`    | string        | Aktienname                                     |
| `price`    | float64       | Live-Preis                                     |

---

### 3.2 Vorverarbeitung
- **Parsing:** CSV → Pandas DataFrame
- **Sortierung:** nach Zeit und Name
- **Pivotierung:** Wide-Format für mehrdimensionale Zeitreihen
- **Resampling:** Normierung auf gleichmäßige Intervalle
- **Transformationen:** 
  - Log-Returns: `ln(P_t) - ln(P_{t-1})`
  - Differenzen: `P_t - P_{t-1}`
- **Fehlwertbehandlung:** Forward-Fill oder Interpolation bei kleinen Gaps

---

### 3.3 Analytische Verfahren
- **Deskriptive Statistik:** Mittelwert, Standardabweichung, Varianz pro Aktie
- **Korrelationen:** Pearson (linear) und Spearman (monoton)
- **Rolling-Korrelationen:** z. B. 60-Zeitschritt-Fenster
- **Visualisierung:** Linienplots, Heatmaps, Scatterplots

---

## 4. Implementierung

### 4.1 Kernskript (`stock.py`)
- Liest `aktien.json`
- Ruft Live-Preise ab
- Speichert Daten persistent in CSV

## 5. Analyseergebnisse

### 5.1 Datensatz
- **Zeitraum der Erhebung:** Mehrere aufeinanderfolgende Zeitstempel  
- **Titel:** DAIMLER, ALIBABA, Thyssen Krupp  
- **Erfassungsintervall:** Minutenbereich  

### 5.2 Beobachtungen
- **Preisbewegungen:** Im beobachteten Zeitraum nahezu konstant (Testphase, keine Handelsvolatilität erfasst)  
- **Korrelationen:**  
  Aufgrund geringer Preisvariation in Testläufen nicht signifikant.  
  Bei längerer Erhebung ist zu erwarten:
  - Hohe Korrelationen bei Titeln aus ähnlichen Sektoren
  - Geringe oder negative Korrelationen bei unterschiedlichen Märkten/Regionen  

### 5.3 Interpretation
Das PoC zeigt, dass die Infrastruktur funktioniert, jedoch:  
- Für aussagekräftige Korrelationen wird ein längerer Erfassungszeitraum benötigt  
- Handelszeiten und Feiertage sollten berücksichtigt werden  
- Daten sollten auf Marktvolatilität kalibriert werden  

---

## 6. Qualitätsaspekte
- **Reproduzierbarkeit:** Append-Only Speicherung der Rohdaten  
- **Versionierung:** JSON-Konfiguration versioniert  
- **Datenintegrität:** Keine Überschreibung bestehender Daten  
- **Zeitzonen-Standard:** UTC empfohlen  

---

## 7. Erweiterungspotenzial
- Automatisierte Erfassung per Cron/Scheduler  
- Einbindung weiterer Assetklassen (Indizes, Rohstoffe, Währungen)  
- Handelskalender-Integration  
- Echtzeit-Dashboards (z. B. Streamlit)  
- ML-Modelle zur Kursprognose  

---

## 8. Limitationen
- Keine garantierte Echtzeitgenauigkeit  
- Abhängigkeit von Yahoo Finance API-Struktur  
- Kein automatisches Handling von Dividenden oder Aktiensplits  
- Fehlende Marktöffnungszeiten-Logik  

---

## 9. Rechtlicher Hinweis
- Nutzung nur im Rahmen der Yahoo-Finance-AGB  
- Keine Anlageberatung  
- Ergebnisse abhängig von Datenqualität und Erfassungsintervall  

---

## 10. Lizenz
Dieses Repository wird unter einer Forschungs- und Lehrlizenz bereitgestellt.  
Kommerzielle Nutzung und API-Missbrauch sind untersagt.  

