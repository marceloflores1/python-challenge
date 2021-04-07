import os
import csv

electiondata_csv = os.path.join('Resources','election_data.csv')

with open(electiondata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    election_dict = {}
    candidate_dict = {}
    for row in csvreader:
        election_dict[row[0]] = (row[2])
        candidate_dict[row[2]] = 0
    for candidate in election_dict.values():
        candidate_dict[(candidate)] += 1

print('Election Results')
print('----------------------------')
print(f'Total votes: {len(election_dict)}')
print('----------------------------')
for k,v in candidate_dict.items():
    print(f'{k}: {"{:.3f}".format(v/len(election_dict)*100)}% ({v})')
print('----------------------------')
print(f'Winner: {max(candidate_dict, key=candidate_dict.get)}')

f = open("Analysis/election_results.txt", "w")
f.write("Election Results")
f.write("\n----------------------------")    
f.write(f'\nTotal Votes: {len(election_dict)}')
f.write("\n----------------------------")    
for k,v in candidate_dict.items():
    f.write(f'\n{k}: {"{:.3f}".format(v/len(election_dict)*100)}% ({v})')
f.write("\n----------------------------")    
f.write(f'\nWinner: {max(candidate_dict, key=candidate_dict.get)}')    
#END