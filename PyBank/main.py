# Import modules
import csv
import os

# Create a path for csv file
filepath = os.path.join("PyBank/Resources", "budget_data.csv")
#print(filepath)

# Open csv file in read mode
with open (filepath, "r") as file_handler:
    lines=file_handler.read()
    print(lines)
    print(type(lines))
    file_handler.read()
    print(filepath)

# io.UnsupportedOperation: not readable.
# looks like the file is already closed.
# Try to reopen the file with read atribute:
#   Type error: expected str, bytes or os.pathlike object.
# Try to use file path instead of file_handler
#with open(filepath) as file_handler2:
 #   data = file_handler2.read()
  #  print(data)

# Read csv file
#file_handler.read()
#csvreader = csv.reader(filepath, delimiter=",")
#print(csvreader)
