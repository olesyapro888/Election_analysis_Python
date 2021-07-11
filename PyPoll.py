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

# Initialize a total vote counter.
total_votes = 0
# Declare a new list as Candidate Options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
  txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
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

    # Add to the total vote count.
    total_votes += 1
    # Print the candidate name (3 column as 2 index of row) from each row
    candidate_name = row[2]

    # To get the unique names in the by using "If  not in" the candidate does not match any existing candidate...
    if candidate_name not in candidate_options:
      # Add it to the list of candidates.
      candidate_options.append(candidate_name)
    
    # Setting each candidate's vote count to zero by using format "dictionary_name[key]" to count a value 
      candidate_votes[candidate_name] = 0
  
  # Add a vote to that candidate's count
    candidate_votes[candidate_name] +=1 
  
  # Determine the percentage of votes for each candidate by looping through the counts. # Iterate through the candidate list. 
  for candidate_name in candidate_votes:
   # Retrieve vote count of a candidate by assignign a variable for the value of key to calculate %
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
    # 2. If true then set winning_count = votes and winning_percent =
    # vote_percentage.
      winning_count = votes
      winning_percentage = vote_percentage
    # 3. Set the winning_candidate equal to the candidate's name.
      winning_candidate = candidate_name

  #print(f"{candidate_name}: received {vote_percentage:.3}% of the vote.")
  # Print out each candidate's name, vote count, and percentage of votes to the terminal.
  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
  winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
  print(winning_candidate_summary)

  
# 3. Print the total votes.
#print(total_votes)
# Print the candidate list.
#print(candidate_options)
# Print the candidate vote dictionary.
#print(candidate_votes)
    
