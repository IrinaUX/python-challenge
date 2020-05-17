import os
import csv
# from collections import defaultdict

# Set the file path
path=os.path.join("Resources","budget_data.csv")

# Define a function to count total number of months.
'''
This function takes the path variable defined outside the function as an input.
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
'''
The function takes path parameter as an input and perform the following:
Open file in read mode.
Use csv reader method to read the file line by line.
Use next() method to skip the header.
Define two variables to store current and previous values to calculate the change.
Initialize both variables as None to use in the conditional statements.
When values are still in their initial state, then assign the current values.
When both values are available, then compute the difference.
Print to the console.
Note: still working on how to make the last row to be taken into the computation loop.
Note: currently the loop does not take the last row into the computation.
'''
def averageChange(path):
    # Define the variables for the difference calculation - num0 is previous value and num1 is the current value.
    num0 = None # initialize variable as None (not zero, no value assigned)
    num1 = None # initialize variable as None (not zero, no value assigned)
    with open(path, 'r', newline='') as file_input:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object) # skip the header of the csv file
        # Start For loop to iterate over the csv file line by line:
        for value in csv_reader_object: # for each line in the csv file
            if num0 is None: # if num0 is still None - not assigned yet, then:
                num0 = int(value[1]) # assign the value from current row's column.index[1].
            elif num0 is not None and num1 is None: # Check the second row.
                # if num0 is available, but num1 is still not assigned, then assign num1 variable value from the current row's column.index[1].
                num1 = int(value[1]) # assign value to the second number.
            elif num0 is not None and num1 is not None: # Finally, when both values are available, then:
                change = num1 - num0 # compute the difference.
                print(f"{num1} - {num0} = ${change}.") # print to the terminal
                num0 = num1 # swap the value of num0 to the num1 for the next loop's calculation.
                num1 = int(value[1]) # assign a new value to the num1 variable for the next loop's calculation.
                

# Call the functions to perform budget analysis:
findTotalNumberOfMonths(path)
findRevenueTotal(path)
averageChange(path)
