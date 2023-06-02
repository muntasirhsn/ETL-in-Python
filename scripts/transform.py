# transform.py

import numpy as np
import pandas as pd
import os
import csv
from datetime import datetime

from tables import TeslaRaw
from base import session
from sqlalchemy import text

# Settings
base_path = os.path.abspath(__file__ + "/../../") # parent folder of the .py file 
source_path =  base_path + "/data/source/downloaded_at=" + datetime.now().strftime("%Y-%m-%d") 
raw_path = base_path + "/data/raw/downloaded_at=" + datetime.now().strftime("%Y-%m-%d")


def reduce_decimal(float_input):
    """
    Reduces the decimal poins for float value columns, e.g. 'open', 'high' etc. 
    """
    float_input = np.round(float_input, decimals=4)
    return float_input


def truncate_table():
    """
    Ensures that "tesla_raw" table is always in empty state before running any transformations.
    
    """
    session.execute(
        text("TRUNCATE TABLE tesla_raw;ALTER SEQUENCE tesla_raw_id_seq RESTART;")
    )
    session.commit()


def transform_new_data():
    """
    Applies all transformations for each row in the .csv file before saving it into database
    """
    df_raw = pd.read_csv(raw_path + '/Tesla.csv')
    Tesla_raw_objects = []
    for index, row in df_raw.iterrows():
        # Apply transformations and save as TeslaRaw object
            Tesla_raw_objects.append(
                TeslaRaw(
                    date=row["date"],
                    open=reduce_decimal(row["open"]),
                    high=reduce_decimal(row["high"]),
                    low=reduce_decimal(row["low"]),
                    close=reduce_decimal(row["close"]),
                    adj_close=reduce_decimal(row["adj_close"]),
                    volume=row["volume"],
                )
            )
            
    # Bulk save all new processed objects and commit
    session.bulk_save_objects(Tesla_raw_objects)
    session.commit()
        


def main():
    print("Transform started")
    print("Transform - removing any old data from tesla_raw table")
    truncate_table()
    print("Transform - transforming new data available in tesla_raw table")
    transform_new_data()
    print("Transform ended")
