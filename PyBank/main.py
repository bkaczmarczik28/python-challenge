#this is main.py in PyBank

import csv
import os

#Identify csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#initialize variables
totalMonths=0
totalAmount=0
sumChange=0
profit = 0
loss = 0
previous = 0 

#Open the file using the "write" mode
with open(csvpath, newline="") as csvfile:
   
    #identify how the data is broken up in csv file
    csvreader=csv.reader(csvfile, delimiter=",")
    #skip first header row in csv file
    csvHeader = next(csvreader)

    for row in csvreader:

        #ensure first line is skipped to calculate average change
        if previous != 0:

            if float(row[1])>profit:
                #store greatest profit
                profit = float(row[1])-previous
                profitPeriod = (row[0])
                        
            if float(row[1])<loss:
                #store greatest loss
                loss = float(row[1])-previous
                lossPeriod = (row[0])

            #calculate average of the changes in profit/loss over entire period
            #calculate change from previous month
            change=float(row[1])-previous
            sumChange=sumChange+change

        #exclude from if statement so first row is included

        #track total number of months
        totalMonths=totalMonths+1

        #store the current profit/loss to use for the next iteration
        previous=float(row[1])

        #calculate net total amount
        totalAmount=totalAmount+float(row[1])
    
    #calculate the average of the changes in profit/loss over entire period
    #subtrate 1 to eliminate first month from average
    averageChange = (sumChange)/(totalMonths-1)

    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months: " + str(totalMonths))

    #convert float number to US currency
    totalAmount = '${:,.2f}'.format(totalAmount)
    averageChange = '${:,.2f}'.format(averageChange)
    profit = '${:,.2f}'.format(profit)
    loss='${:,.2f}'.format(loss)

    print("Total: " + str(totalAmount))
    print("Average Change: " + str(averageChange))
    print("Greatest Increase in Profits: (" + profitPeriod + ") " + str(profit))
    print("Greatest Decrease in Profits: (" + lossPeriod + ") " + str(loss))

#create a txt file with the information
file = open("pybankStore.txt", "w")
    
textlist = [f"Financial Analysis",
        f"--------------------------------",
        f"Total Months: {str(totalMonths)}",
        f"Total: {str(totalAmount)}",
        f"Average Change: {str(averageChange)}",
        f"Greatest Increase in Profits: ({profitPeriod}) {str(profit)}",
        f"Greatest Decrease in Profits: ({lossPeriod}) {str(loss)}",
        ]

for line in textlist:
    file.write(line)
    file.write("\n")
file.close()