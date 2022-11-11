import os
import csv

csvpath = os.path.join("..", "Resources/election_data.csv")

#starting values
vote_total = 0
most_votes_count = 0
most_votes_candidate = " "

#define list
candidates_list = {}

#path

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    
    for row in csvreader:
    
#count
        
        candidate_name = row[2]

        vote_total = vote_total + 1
        
        if candidate_name in candidates_list:
             candidates_list[candidate_name] = candidates_list[candidate_name] + 1
        else:
             candidates_list[candidate_name] = 1

    # for debuging print(candidates)


#Print the final results        

with open('election_analysis.txt', 'w') as election_analysis:
    print ("\n" + "Election Results")
    print('-----------------------------------------------' + "\n")
    output = ("Total Votes: " + str(vote_total) + "\n")
    print(output)
    election_analysis.write(output)
    print("-----------------------------------------------" + "\n")
 
  #analysis of the results and finding the winner

    for candidate_name,  candidate_votes in candidates_list.items():
         if candidate_votes > most_votes_count:
            most_votes_candidate = candidate_name
            most_votes_count = candidate_votes
            candidates_percent = round((candidate_votes/vote_total)*100,3)
        
 #Export results to a text file    
            output = candidate_name + ":" + str(candidates_percent) + '% ' + '(' + str(candidate_votes) + ')'
            print(output)
            election_analysis.write(output + '\n')
  

    print(f"----------------------------------------\nWinner: {most_votes_candidate}\n----------------------------------------" + '\n')
    election_analysis.write(f'----------------------------------------\nWinner: {most_votes_candidate}\n----------------------------------------' + "\n")