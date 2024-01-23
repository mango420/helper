# Tests

## Code Aufgaben (F10):

### 1. Aufgabe:

Entfernen Sie Zeilen in "sales",
die doppelte Paare von "store" und "type" haben,
und speichern Sie das Ergebnis als "store_types".
Geben Sie die ersten Zeilen von "store_types" aus.

```
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())
```


### 2. Aufgabe:

Entfernen Sie Zeilen in "sales", 
die doppelte Paare von "store" und "department" haben, 
und speichern Sie das Ergebnis als "store_depts". 
Geben Sie die ersten Zeilen von "store_depts" aus.

```
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())
```


### 3. Aufgabe:

Filtern Sie die Zeilen in "sales" mit Ferienwochen, 
die in der Spalte "is_holiday" gekennzeichnet sind, 
und entfernen Sie doppelte Daten. 
Speichern Sie das Ergebnis als "holiday_dates". 
Wählen Sie die Spalte "date" von "holiday_dates" aus und geben Sie sie aus.

```
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates()
holiday_dates = holiday_dates['date']
print(holiday_dates)
```

### 4. Aufgabe:

Schreibe eine einfache request an https://swapi.dev/api/people und speicher alle heights in ein Panda Dataframe.

import requests
import pandas as pd

response = requests.get("https://swapi.dev/api/people")

data = response.json()

heights = [person['height'] for person in data['results']]

df = pd.DataFrame({'height': heights})

print(df)

## Theoriefragen (F11 / ist probably sus):

### 1. Was ist Data Cleaning?

    a) Daten analysieren
    b) Daten speichern
    c) Daten bereinigen
    d) Daten teilen

    c) Daten bereinigen


### 2. Welches Problem erfordert Data Cleaning NICHT?

    a) Fehlende Daten
    b) Duplikate
    c) Korrekte Daten
    d) Ausreißer

    c) Korrekte Daten


### 3. Welcher Schritt im Data Cleaning-Prozess beinhaltet die Identifizierung von Problemen?

    a) Data Analysis
    b) Data Documentation
    c) Data Visualization
    d) Data Profiling

    a) Data Analysis

