import os
import csv
# from collections import defaultdict

# Set the file path
path=os.path.join("Resources","budget_data.csv")
output_file = "output.txt"

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
def find_months_total(path):
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
def find_revenue_total(path, output_file):
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object)
        profit_list = []
        for value in csv_reader_object:
            profit_list.append(int(value[1]))
        total_profit_and_loss = round(sum(profit_list))
        print(f"Total profit and loss is ${total_profit_and_loss}.")

        # Append to an existing file:
        textFileOutput = open(output_file,"a+")
        textFileOutput.write(f"Total $: {total_profit_and_loss} \n")
        textFileOutput.close()

# Define a function to calculate the average change in revenue.
'''
The function takes path parameter as an input and perform the following:
Open file in read mode.
Use csv reader method to read the file line by line.
Use next() method to skip the header.
a)  Define two variables to store current and previous values to calculate the change.
    Initialize both variables as None to use in the conditional statements.
    When values are still in their initial state, then assign the current values.
    When both values are available, then compute the difference.
b)  For the average computation add the following:
    Two new variables to hold the running total of changes and the row count number.
    Calculate the average and round the results before writing to the text output file.
c)  To identify the greatest profit increase and decrease with their respective dates, add the following:
    Add two variables for the greatest increase and greatest decrease.
    Add two more variables for their respective dates.
    Track the maximum increase and maximum decrease using another IF condition inde the else branch of For loop.
    Output the results into the summary table
'''               

def calculate_average_changes_and_pnl_max_min(path, output_file):
    # Define the variables for the difference calculation - num0 is previous value and num1 is the current value.
    num0 = 0 # initialize variable as None (not zero, no value assigned)
    num1 = 0 # initialize variable as None (not zero, no value assigned)
    runningTotalChanges = 0 # Create and initialize variable to keep the running total of the changes for future average calculation.
    row_count = 0 # Create and initialize variable to count the total number of rows for average calculation.
                  # Note: the row count is 86 without the header. But changes are only computed for the 85 rows, since the first row does not have previous value.
                  # Hence, need to initialize as 0 to not take first 0 changes into the average computation.
    changes_average = 0 # Create and initialize variable for the average changes.
    changes_greatest_increased = 0 # Create and initialize variable for the greatest profit increase.
    changes_greatest_decreased = 0 # Create and initialize variable for the greatest profit decrease.
    date_greatest_increase = "" # Create and initialize variable to store the date for the greatest increase for the output file.
    date_greatest_decrease = "" # Create and initialize variable to store the date for the greatest decrease for the output file.
    with open(path, 'r') as file_input:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object) # skip the header line
        # Start the for loop to iterate through each line in the csv file
        for value in csv_reader_object: 
            if num0 == 0: # Check the second row.
                num0 = int(value[1]) 
            else: # for all the other rows
                num1 = int(value[1]) # assign value to the second number.
                change = num1 - num0 # compute the difference.
                print(f"{num1} - {num0} = ${change}.") # print to the terminal
                runningTotalChanges = runningTotalChanges + change # add current difference to the running total.
                num0 = num1
                print(f"Running total in changes is ${runningTotalChanges}.")
                row_count += 1
                print(f"Row count is {row_count}.")
                
                # Add condition to check if the changes are positive or negative for the Greatest increase and Greatest decrease identification.
                if change > changes_greatest_increased:
                    #print(f"Calculated change of ${change} larger than recorded greatest change of ${changes_greatest_increased}.")
                    changes_greatest_increased = change
                    date_greatest_increase = (value[0]) # get the date from the same row index[0]
                    print(f"The data of greatest increase is {date_greatest_increase}.")
                    #print(f"Updated greatest change is ${change}.")
                elif change < changes_greatest_decreased:
                    changes_greatest_decreased = change
                    date_greatest_decrease = (value[0]) # get the date from the same row index[0]
                
        # Outside of the FOR loop, compute the total of all changes over row count:
        print(f"Row count is = {row_count} and total changes are ${runningTotalChanges}.")
        changes_average = runningTotalChanges / row_count # calculate the average changes.
        print(changes_average)
        print(f"Greatest profit increase: {date_greatest_increase} (${changes_greatest_increased})")
        print(f"Greatest profit decrease: {date_greatest_decrease} (${changes_greatest_decreased})")

        # Write the results to the text file:
        textFileOutput = open(output_file,"a+")
        textFileOutput.write(f"Average Change: ${round(changes_average, 2)} \n") # round the printed output average to 2 decimal points.
        textFileOutput.write(f"Greatest Increase in Profits: {date_greatest_increase} (${changes_greatest_increased})\n")
        textFileOutput.write(f"Greatest Decrease in Profits: {date_greatest_decrease} (${changes_greatest_decreased})\n")
        textFileOutput.close()


# Call the functions to perform budget analysis:
find_months_total(path)
find_revenue_total(path, output_file)
calculate_average_changes_and_pnl_max_min(path, output_file)
