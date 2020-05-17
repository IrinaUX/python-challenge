import os
import csv
from collections import defaultdict

# Set the file path
path=os.path.join("Resources","budget_data.csv")

def findTotalNumberOfMonths(path):
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        #csv_reader_object = csv.reader(file_input, delimiter=',')
        iterRows = iter(file_input)
        next(iterRows)
        rows_num = (sum(1 for _ in iterRows))
        print(f"The budget data is available for total of {rows_num} months.")
        textFileOutput = open("output.txt","w+")
        textFileOutput.write("Financial Analysis \n")
        textFileOutput.write("--------------------------- \n")
        textFileOutput.write(f"Total Months: {rows_num} \n")
        textFileOutput.close()

def findRevenueTotal(path):
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        csv_reader_object = csv.reader(file_input, delimiter=',')
    
        next(csv_reader_object)
        profit_list = []
        for value in csv_reader_object:
            profit_list.append(int(value[1]))
        total_profit_and_loss = round(sum(profit_list))
        print(f"Total profit and loss is ${total_profit_and_loss}")

        # Append to an existing file:
        textFileOutput = open("output.txt","a+")
        textFileOutput.write(f"Total $: {total_profit_and_loss} \n")
        textFileOutput.close()

# Call functions one by one to process the budget file
findTotalNumberOfMonths(path)
findRevenueTotal(path)
