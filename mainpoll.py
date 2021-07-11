import os
import csv

total_votes = 0
khan_total_votes = 0
correy_total_votes = 0
li_total_votes = 0
otooley_total_votes = 0
candidates = {}

election_csv = os.path.join("Resources", "election_data.csv")

# Iterate through csv to count votes per candidate
with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan_total_votes += 1
        if row[2] == "Correy":
            correy_total_votes += 1
        if row[2] == "Li":
            li_total_votes += 1
        if row[2] == "O'Tooley":
            otooley_total_votes += 1

# Calculating the percent of vote each candidate receives
khan_percent = (khan_total_votes / total_votes) * 100
correy_percent = (correy_total_votes / total_votes) * 100
li_percent = (li_total_votes / total_votes) * 100
otooley_percent = (otooley_total_votes / total_votes) * 100

# Creating dictionary to output the winner
candidates = {"Khan": khan_total_votes, 
                "Correy": correy_total_votes,
                "Li": li_total_votes,
                "O'Tooley": otooley_total_votes
 }
winner = max(candidates, key=candidates.get)
    
#Print results to terminal
print("Election Results")
print("--------------------")
print("Total Votes: " + str(total_votes))
print("--------------------")
print("Khan: {:.3f}".format(khan_percent) + "% (" + str(khan_total_votes) + ")")
print("Correy: {:.3f}".format(correy_percent) + "% (" + str(correy_total_votes) + ")")
print("Li: {:.3f}".format(li_percent) + "% (" + str(li_total_votes)+ ")")
print("O'Tooley: {:.3f}".format(otooley_percent) + "% ("+ str(otooley_total_votes)+ ")")
print("--------------------")
print("Winner: " + winner)
print("--------------------")

# Export analysis to text file 
output_path = os.path.join("analysis", "election_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.writelines(["Election Results \n",
    "--------------------" + "\n",
    "Total Votes: " + str(total_votes) + "\n", 
    "Khan: {:.3f}".format(khan_percent) + "% (" + str(khan_total_votes) + ") \n",
    "Correy: {:.3f}".format(correy_percent) + "% (" + str(correy_total_votes) + ") \n",
    "Li: {:.3f}".format(li_percent) + "% (" + str(li_total_votes)+ ") \n",
    "O'Tooley: {:.3f}".format(otooley_percent) + "% ("+ str(otooley_total_votes)+ ") \n",
    "-------------------- \n",
    "Winner: " + winner + "\n",
    "-------------------- \n"
     ])
txtfile.close()
