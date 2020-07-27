#Open the data file.
# Add our dependencies.
import csv
import os

#Assign a variable to load a file for a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)


 
#1. The total number of votes cast
#2. A complete list of all the candidates.
#3. The percentage of votes each candidate won
# The total votes for each candidate.
#5. The winner of the election based on popular vote.