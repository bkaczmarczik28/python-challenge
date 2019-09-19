#this is the main.py for PyBoss

import csv
import os

#create a new csv file
with open("modified_employee_data.csv", 'w') as exportData:
    #initialize csv.writer, to start creating new file
    csvwriter = csv.writer(exportData, delimiter=',')
    #write the header for the new csv file
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN","State"])

#access employee data
csvpath = os.path.join("employee_data.csv")

#function that splits the full name into first name and last name
#CHECKED - FUNCTION WORKS
def splitName(name):
    firstName=name.split()[0]
    lastName=name.split()[1]
    return firstName, lastName

#function that edits the DOB to new format
#CHECKED - FUNCTION WORKS
def editDOB(DOB):
    year=DOB.split('-')[0]
    month=DOB.split('-')[1]
    day=DOB.split('-')[2]

    newDOB=month+"/"+day+'/'+year
    return newDOB

#function that secures full SSN
#CHECKED - FUNCTION WORKS
def editSSN(SSN):
    last4Digits=SSN.split('-')[2]
    newSSN="***-**-"+last4Digits
    return newSSN

#function that takes the full state name and abbreviates it
#CHECKED - FUNCTION WORKS
def abbrevState(inputState):
    us_states_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
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
    'Palau': 'PW',
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
    'Wyoming': 'WY',
    }
    
    abbrevState = us_states_abbrev[inputState]
   
    return abbrevState

with open(csvpath, newline="") as csvfile:

    #read data
    csvreader=csv.reader(csvfile, delimiter=",")
    #skip heaer
    cvsHeader=next(csvreader)

    #iterate for each row of data
    for row in csvreader:

        #intialize the data in the row
        EmpID=row[0]
        fullName=row[1]
        DOB=row[2]
        SSN=row[3]
        state=row[4]
       
        #call functions that rewrite the data in each row
        firstName, lastName=splitName(fullName)

        newDOB=editDOB(DOB)
    
        newSSN=editSSN(SSN)
    
        newState=abbrevState(state)
    
        #write the altered data into the new csv file
        #the "a" will append the data. If you use "w" it will write over the data
        with open("modified_employee_data.csv", 'a') as exportData:
            #initialize csv.writer, to start creating new file
            csvwriter = csv.writer(exportData, delimiter=',')
            #write the header for the new csv file
            csvwriter.writerow([EmpID, firstName, lastName, DOB, SSN, newState])

    