import os
import csv

path=os.path.join("Resources","budget_data.csv")
#print(path)

# PyBank * Your task is to create a Python script that analyzes the records to calculate each of the following:

# PyBank 1 - The total number of months included in the dataset

with open(path, 'r') as file:
    iterRows = iter(file)
    next(iterRows)
    rowsNum = (sum(1 for _ in iterRows))
    #rowsNumWithoutHeader = rowsNum - 1
    print(f"The budget data is available for total of {rowsNum} months.")
 # PyBank 2 - The net total amount of "Profit/Losses" over the entire period
   
    
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




