# automated-excel-data-integration
Python script for automating data mapping and integration between engineering Excel files. Uses Pandas for ETL-like processing, enabling efficient lookup, transformation, and update of configuration spreadsheets.

# Excel Data Mapping Automation

This project automates the process of mapping and updating engineering Excel configuration files using Python and Pandas.  
It performs ETL-like operations:
- Extracts data from source spreadsheets
- Searches and matches configuration values
- Updates target Excel files with corresponding data (assembly, folders, drawings, installation references)

## Features
- Automated lookup and mapping between two Excel files
- ETL (Extract, Transform, Load) workflow with Pandas
- Engineering-oriented use case (configurations, assemblies, BOM-like data)
- Easy to adapt for similar Excel integration tasks

## How it works
The workflow of the script is straightforward and tailored to engineering Excel data:
1. The script opens the main configuration file **Config.xlsx**.  
2. It reads values from column **M** (e.g., assembly identifiers).  
3. For each value, it searches in the reference file **BA_LISTA.xlsx**.  
4. If a match is found, the script retrieves related data such as:
   - **ASSEMBLY** information  
   - **FOLDERS**  
   - **BOUGHT ASSY**  
   - **DRAWING**  
   - **INSTALLATION**
5. The retrieved data is then written back into the corresponding row of **Config.xlsx**, filling in missing values automatically.  
This process turns a manual, repetitive data lookup into an automated ETL-like pipeline optimized for engineering use cases.

## Requirements
- Python 3.10+
- pandas
- openpyxl

Install dependencies:
```bash
pip install pandas openpyxl
