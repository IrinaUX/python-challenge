import os
import csv

filepath = os.path.join("PyPoll/Resources", "election_data.csv")
with open("filepath", 'r') as filehander:
    data = filehandler.read()
    print(data)