import os
import csv
from datetime import datetime
# import pycountry

path = "employee_data.csv"
output_file = "employee_data_formatted.csv"
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
    }
with open(path, 'r') as csv_file_input:
    csv_reader_object = csv.reader(csv_file_input, delimiter=',')
    csv_header = next(csv_reader_object) # skip the header
    print(csv_header)
    # Rename the header columns
    dictionary = {"Emp ID": [], "First Name": [], "Last Name": [], "DOB": [], "SSN": [], "State": []}
    #dictionary_with_split_names = {"First Name": [], "Last Name": []}
    textFileOutput = open(output_file,"w+")
    textFileOutput.write(f"{csv_header} \n")
    for row in csv_reader_object:
        name = row[1].split(' ')
        first_name, last_name = name[0], name[1]
        #print(last_name)
        employee_id = row[0]
        dictionary["Emp ID"].append(employee_id)
        dictionary["First Name"].append(first_name)
        dictionary["Last Name"].append(last_name)
        date_of_birth = row[2]
        dob_strip = date_of_birth.split('-')
        dob_day = dob_strip[2]
        dob_month = dob_strip[1]
        dob_year = dob_strip[0]
        dob_reversed = (dob_month + '/' + dob_day + '/' + dob_year)
        dob_new = datetime.strptime(dob_reversed, '%m/%d/%Y')
        dictionary["DOB"].append(dob_new)
        ssn_split = row[3].split('-')
        ssn0 = ssn_split[0]
        ssn1 = ssn_split[1]
        ssn2 = ssn_split[2]
        ssn0_new = "***"
        ssn1_new = "**"
        ssn_new = (ssn0_new + '-' + ssn1_new + '-' + ssn2)
        dictionary["SSN"].append(ssn_new)
        state = row[4]
        #print(state_new)
        dictionary["State"].append(state)
        string = (employee_id + ', ' + first_name + ', ' + last_name + ', ' + str(dob_reversed) + ', ' + ssn_new + ', ' + state)
        textFileOutput.write(f"{string} \n")
        print(string)
        
    # textFileOutput.write(dictionary)
    # textFileOutput.close()


