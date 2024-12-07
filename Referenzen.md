
# Videos und Beiträge mit denen ich mich in den letzten 3 Tagen beschäftigt habe:


## Verständnis über die Modelle (Logistische Regression, Decision Tree):

### Logistische Regression:
Bei einer Logistischen Regression ist die abhängige Variable eine dichotome variable, das heißt sie kann nur zum Beispiel die Werte 1 und 0 oder ja und nein annehmen.
Dies kann sehr hilfreich sein, wenn man die Eintrittswahrscheinlichkeit von einer bestimmten Sache herausfinden möchte, wie zum Beispiel
- **Abhängige Variable:** Unfall: Ja/Nein?
- **Unabhängige Variablen:** Geschwindigkeit, Wetter, Fahrzeug

**Formel:** 1/1+e^-z = 1/1+e^-(b1*Geschwindigkeit+b2*Wetter+b3*Fahrzeug+a)   b,a sind die Koeffizienten

Referenz: https://www.youtube.com/watch?v=C5268D9t9Ak


**(Uses the Greedy Algorithm)**

### Decision Tree: 
Bei einer Decision Tree werden die Entscheidungen auf Basis von Baumstrukturen getroffen.
Dabei wird die abhängige Variable in Kategorien eingeteilt (z.B "Ja/Nein" oder "1/0"), indem die Daten iterativ anhand der unabhängigen Variablen (Features) segmentiert werden.

Der Baum besteht aus Knoten, die bestimmte Regeln repräsentieren, und Blättern, die die möglichen Kategorien darstellen.

Ein Entscheidungsbaum teilt die Daten schrittweise auf, indem er bei jedem Schritt die beste Teilung findet.
Die beste Teilung minimiert die Vermischung der Kategorien (z. B. mittels Kriterien wie Gini-Index oder Entropie).
Die Blätter des Baumes geben die vorhergesagte Kategorie der Zielvariablen an.

Referenz: https://www.youtube.com/watch?v=ZVR2Way4nwQ


-----------------------------------------------------------------