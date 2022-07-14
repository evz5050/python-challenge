# Read in CSV
import os
import csv
csvpath = os.path.join('election_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# calculate Total Votes, candidate totals/percentages and winner
    total_votes = 0
    candidates_unique = []
    candidate_votes = []
    
    for row in csvreader:
        total_votes+=1 
        candidate_name = (row[2])
        if candidate_name in candidates_unique:
            candidate_index = candidates_unique.index(candidate_name)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            candidates_unique.append(candidate_name)
            candidate_votes.append(1)



percentage = []
max_votes = candidate_votes[0]
max_index = 0

for x in range(len(candidates_unique)):
    vote_percentage = round(candidate_votes[x]/total_votes*100, 3)
    percentage.append(vote_percentage)
    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_index = x
election_winner = candidates_unique[max_index] 

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})')
print('-------------------------')
print(f'Winner: {election_winner}')
print('-------------------------')

# Export to txt file
output_file = os.path.join("PyPoll.txt")
with open(output_file, "w+") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("__________________________\n")
    txt_file.write("\n")
    txt_file.write(f'Total Votes: {total_votes}')
    txt_file.write("\n")
    for x in range(len(candidates_unique)):
        txt_file.write(f'{candidates_unique[x]} : {percentage[x]:.3f}% ({candidate_votes[x]})')
        txt_file.write("\n")
    txt_file.write("\n")
    txt_file.write(f'Winner: {election_winner}')