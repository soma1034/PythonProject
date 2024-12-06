import pandas as pd

# Datei einlesen
file_path = 'C:/Users/Mazlum/Python_Project/PythonProject/data/fruit_data.xlsx'
fruit_data = pd.read_excel(file_path)

# Erste Zeilen anzeigen
print(fruit_data.head())