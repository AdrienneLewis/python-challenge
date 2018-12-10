import os
import csv

print("Election Results: ")


#define file path
pollcsv = os.path.join("..", "..", "..", "Desktop", "election_data.csv")

#create lists
Votes = [] #list of voter ids for all votes cast
VotesList = []  #list of all names cast as votes
Candidates = ["Khan", "Correy", "Li", "O'Tooley"] #list of candidates extracted from voteslist
Candidate1 = "Khan"
Candidate2 = "Correy"
Candidate3 = "Li"
Candidate4 = "O'Tooley"
Candidate1voters = []
Candidate2voters = []
Candidate3voters = []
Candidate4voters = []

#Find total Votes
with open(pollcsv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)
    for row in csvreader:
        Votes.append(row[0])
        VotesList.append(row[2])
    for i in range(len(VotesList) -1):
        if VotesList[i] == Candidate1:
            Candidate1voters.append(row[0])
    for i in range(len(VotesList) -1):
        if VotesList[i] == Candidate2:
            Candidate2voters.append(row[0])
    for i in range(len(VotesList) -1):
        if VotesList[i] == Candidate3:
            Candidate3voters.append(row[0])
    for i in range(len(VotesList) -1):
        if VotesList[i] == Candidate4:
            Candidate4voters.append(row[0])


avgVotes1 = int(len(Candidate1voters) / len(Votes) * 100)
avgVotes2 = int(len(Candidate2voters) / len(Votes) * 100)
avgVotes3 = int(len(Candidate3voters) / len(Votes) * 100)
avgVotes4 = int(len(Candidate4voters) / len(Votes) * 100)



print("Total Votes: " + str(len(Votes)))
print(f"Khan:      {avgVotes1}%    ({len(Candidate1voters)})")
print(f"Correy:    {avgVotes2}%    ({len(Candidate2voters)})")
print(f"Li:        {avgVotes3}%    ({len(Candidate3voters)})")
print(f"O'Tooley:  {avgVotes4}%    ({len(Candidate4voters)})") 

print("The Winner is Khan")

averages = [avgVotes1, avgVotes2, avgVotes3, avgVotes4]
Votescount = [len(Candidate1voters), len(Candidate2voters), len(Candidate3voters), len(Candidate4voters)]


Election_Results = zip(Candidates, averages, Votescount)

# Set variable for output file
outputfile = os.path.join("election_results.txt")

#  Open the output file
with open(outputfile, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Candidates", "PercentVote", "CountVotes"])

    # Write in zipped rows
    writer.writerows(Election_Results)
