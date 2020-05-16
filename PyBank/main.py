# Import modules
import csv
import os

# Create a path for csv file
filepath = os.path.join("Resources", "budget_data.csv")
#print(filepath)

# Open csv file in read mode
with open (filepath, "r") as file_handler:
    lines=file_handler.read()
    print(lines)
    print(type(lines))
    file_handler.read()
    print(f'file path {filepath}')



