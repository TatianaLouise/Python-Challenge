# Import os to create file paths across operating systems

import os

import csv

election_csv = os.path.join("Resources", "election_data.csv")

election_csv

# Import and read into election_csv

with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter = ",")
    

# Use next(csv_reader, None) to skip the header row

    next(election_reader, None)

# Define the function and have it accept the 'election_results' as it's sole parameter
# Assign values to variables

def print_election_results(election_results):
    
#Create lists to store ballots, candidate names, votes per candidate
# Initialize vote count

    votes_per_candidate = [0,0,0]

    candidate_list = []

    vote_percentages = []

    print_results = []

    total_votes = 0

    # Add the candidates to the candidate_list


    for row in election_results:
        # Create a complete list of candidates who received votes
        # If the name does not exist in the candidate list, add the name in current row

        candidate_name = row[2]
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
       
       #Find the candidate position in the list        
        candidate_position = candidate_list.index(candidate_name)
        
       # Increment number of votes for the candidate by 1 to find the total number of votes per candidate
        votes_per_candidate[candidate_position] += 1
      
        # Retrieve the total number of votes and add to list

        total_votes += 1

    # The percentage of votes each candidate won
    for votes in votes_per_candidate:

        percent_per_candidate = round(((votes / total_votes) *100), 3)
        vote_percentages.append(percent_per_candidate)

    # Find the index of the max votes_per candidate in order to find the winner
    winner_position = vote_percentages.index(max(vote_percentages))
    winner = candidate_list[winner_position]


    # The winner of the election based on popular vote

    print_results.append("Election results")

    print_results.append("---------------")

    print_results.append("Total Votes: " + str(total_votes))

    print_results.append("---------------")

    for i, candidate in enumerate(candidate_list):

        print_results.append(candidate + ": " + " %"  + str(vote_percentages[i]) + " (" +  str(votes_per_candidate[i]) + ") ")
    
    print_results.append("--------------")
    
    print_results.append("Winner: "  + winner)

    print_results.append("--------------")

    return print_results

# Import and read into election_csv

with open(election_csv) as csvfile:
    election_reader = csv.reader(csvfile, delimiter = ",")
    

# Use next(csv_reader, None) to skip the header row

    next(election_reader, None)

    print_results = print_election_results(election_reader)

    for txt in print_results:
        print(txt) 


output_path = os.path.join('Analysis', 'election_results.txt')

with open(output_path, 'w') as file:

    csvwriter = csv.writer(file, delimiter = ",")

    for txt in print_results:

      csvwriter.writerow([txt])