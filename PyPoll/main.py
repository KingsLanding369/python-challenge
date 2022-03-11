import os
import csv

pollData = os.path.join(".","Resources","election_data.csv")

# Open the CSV file
with open(pollData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # The total number of votes:
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # List of candidates who received votes:
    candidatelist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candidatelist: 
            candidatelist.append(candidate)
    candidatecount = len(candidatelist)

  # Number of votes each candidate & the percentage of votes for each candidate:
    votes = list()
    percentage = list()
    for j in range (0,candidatecount):
        name = candidatelist[j]
        votes.append(tally.count(name))
        vote_percentage = votes[j]/row_count
        percentage.append(vote_percentage)

  # The winner of the election based on number of votes:
    winner = votes.index(max(votes))    

  # Print the results to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candidatecount): 
        print(f"{candidatelist[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidatelist[winner]}")
    print("----------------------------")

  # Print the results to "PyPoll.txt" file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for k in range (0,candidatecount): 
        print(f"{candidatelist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candidatelist[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))