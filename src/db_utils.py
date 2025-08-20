from sqlalchemy import create_engine
import pandas as pd

def save_to_db(df, table_name, connection_string):
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"✅ Saved {len(df)} rows into {table_name}")