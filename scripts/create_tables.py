# create_tables.py

from base import Base, engine
# Import the TeslaRaw , TeslaClean table
from tables import TeslaRaw, TeslaClean

# Create the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)
