'''
## Option 2: PyPoll

![Vote-Counting](Images/Vote_counting.jpg)

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, 
but unfortunately, his concentration isn't what it used to be.)

You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). 
Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
Your task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:

```
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
```
'''

import csv
import os

#I found this function online... wasn't clever enough to make it myself. But I can use it!
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

#the rest of this is my own!
csvpath = os.path.join("raw_data","election_data_2.csv")

with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)

        totalVotes=0
        candidates=[]

        votes_per_candidate = {}
        for row in csvreader:
            totalVotes=totalVotes+1
            if row[2] not in candidates:
                candidates.append(row[2])
                votes_per_candidate.update({row[2]:1})
            else:
                votes_per_candidate.update({row[2]:votes_per_candidate[row[2]]+1})

            #now just need to add the thing that updates the dictionary values if the candidate IS in the candidate list

        candidate_percentages={}
        for key,value in votes_per_candidate.items():
            candidate_percentages.update({key:str(round(100*value/totalVotes,4))+"%"})
    
    
        Winner=keywithmaxval(votes_per_candidate)

        print()
        print()
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {totalVotes}")
        print("-------------------------")        
        for candidate in candidates:
            print(f"{candidate}: {candidate_percentages[candidate]} ({votes_per_candidate[candidate]})")
        print("-------------------------")  
        print(f"Winner: {Winner}")
        print("-------------------------")  
        print()
