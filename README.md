# python-challenge
Python - week 1 - homework

# Python Homework notes, by Irina Kim.

## PyBank
For this analysis, three functions have been implemented:
1. Find total number of months.
2. Find total revenue.
3. Find the profit and loss change (in progress). 
Below is the current documentation for each function:
All functions use global variable "path" to pass the file path.

### Define a function to count total number of months.
### def findTotalNumberOfMonths(path)
- This function takes the path variable defined outside the function as an input.
- With provided path, open the csv file using "with" method to avoid issues, when forgetting to close the file.
- Open csv file in read mode and optional parameter newline default to null.
- Open csv file as "file_input".
- Use iter() method to iterate through each row in the csv file.
- Use next() method to skip the header line.
- Use list comprehension to sum up the numbers of rows.
- Print the found months.
- Create text file named output.txt in write mode (also create new file, if does not exist).
- Write first line.
- Write new lines.


### Define function to find the total revenue:
### def findRevenueTotal(path)
- The function takes path parameter as an input.
- Open file in read mode.
- Use csv reader method to read the file line by line
- Use next() method to skip the header.
- Define profit_list parameter as empty list.
- Loop through the csv object and append the value from column 2 (index[1] in the array).
- At the same time, define the value as data type integer.
- Use sum method on the profit_list to obtain the total revenue.
- At the same time, round the sum value.
- Print the statement and write into output.txt file

### Define a function to calculate the average change in revenue.
### def averageChange(path) 
- The function takes path parameter as an input and perform the following:
- Open file in read mode.
- Use csv reader method to read the file line by line.
- Use next() method to skip the header.
- Define two variables to store current and previous values to calculate the change.
- Initialize both variables as None to use in the conditional statements.
- When values are still in their initial state, then assign the current values.
- When both values are available, then compute the difference.
- Print to the console.
- Note: still working on how to make the last row to be taken into the computation loop.
- Note: currently the loop does not take the last row into the computation.


## PyPoll
For this analysis three functions have been implemented (note: only two are used)
1. Find total number of votes
2. Create a list of candidates
3. Analyze the votes results per candidate
Below is the current documentation for each function:
All functions use global variable "path" to pass the file path.

### Define a function to count total number of months.
### def find_votes_total(path)
- This function takes the path variable defined outside the function as an input.
- Also uses an output_file variable to specify the path and the file name for the outputs.
- Using list comprehension, count the total number of rows and output the results as Total Votes.

### def create_candidates_list
### (not used in the final analysis, for testing only)
- This auxiliary function is to create a list with all the candidates in the elections.
- The functino opens provides csv file in read mode
- Iterates through the csv_reader_object to check if candidate is already included in the list of candidates.
- If candidate is not yet in the list, then add it. Otherwise, continue the loop

### def analyze_votes_per_candidates
- The function takes two parameters as input - input file path and output file path and name of the file.
- Open file in read mode.
- Initialize rows_num - total number of rows in the csv file
- Initialize list_of_candidates list as empty
- Iterate through the file and add the candidate to the list of candidates, if not present yet.
- While iteraring also count the number of rows for the percentage calculation.
- User the Counter method to create a dictionary with candidates and their accumulated votes.
- Use max() method on the list of candidates to find the candidate with the maximum votes.
- Using list comprehension, create a new list with candidates with the maximum votes
- Print formatted results to the console and to the text file.
    