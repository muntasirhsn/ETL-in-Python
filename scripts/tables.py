# tables.py

from sqlalchemy import cast, Column, Integer, String, Float, Date
# Import the function required
from sqlalchemy.orm import column_property

from base import Base

class TeslaRaw(Base):
    __tablename__ = "tesla_raw"

    id = Column(Integer, primary_key=True)
    date = Column(String(55))
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adj_close = Column(Float)
    volume = Column(Integer)
    # Create a unique transaction id
    transaction_id = column_property(date + "_") # "_" was added to avoid mix up with date column

class TeslaClean(Base):
    __tablename__ = "tesla_clean"

    id = Column(Integer, primary_key=True)
    # create a date column of type Date NOT String! 
    date = Column(Date)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adj_close = Column(Float)
    volume = Column(Integer)
    # Create a unique transaction id
    transaction_id = column_property(cast(date, String) + "_")

