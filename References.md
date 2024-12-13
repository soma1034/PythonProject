
# Videos und Beiträge mit denen ich mich in den letzten Tagen beschäftigt habe:



## Pandas und Python für die Datenanalyse und Datenaufbereitung:

Referenz: https://www.youtube.com/watch?v=gtjxAH8uaP0

## Machine Learning Video:

Referenz: https://www.youtube.com/watch?v=i_LwzRVP7bg

## Classification Basics:

Referenz:  https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82


## Accuracy, Recall, Precision & F1 Score:+

**Formel:**

 - Accuracy = Total correct guesses / Total guesses

 - Recall = True Positives (TP) / True Positives (TP) + False Negatives

 - Precision = True Positives (TP) / True Positives (TP) + False Positives (FP)

 - F1 Score =  2 * (Precision * Recall / Precision + Recall)
 

Referenz: https://www.youtube.com/watch?v=8d3JbbSj-I8

## ROC-AUC:

Referenz: https://www.youtube.com/watch?v=r4RpCq3nyY4


## Verständnis über die Modelle und Hyperparameter (Logistische Regression, Decision Tree):

### Logistische Regression:
Bei einer Logistischen Regression ist die abhängige Variable eine dichotome variable, das heißt sie kann nur zum Beispiel die Werte 1 und 0 oder ja und nein annehmen.
Dies kann sehr hilfreich sein, wenn man die Eintrittswahrscheinlichkeit von einer bestimmten Sache herausfinden möchte, wie zum Beispiel:
- **Abhängige Variable:** Unfall: Ja/Nein?
- **Unabhängige Variablen:** Geschwindigkeit, Wetter, Fahrzeug

**Formel:** 1/1+e^-z = 1/1+e^-(b1*Geschwindigkeit+b2*Wetter+b3*Fahrzeug+a)   b,a sind die Koeffizienten

Referenz: https://www.youtube.com/watch?v=C5268D9t9Ak



### Decision Tree: 
**(Uses the Greedy Algorithm)**

Bei einer Decision Tree werden die Entscheidungen auf Basis von Baumstrukturen getroffen.
Dabei wird die abhängige Variable in Kategorien eingeteilt (z.B "Ja/Nein" oder "1/0"), indem die Daten iterativ anhand der unabhängigen Variablen (Features) segmentiert werden.

Der Baum besteht aus Knoten, die bestimmte Regeln repräsentieren, und Blättern, die die möglichen Kategorien darstellen.

Ein Entscheidungsbaum teilt die Daten schrittweise auf, indem er bei jedem Schritt die beste Teilung findet.
Die beste Teilung minimiert die Vermischung der Kategorien (z. B. mittels Kriterien wie Gini-Index oder Entropie).
Die Blätter des Baumes geben die vorhergesagte Kategorie der Zielvariablen an.

(Beispiel im Video)
Referenz: https://www.youtube.com/watch?v=ZVR2Way4nwQ

### Hyperparameter-Tuning: 

Hyperparameter-Tuning bedeutet, dass man die besten Einstellungen für ein Machine-Learning-Modell sucht, 
um die Leistung des Modells zu verbessern. 
Hyperparameter sind sowas wie die Lernrate oder die maximale Tiefe eines Entscheidungsbaums, die man vorher festlegen muss. 
Wenn die Werte schlecht gewählt sind, kann das Modell schlecht arbeiten. Mit Methoden wie Grid Search oder Random Search probiert man verschiedene Kombinationen aus, 
bis man die besten Werte findet, damit das Modell auch bei neuen Daten gut funktioniert.


Referenz:

https://www.youtube.com/watch?v=vnXx7t2pnvQ,
 
https://www.youtube.com/watch?v=HdlDYng8g9s


-----------------------------------------------------------------