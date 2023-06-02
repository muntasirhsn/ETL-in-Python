# extract.py

import pandas as pd
import yfinance as yf
import os
from datetime import datetime

base_path = "C:/ETL_Demo"
source_path =  base_path + "/data/source/downloaded_at=" + datetime.now().strftime("%Y-%m-%d") 
raw_path = base_path + "/data/raw/downloaded_at=" + datetime.now().strftime("%Y-%m-%d")


# Create a directory at the `path` passed as an argument
def create_directory_if_not_exists(path):
    """
    Create a new directory if it doesn't exists
    """
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist 
        os.mkdir(path)
    

# Write a snapshot of the new data/file obtained to the specified directory
def download_snapshot():
    """
    Download the new data from the source
    """
    create_directory_if_not_exists(source_path)
    df = yf.download('TSLA', period = '1000d', interval = '1d')
    # download the stock data to CSV as a source file
    df.to_csv(os.path.join(source_path, r'Tesla.csv'))

# extract raw data from the downloaded snapshot, transfrom and save to csv
def save_new_raw_data():
    """
    Save new raw data from the source
    """
    create_directory_if_not_exists(raw_path)
    df_raw = pd.read_csv(f"{source_path}/{'Tesla.csv'}")
    df_raw = df_raw.rename(columns={'Date': 'date',
                                'Open': 'open', 
                                'High': 'high', 
                                'Low': 'low', 
                                'Close': 'close',
                                'Adj Close': 'adj_close',
                                'Volume': 'volume'})
    df_raw.to_csv(os.path.join(raw_path, r'Tesla.csv'))
    

# Main function called inside the execute.py script
def main():
    print("Extract started")
    create_directory_if_not_exists(raw_path)
    print("Extract - downloading source file")
    download_snapshot()
    print(f"Extract - saving data from '{source_path}' to '{raw_path}'")
    save_new_raw_data()
    print("Extract ended")
