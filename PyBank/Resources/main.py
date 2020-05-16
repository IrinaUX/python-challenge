import os
import csv
file = "budget_data.csv"
with open(file, 'r') as filehandler:
    lines=filehandler.read()
    print(lines)
    print(type(lines))

