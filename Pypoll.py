import csv
import os
#assign a variable for the file to load and the path
file_to_load =os.path.join("Resources","election_results.csv")

#assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#adding a new column to reference candidate name
candidate_options = []

#create a dictionary to store dandicate vote counts

candidate_votes = {}

#open the election results and read the file
with open(file_to_load) as election_data:

    #to do: perform analysis.
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
   
   #print each row in the CSV file
    for row in file_reader:
       #add to the total voter counter
       total_votes += 1

       #print the candidate name from each for
       candidate_name = row[2]

       #if the candidate name does not match any existing candidate

       if candidate_name not in candidate_options:

           #add it to the list of candidates

            candidate_options.append(candidate_name)


               #creat a key to track the vote count for each candidate

            candidate_votes[candidate_name] = 0

       #count the number of votes for each candidate name

       candidate_votes[candidate_name] += 1


print(candidate_votes)

#close the file.

