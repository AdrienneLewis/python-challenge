import os
import csv

print("Financial Analysis:")

#define file path
bankcsv = os.path.join("..", "..", "..", "Desktop", "budget_data.csv")

#create lists
Months = []
Profits = []
AvgChange = []



#Find total months
with open(bankcsv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    for row in csvreader:
        Months.append(row[0])
    

with open(bankcsv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    #Loop through profits column and find total profits
    for row in csvreader:
        Profits.append(int(row[1]))
   

    #Loop through profits and find changes, subtract profits for previous month from next month
    for i in range(len(Profits) -1):
        AvgChange.append(Profits[i + 1] - Profits[i])


print("Total Months: " + str(len(Months)))   
print(f"Total: {sum(Profits)}")     
print(f"Average Change:   {sum(AvgChange) / len(AvgChange)}")
print(f"Greatest Decrease in Profits:  {min(AvgChange)}")
print(f"Greatest Increase in Profits: {max(AvgChange)}")

Total_Months= str(len(Months))
Total = str(sum(Profits))
Avg_Change = str(sum(AvgChange) / len(AvgChange))
Greatest_Inc = str(min(AvgChange))
Greatest_Dec = str(max(AvgChange))


financial_analysis = zip(Total_Months, Total, Avg_Change, Greatest_Inc, Greatest_Dec)

# Set variable for output file
outputfile = os.path.join("financial_anaylsis.txt")

#  Open the output file
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total Months", "Profits", "Average Change", "Greatest Decrease",
                     "Greatest Decrease"])

    # Write in zipped rows
    writer.writerows(financial_analysis)


      

        


       

