#this is main.py for PyPoll

#main code for Homework 3 - PyPoll Activity

import csv
import os

csvpath = os.path.join("Resources", "election_data.csv")

#initialize variables
voteKhan = 0
voteCorrey = 0
voteLi = 0
voteTooley = 0
totalVotes = 0 

with open(csvpath, newline="") as csvfile:

    #identify how the data is broken up in csv
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csvHeader=next(csvreader)

    for row in csvreader:
        #tally the number of votes
        totalVotes += 1

        #tally who the vote goes to
        if row[2]=="Khan":
            voteKhan += 1

        elif row[2]=="Correy":
            voteCorrey += 1

        elif row[2]=="Li":
            voteLi += 1
        
        elif row[2]=="O'Tooley":
            voteTooley +=1

        else:
            #if they voted for none of the 4 candidates
            pass

    #calculate the percent of votes for each candidate
    #covert to float with 3 decimal places
    percentKhan = (voteKhan / totalVotes)*100
    percentKhan = "{0:.3f}".format(percentKhan)

    percentCorrey = (voteCorrey / totalVotes)*100
    percentCorrey = "{0:.3f}".format(percentCorrey)

    percentLi = (voteLi / totalVotes)*100
    percentLi = "{0:.3f}".format(percentLi)

    percentTooley = (voteTooley / totalVotes)*100
    percentTooley = "{0:.3f}".format(percentTooley)

#determine the winner by popular vote
if voteKhan > voteCorrey and voteKhan > voteCorrey and voteKhan > voteLi and voteKhan > voteTooley:
    winner = "Khan"
elif voteCorrey > voteLi and voteCorrey > voteTooley:
    winner = "Correy"
elif voteLi > voteTooley:
    winner = "Li"
else:
    winner = "O'Tooley"

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------------")
print(f"Khan: {percentKhan}% ({voteKhan})")
print(f"Correy: {percentCorrey}% ({voteCorrey})")
print(f"Li: {percentLi}% ({voteLi})")
print(f"O'Tooley: {percentTooley}% ({voteTooley})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#create a txt file with the printed information
file = open("pypollStore.txt", "w")

textlist = ["Election Results",
    "-------------------------------",
    "Total Votes: {totalVotes}",
    "-------------------------------",
    "Khan: {percentKhan}% ({voteKhan})",
    "Correy: {percentCorrey}% ({voteCorrey})",
    "Li: {percentLi}% ({voteLi})",
    "O'Tooley: {percentTooley}% ({voteTooley})",
    "-------------------------------",
    "Winner: {winner}",
    "-------------------------------"
    ]

for line in textlist:
    file.write(line)
    file.write("\n")
file.close()