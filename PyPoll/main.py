#Importing libraries
import os
import csv

#Filepath
electiondata_csv = os.path.join('Resources','election_data.csv')

#Read csv file
with open(electiondata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    election_dict = {}
    candidate_dict = {}
#Loop csvfile for election_dict, this will have voter ids as keys and candidates as values
    for row in csvreader:
        election_dict[row[0]] = (row[2])
        candidate_dict[row[2]] = 0
#Loop election_dict for candidate_dict, this will have candidates as keys and vote count as values
    for candidate in election_dict.values():
        candidate_dict[(candidate)] += 1

#Printing results in terminal
print('Election Results')
print('----------------------------')
print(f'Total votes: {len(election_dict)}') #election_dict has all the votes so the lenght is the total votes
print('----------------------------')
for k,v in candidate_dict.items(): #loop to print informtation for every candidate
    print(f'{k}: {"{:.3f}".format(v/len(election_dict)*100)}% ({v})') #the % of votes = the value for every candidate which represented vote count and divide by the total votes, with some formatting to get percentage as desired
print('----------------------------')
print(f'Winner: {max(candidate_dict, key=candidate_dict.get)}') #to determine the winner we get the max value of candidate_dict which has the votecount as value for every candidate, after we get the Key that has the Candidate

#Printing the same results by exporting to txt file
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