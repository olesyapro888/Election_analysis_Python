# The data need to retrieve.
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.

  # direct path to the file
# file_to_load = "Resources/election_results.csv"

  # indirect path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
  #election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

  # To do: perform analysis.
  print(election_data)

# Close the file.
#election_data.close() (changed with)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
