# This could is created produce the following
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# The below comments relate to the 1 - 5 products that are produced.

#Open the data file.
# Add our dependencies.
import csv
import os

#Assign a variable to load a file for a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. The total number of votes cast
#1. Initialize a total vote counter.
total_votes = 0

#2. A complete list of all the candidates.
candidate_options = []

#3. Create a dictonary to hold the candidate options and thier count of votes.
candidate_votes = {}

#4. Determine winning candidate along with winning count and percentage
#4. initiate variables for winning candidate, winning count and winning percentage
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
        #1. Add to the total vote count.
        total_votes += 1
        
        #2, Print the candidate name from each row
        candidate_name = row[2]

        #2. If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            #2. Add it to the list of candidates
            candidate_options.append(candidate_name)

            #3. Begin tacking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        #3. Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

#ASave the results to our text file.
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #4. Determine the percentage of votes for each candidate by looping through
    #4. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #4. Retrieve vote count of candidate.
        votes = candidate_votes[candidate_name]
            
        #4. Calcualte the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        #4. Print the candidaate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")

        #5. Determine winning vote count and candidate
        #5. Determine if the votes are greater that the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #5 if ture then set winning_count = votes and wining_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Print each candidate, their voter count, and the percentage to the terminal.
        candidate_results = (f" {candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #5. Print(winning_candidate_summary)
    print(winning_candidate_summary)
         
    #5. Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)