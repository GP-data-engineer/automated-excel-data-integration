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

## Requirements
- Python 3.10+
- pandas
- openpyxl

Install dependencies:
```bash
pip install pandas openpyxl
