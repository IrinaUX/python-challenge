import os
import csv
from collections import Counter
from collections import OrderedDict 

# Set the file path
path=os.path.join("Resources","election_data.csv")
#output_path = "analysis"
output_file = "analysis/output.txt"
candidates_list = []
#rows_num = 0
# Define a function to count total number of months.


def find_votes_total(path):
    '''
    This function takes the path variable defined outside the function as an input.
    Also uses an output_file variable to specify the path and the file name for the outputs.
    Using list comprehension, count the total number of rows and output the results as Total Votes.
    '''
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        #csv_reader_object = csv.reader(file_input, delimiter=',')
        iterRows = iter(file_input)
        next(iterRows)
        rows_num = (sum(1 for _ in iterRows))
        print("Election Results")
        print("--------------------------")
        print(f"Total Votes: {rows_num}")
        print("--------------------------")
        # Write results to the output.txt file in analysis folder
        textFileOutput = open(output_file,"w+")
        textFileOutput.write("Election Results \n")
        textFileOutput.write("--------------------------- \n")
        textFileOutput.write(f"Total Votes: {rows_num} \n")
        textFileOutput.write("--------------------------- \n")
        textFileOutput.close()
    #print(rows_num)
    return rows_num 

def create_candidates_list(path, output_file):
    '''
    This auxiliary function is to create a list with all the candidates in the elections.
    The functino opens provides csv file in read mode
    Iterates through the csv_reader_object to check if candidate is already included in the list of candidates.
    If candidate is not yet in the list, then add it. Otherwise, continue the loop
    '''
    # candidates_list = [] # moved to global variables
    #candidates = collections.Counter()
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object) # to skip the header
        for row in csv_reader_object:
            candidate = str(row[2])
            if candidate not in candidates_list:
                candidates_list.append(candidate)
        return(candidates_list)

def find_candidate_with_maximum_votes(path, output_file):
    '''
    The function takes two parameters as input - input file path and output file path and name of the file.
    Open file in read mode.
    Initialize rows_num - total number of rows in the csv file
    Initialize list_of_candidates list as empty
    Iterate through the file and add the candidate to the list of candidates, if not present yet.
    While iteraring also count the number of rows for the percentage calculation.
    User the Counter method to create a dictionary with candidates and their accumulated votes.
    Use max() method on the list of candidates to find the candidate with the maximum votes.
    Using list comprehension, create a new list with candidates with the maximum votes
    Print formatted results to the console and to the text file.
    '''
    with open(path, 'r', newline='') as file_input: # open('output.txt', 'wb') as file_output:
        csv_reader_object = csv.reader(file_input, delimiter=',')
        next(csv_reader_object) # to skip the header
        
        # Create an initialize a new list to store candidates from candidates column
        rows_num = 0
        list_of_candidates = [] 

        # Start for loop to iterate through the csv file
        for value in csv_reader_object:
            list_of_candidates.append(value[2]) # append candidates to the list of candidates
            rows_num += 1 # count running total number of rows
            
        # #list_of_candidates_sorted
        # list_of_candidates_sorted = sorted(list_of_candidates)
        
        # Use Counter method to count the votes:
        vote_count = Counter(list_of_candidates) # Counter summarized the list with votes into a dictionary
        vote_count_sorted = vote_count.most_common() # use most common method to sort the dictionary based on the key value
        
        # Open the text file to write the output results
        textFileOutput = open(output_file,"a+")
        
        # Start a for loop over the list of candidates sorted by their votes.
        # Calculate the percentage and output in the console and the text file
        for i in range(len(vote_count_sorted)):
            candidate_percentage = round((((vote_count_sorted[i][1]) / rows_num) * 100), 3)
            print(f"{vote_count_sorted[i][0]}: {candidate_percentage}% ({vote_count_sorted[i][1]})")
            textFileOutput.write(f"{vote_count_sorted[i][0]}: {candidate_percentage}% ({vote_count_sorted[i][1]}) \n")
        
        # Find the maximum number of votes:
        max_votes = max(vote_count.values())
        
        # Use list comprehension method to create a list with the candidates with max votes (in case votes count is the same for several candidates)
        list_of_candidates_with_max_votes = [i for i in vote_count.keys() if vote_count[i] == max_votes]
        
        # Print to the console:
        print("--------------------------")
        print(f"Winner: {list_of_candidates_with_max_votes[0]}")
        print("--------------------------")
        
        # Output to the file:
        textFileOutput.write("--------------------------- \n")
        textFileOutput.write(f"Winner: {list_of_candidates_with_max_votes[0]} \n")
        textFileOutput.write("--------------------------- \n")
        textFileOutput.close()



# Call the functions to perform elections result analysis:

find_votes_total(path)
create_candidates_list(path, output_file)
find_candidate_with_maximum_votes(path, output_file)