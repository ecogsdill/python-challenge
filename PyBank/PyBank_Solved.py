'''
## Option 1: PyBank

![Revenue](Images/revenue-per-lead.jpg)

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.\
You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). 
Each dataset is composed of two columns: `Date` and `Revenue`. 
(Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The total amount of revenue gained over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period

As an example, your analysis should look similar to the one below:

```
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
```

Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''

import csv
import os


csvpath = os.path.join("raw_data","budget_data_2.csv")

with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)


        months = 0
        RevDiffTotal=0
        lastRevenue=0
        currentRevenue=0
        RevDiff=0
        MaxRevChange=0
        MinRevChange=0
        TotalRevenue=0

        for row in csvreader:
            
            #revenueList.append(row[1])
            months=months+1
            TotalRevenue=float(TotalRevenue)+float(row[1])
            currentRevenue=row[1]
            RevDiff=float(currentRevenue)-float(lastRevenue)
            RevDiffTotal=RevDiffTotal+RevDiff
            lastRevenue=row[1]

            if RevDiff>MaxRevChange:
                MaxRevChange=RevDiff
                MaxRevMonth=row[0]
            if RevDiff<MinRevChange:
                MinRevChange=RevDiff
                MinRevMonth=row[0]

        AvgRevChange = RevDiffTotal/months

        print()
        print()
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {months}")
        print(f"Total Revenue: ${round(TotalRevenue,2)}")
        print(f"Average Revenue Change: ${round(AvgRevChange,2)}")
        print(f"Greatest Increase in Revenue: {MaxRevMonth} ${round(MaxRevChange,2)}")
        print(f"Greatest Decrease in Revenue: {MinRevMonth} ${round(MinRevChange,2)}")
        print()