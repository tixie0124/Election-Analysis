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

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

#save the results to our txt file.
with open(file_to_save,"w") as txt_file:

    #print the final vote count to the terimal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"---------------------\n")
    print(election_results, end= "")
    txt_file.write(election_results)

    #to calculate the percetage of votes each candidate received
    for candidate_name in candidate_votes:

        #to retrieve vote count for each candidate
        votes = candidate_votes[candidate_name]

        # calculate the percentage of votes.
        vote_percentage = (votes / total_votes) * 100

        # print the candidate name and the percentage of votes

       #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

       #print each candidate's result and percentages to the txt file
        print(candidate_results)

        txt_file.write(candidate_results)

# determine winning vote count and candidate

#1.determine if the votes are greater than the winning count.

        if(votes>winning_count) and (vote_percentage>winning_percentage):

         #2.if true then set the winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #set the winning_candidate to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")

    txt_file.write(winning_candidate_summary)
#close the file.

