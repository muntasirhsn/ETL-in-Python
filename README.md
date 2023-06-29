# ETL-in-Python
This is a simple demonstration of extract, transform and load (ETL) process in python. Tesla share price data is extracted, transformed and loaded into a PostgreSQL database. 

## Extract (extract.py)
Local directory (data) is created for data to be saved
Download time series data to local directory (data) from remote source (Tesla share price), extract the data in csv format and save data in data/source
Rename the column names/header of the source data and save csv files data/raw

## Transform (base.py, tables.py, transform.py)
Creates engine, session and base to interact with SQL database
Defines python classes to create tables with column names and data types) in SQL database
Create tables (raw and clean) in the database with create_tables.py
Transforms the data from the csv file in the local directory (data/raw) and saves to raw table (tesla_raw) in the database

## Load (load.py, base.py, tables.py)
Further transformations of tesla_raw in the SQL database 
Filter new rows within the tesla_raw table that do not exist in tesla_clean table and insert them into tesla_clean table 

## How to use:
1. Execute the create_tables.py file first to create tables in the SQL database (this should be done only once i.e. only when executing the ETL process for the first time!)

2. Execute execute.py file for completing the ETL process

![image](https://github.com/muntasirhsn/ETL-in-Python/assets/29087240/d242a517-fdcd-4541-a7c1-4ce6588cdb8d)

3. Use an automation tool like Windows Task Scheduler or Airflow to run the execute.py file on a schedule instead of doing it manually and new records will be automatically extracted, transformed and loaded into the database! 
