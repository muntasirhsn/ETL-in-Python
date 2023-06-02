# load.py

from base import session
from tables import TeslaRaw, TeslaClean

from sqlalchemy import cast, Integer, Date, delete
from sqlalchemy.dialects.postgresql import insert

def insert_transactions():
    """
    Insert operation: adds new data
    """
    
    # Select the transaction ids in the clean table TeslaClean
    clean_transaction_ids = session.query(TeslaClean.transaction_id)

    # Select the columns and cast the appropriate types if needed
    transactions_to_insert = session.query(
        cast(TeslaRaw.date, Date),
        TeslaRaw.open,
        TeslaRaw.high,
        TeslaRaw.low,
        TeslaRaw.close,
        TeslaRaw.adj_close,
        TeslaRaw.volume
        # Filter for the new rows
        ).filter(~TeslaRaw.transaction_id.in_(clean_transaction_ids))

    # Print total number of transactions to insert
    print("Transactions to insert:", transactions_to_insert.count())

    # Insert the rows from the previously selected transactions
    columns = ["date", "open", "high", "low", "close", "adj_close", "volume"]
    statement = insert(TeslaClean).from_select(columns, transactions_to_insert)

    # Execute and commit the statement to make changes in the database.
    session.execute(statement)
    session.commit()
    

    

def main():
    print("Load started")
    print("Load - inserting new rows")
    insert_transactions()
    print("Load ended")
