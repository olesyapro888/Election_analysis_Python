# The data need to retrieve.
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

# Add our dependencies (modules)
import csv
import os

# Assign a variable for the file to load from a path.

  # direct path to the file
# file_to_load = "Resources/election_results.csv"

  # indirect path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Declare a new list as Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
  txt_file.write("Counties in the Election\n________________________\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()
# Open the election results and read the file.
  #election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

# To do: perform analysis.
#print(election_data)
# Close the file. #election_data.close()

# Read the file object with the reader function.
  file_reader = csv.reader(election_data)
  
  # Read (and print) the header row.
  headers = next(file_reader)
  #print(headers)

  #Print each row in the CSV file.
  for row in file_reader:
    #print(row)
    # 2. Add to the total vote count.
    total_votes += 1
    # Print the candidate name from each row
    candidate_name = row[2]

    # If the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
      # Add it to the list of candidates.
      candidate_options.append(candidate_name)
    # Begin tracking that candidate's vote count Setting each candidate's vote count to zero.
      candidate_votes[candidate_name] = 0
  
# 3. Print the total votes.
#print(total_votes)
# Print the candidate list.
print(candidate_options)