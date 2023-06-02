# base.py

# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

# Create the engine
engine = create_engine("postgresql://user:password@@localhost/sample_db") # use your own database details
# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()
