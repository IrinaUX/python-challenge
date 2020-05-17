import os
import csv
#import itertools
#import pandas as pd
from collections import defaultdict

def findTotalNumberOfMonths(folder, file):
    path=os.path.join(folder, file)
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


def findRevenueTotal(folder, file):
    path=os.path.join(folder, file)
    #print(path)

# PyBank * Your task is to create a Python script that analyzes the records to calculate each of the following:

# PyBank 1 - The total number of months included in the dataset


    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        # print(csv_reader_object)
        # csv_output_object = csv.writer(file_output)
        # csv_output_object.write(file_output)

        # PyBank 2 - The net total amount of "Profit/Losses" over the entire period
        
        next(csv_reader_object)
        profit_list = []
        for value in csv_reader_object:
            profit_list.append(int(value[1]))
        total_profit_and_loss = round(sum(profit_list))
        print(f"Total profit and loss: {total_profit_and_loss}")

        # Write to a new file:
        textFileOutput = open("output.txt","a+")
        textFileOutput.write(f"Total $: {total_profit_and_loss} \n")
        
    

    #     # Convert reader to the list
    # data = list(csv_reader_object)
    # total_revenue = 0
    # amount1 = 0
    # amount2 = 0
    # for row in data:
    #     revenue = eval(row[1])
    #     total_revenue += revenue
    #     amount2 = revenue
    #     print(amount2)
    
    # first_row = next(csv_reader_object)
    # first_value = int(first_row[1])
    # print(first_value)
    # profit = []
    # for row in csv_reader_object:
    #     change = int(row[1] - first_value)
    #     profit.append(change)
    #     value = int(row[1])

    # totalList = []
    # for row in csv_reader_object:
    #     totalList.append(int(row[1]))
    # textFileOutput.write(f"Total: ${totalList} \n")
    # #print(totalList)
    # print("Total: " + "$" + str(sum(totalList)))

    # for row in csv_reader_object:
    #     content = list(row[i] for i in included_cols)
    #     print(content)

    # for line in file_input.readline():
    #     array = line.split(',')
    #     second_column = array[1]
    #     print(second_column)

    # for row in csv_reader_object:
    #     rowtotal = 0
    #     for column in row[1]:
    #         rowtotal += int(column)
    #     print(row[1], rowtotal)
    
    # # Add values from column 2 (index 1) using list comprehension
    # total = 340340340
    # print(f"The data type of total profit is {type(total)}.")
    # column2_sum = (sum(csv_reader_object[1] for _ in iterRows[1]))
    # print(column2_sum)
        textFileOutput.close()

        # Try to read index directly without extracting the column to a list
    #csvreader = csv.reader(path,delimiter=',')
    ##for lines in csvreader:
      #  print(lines[1])

        # Try to make a list of all the values in column "Profit/Losses" (index[1])
    # colProfitLosses =[]
# def running_total(a):
#     total = 0
#     for item in a:
#         total += item
#         yield total
# running_total()
    #csv_reader_object = csv.reader(file)
    # total = sum(int([x]) for _ in iterRows[1])

    # print(list(itertools.accumulate(csv_reader_object)))
    # print(sum(float(r['Profit/Losses']) for r in csv_reader_object))
    # print([x+x for x in csv_reader_object])
    # has_header = csv.Sniffer().has_header(file.read(1024))
    # file.seek(0)
    # csv_reader_object = csv.reader(file)
    # print(sum(int(x[1]) for x in csv_reader_object))
    # if has_header:
    #     next(csv_reader_object)
    #     #for row in csv_reader_object:
            #print("CSV row: {0}".format(row))
            #print(type({1}))
    #csv_reader_object.line_num
    #csvreader=csv.reader(path,delimiter=',')
    #csvheader = next(csv_reader_object)
    #header = next(csvreader) # skip the header
    #linesWithoutHeader = csv_reader_object.line_num - 1
    #print(f"Total number of months (rows) is {str(linesWithoutHeader)}.")
# PyBank 2 - The net total amount of "Profit/Losses" over the entire period

    # total = sum(long(row["Profit/Losses"]) for row in csv_reader_object)
    # print(total)
    # column = 1
    # print(type(csv_reader_object))
# def file_len(path):
#     with open(path) as f:
#         for i in enumerate(f):
#             # pass
#             #print(i)
#             return i + 1

# file_len(path)
# print(file_len(path))

# with open(path, 'r') as text:
#     print(text)
#     text = text.read()
#     #print(text)
#     lst = []
#     for row in text:
#         #print("text line number: " + row)
#         lst.append(row)
#     #print(lst)


# with open(path, 'r') as filehandler:
#     # lines=filehandler.read()
#     # print(lines)
#     # print(type(lines))
#     # filehandler.read()
#     csvreader=csv.reader(path,delimiter=',')
#     #print(csvreader)
#     csvheader = next(csvreader)
#     print(csvheader)
#     print(f"csv header: {csvheader}")
# # Find the total number of months included in the dataset
#     data = list(csvreader)
#     rowcount = len(data)
#     print(rowcount)

findTotalNumberOfMonths("Resources","budget_data.csv")
findRevenueTotal("Resources","budget_data.csv")
