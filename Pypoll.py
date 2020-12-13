import csv
import os
#assign a variable for the file to load and the path
file_to_load =os.path.join("Resources","election_results.csv")

#open the election results and read the file
with open(file_to_load) as election_data:

    #to do: perform analysis.
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)


#close the file.

