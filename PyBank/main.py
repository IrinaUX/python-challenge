import os
import csv
from collections import defaultdict

# Set the file path
path=os.path.join("Resources","budget_data.csv")

# Define a function to count total number of months/
'''
This function take the path variable defined outside the function as an input.
With provided path, open the csv file using "with" method to avoid issues, when forgetting to close the file.
Open csv file in read mode and optional parameter newline default to null.
Open csv file as "file_input".
Use iter() method to iterate through each row in the csv file.
Use next() method to skip the header line.
Use list comprehension to sum up the numbers of rows.
Print the found months.
Create text file named output.txt in write mode (also create new file, if does not exist).
Write first line.
Write new lines.
'''
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

#Define function to find the total revenue:
'''
The function takes path parameter as an input.
Open file in read mode.
Use csv reader method to read the file line by line
Use next() method to skip the header.
Define profit_list parameter as empty list.
Loop through the csv object and append the value from column 2 (index[1] in the array).
At the same time, define the value as data type integer.
Use sum method on the profit_list to obtain the total revenue.
At the same time, round the sum value.
Print the statement and write into output.txt file
'''
def findRevenueTotal(path):
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object)
        profit_list = []
        for value in csv_reader_object:
            profit_list.append(int(value[1]))
        total_profit_and_loss = round(sum(profit_list))
        print(f"Total profit and loss is ${total_profit_and_loss}.")

        # Append to an existing file:
        textFileOutput = open("output.txt","a+")
        textFileOutput.write(f"Total $: {total_profit_and_loss} \n")
        textFileOutput.close()

# Define a function to calculate the average change in revenue.
def averageChange(path):
    # maxPostive = 0
    # maxNegative = 0
    # changeNegative = []
    # changePositive = []
    num0 = None
    num1 = None
    num2 = None
    with open(path, 'r', newline='') as file_input:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object) # skip the header
        #str1 = next(csv_reader_object) # assign next row to str1 parameter
        #print(str1)
        #string_split = str1.index[1]
        #print(string_split)
        for value in csv_reader_object:
            if num0 == None: # first value in column Profit/Losses is unknown
                num0 = int(value[1])
                print(f"The very first value in column pnl is ${num0}.")
                #changeNegative.append(int(value[1]))
                #print(f"Losses collected in one list ${changeNegative}.")
            elif num1 == None:
                num1 = int(value[1])
            elif num0 is not None and num1 is not None:
                #num1 = int(value[1])
                #print(f"The first value in column pnl is ${num1}.")
                change = num1 - num0
                #num1 = next(int(value[1]))
                print(f"Next first value is changed to $ {num1}.")
                print(f"Pnl change is ${change}.")
                next(csv_reader_object)
            elif num1 is not None and num2 is not None:
                num2 = int(value[1])
                print(f"The second value in column pnl is ${num2}.")
                change = num2 - num1
                print(f"Next Pnl change is ${change}.")
                next(csv_reader_object)
                print(f"Next second value is changed to $ {num2}.")
            elif num0 is not None and num1 is not None: # when two values for comparison are not absent.
                change = num1 - num0
                print(change)



    # print(f"The first value in column pnl is ${num1}.")
    # print(f"The next value in column pnl is ${num2}.")
    # Compute the difference between the two numbers (previous and next):
    
                #changePositive.append(int(value[1]))
                #print(f"Losses collected in one list ${changePositive}.")
    #print(f"LOSSES collected in one list ${changeNegative}.")
    #print(f"PROFIT collected in one list ${changePositive}.")

# Call functions one by one to process the budget file
# findTotalNumberOfMonths(path)
# findRevenueTotal(path)
averageChange(path)
