import os
import csv

path=os.path.join("Resources","budget_data.csv")
#print(path)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

with open(path, 'r') as file:
    csv_reader_object = csv.reader(file)
    for row in csv_reader_object:
        print("CSV row: {0}".format(row))
    #csv_reader_object.line_num
    #csvheader = next(csv_reader_object)
    linesWithoutHeader = csv_reader_object.line_num - 1
    print(f"Total number of months (rows) is {str(linesWithoutHeader)}.")

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





