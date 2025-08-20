import pandas as pd
import os

# Definiowanie ścieżki do katalogu
base_path = r"C:\GitHub\automated-excel-data-integration\data"

# Definiowanie nazw plików
main_file = os.path.join(base_path, "Config.xlsx")
search_file = os.path.join(base_path, "BA_LISTA.xlsx")

# Wczytanie plików Excel
df_main = pd.read_excel(main_file, sheet_name="Sheet1", header=None)
df_search = pd.read_excel(search_file, sheet_name="Sheet1", header=None)

# Iteracja przez wiersze w kolumnie "M"
for index, row in df_main.iterrows():
    if pd.isna(row[12]):  # Kolumna "M" to indeks 12 (bez nagłówków)
        break  # Koniec, jeśli napotkamy pustą wartość
    
    search_value = str(row[12])  # Upewnienie się, że wartość to string
    df_search[1] = df_search[1].astype(str)  # Konwersja kolumny "B" na string
    
    # Wyszukiwanie w pliku BA_LISTA.xlsx
    found_rows = df_search[df_search[1] == search_value]
    
    for _, found_row in found_rows.iterrows():
        if found_row[0] == 4 and found_row[5] == "ASSEMBLY":  # Warunek dla "ASSEMBLY"
            folder_row = df_search[(df_search.index < found_row.name) & (df_search[0] == 3) & (df_search[4] == "FOLDERS")].tail(1)
            bought_row = df_search[(df_search.index < found_row.name) & (df_search[0] == 2) & (df_search[5] == "BOUGHT ASSY")].tail(1)
            
            if not folder_row.empty and not bought_row.empty:
                df_main.at[index, 6] = folder_row.iloc[0][1]  # Kolumna "G"
                df_main.at[index, 7] = folder_row.iloc[0][2]  # Kolumna "H"
                df_main.at[index, 4] = bought_row.iloc[0][1]  # Kolumna "E"
                df_main.at[index, 5] = bought_row.iloc[0][2]  # Kolumna "F"
                
                # Wyszukiwanie "DRAWING"
                drawing_row = df_search[(df_search.index > found_row.name) & (df_search[0] == 5) & (df_search[5] == "DRAWING")].head(1)
                if not drawing_row.empty:
                    df_main.at[index, 8] = drawing_row.iloc[0][1]  # Kolumna "I"
                    df_main.at[index, 9] = drawing_row.iloc[0][2]  # Kolumna "J"
                
                # Wyszukiwanie "INSTALLATION"
                install_row = df_search[(df_search.index < found_row.name) & (df_search[5] == "INSTALLATION")].tail(1)
                if not install_row.empty:
                    df_main.at[index, 1] = install_row.iloc[0][1]  # Kolumna "B"
                    df_main.at[index, 2] = install_row.iloc[0][2]  # Kolumna "C"

# Zapis wyników
df_main.to_excel(main_file, sheet_name="Sheet1", index=False, header=False)

