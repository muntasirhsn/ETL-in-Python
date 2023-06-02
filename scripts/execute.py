# execute.py

# Import the extract, transform and load scripts
import extract
import transform
import load

# Call their main functions
if __name__ == "__main__":
    extract.main()
    transform.main()
    load.main() 
