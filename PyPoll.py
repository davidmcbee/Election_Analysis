#Open the data file.
# Add our dependencies.
import csv
import os

#Assign a variable to load a file for a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. The total number of votes cast
#1a. Initialize a total vote counter.
total_votes = 0

#2. A complete list of all the candidates.
candidate_options = []

#3a1 Create a dictonary to hold the candidate options and thier count of votes.
candidate_votes = {}

#4A1 Determine winning candidate along with winning count and percentage
#4a2 initiate variables for winning candidate, winning count and winning percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    headers = next(file_reader)
    
    #Print each row inthe CSV file.
    for row in file_reader:
        #1b. Add to the total vote count.
        total_votes += 1
        
        #2a Print the candidate name from each row
        candidate_name = row[2]

        #2b If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            #2c Add it to the list of candidates
            candidate_options.append(candidate_name)

            #3a2. Begin tacking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        #3a3 Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

    #3b1 Determine the percentage of votes for each candidate by looping through
    #3b2 Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #3b3 Retrieve vote count of candidate.
        votes = candidate_votes[candidate_name]
           
        #3b4 Calcualte the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #3b5 Print the candidaate name and percentage of votes.
       # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")

        #4a3 Determine winning vote count and candidate
            #4a4 Determine if the votes are greater that the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #4a5 if ture then set winning_count = votes and wining_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        
            #4a6 Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # To do: print out the winning candidate, vote count and percentage to
        #terminal
        print(f" {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
#1c. Print the total votes.
#print(total_votes)

#2c Print the candidate list
#print(candidate_options)

#3a4 Print the candidate vote dictionary.
#print(candidate_votes)

#3b1 The percentage of votes each candidate won
#vote_percentage = ()





#print(f" {winning_candidate} won with a {winning_count} count of votes and a winning percentage of {winning_percentage:.1f}%")






#5. The winner of the election based on popular vote