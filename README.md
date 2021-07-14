# ELECTION_ANALYSIS
## `-Indice-`

- [Overview of Election Audit](#Overview-of-Election-Audit)
- [Resources](#resources)
- [Election-Audit Results](#Election-Audit-Results)
  - [Vote Summary](#there-were-"x"-votes-cast)
  - [Candidate Summary](#the-candidates-were)
   - [Candidate Results](#the-candidate-results-were)
   - [Election Winner](#the-winner-of-the-election-was)
- [Election-Audit Summary](#Election-Audit-Summary)

## `Overview of Election Audit`

Explain the purpose of this election audit analysis. 

A Colorado Board of Elections employee has given me the folLowing tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout
## `Resources`
  - Data Source: election_results.csv
  - Software: Python 3.9.6, Visual Studio Code 1.58.0
## `Election-Audit Results`
Using a bulleted list, address the following election outcomes

The election analysis performs following:
  ### - There were "x" votes cast in the election
How many votes were cast in this congressional election?
Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

There were 369,711 votes cast in the 'Analysis' folder.

• The counties were:
  - Denver
  - Jefferson
  - Arapahoe

• The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
  ### - The election results were:
•	The Candidate results were:
  - Charles Casper Stockham received 23% of the votes and 85,213 votes
  - Diana DeGette received 73.8% of the votes and 272,892 votes
  - Raymon Anthony Doane received 3.1% of the and with 11,606 votes
    
•	The county votes results were:
  - Jefferson County received 10.5% of the votes with 38,855 votes
  - Denver County received 82.8% of the votes with 306,055 votes
  - Arapahoe County received 6.7% of the votes with 24,801 votes

  ### - The winner of the election was:
  Candidate (1,2,3), who received "x%" of the vote and "y" number of votes.
•	The winner of the election:
  - Diana DeGette, who received 73.8% of the votes with 272,892 votes,
•	The county with the largest voter turnout:
  - Denver county, who received 82.8% of the votes with 306,055 votes.

## `Election-Audit Summary`
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. 
Give at least two examples of how this script can be modified to be used for other elections.

 This script could be used for any election such as: who is candidate winner for each county. 

Firstly, to use the code for any election with some easy script modification and additional data. 

For instance, with some added data it can be used to get result of budget, age, sex of candidates and so on. To analyse "budget" modification is place of counties by changing the index and renaming related variable:

screen of code1

Additionally, the script can be modified to select winner candidates in each county. For instance, 

calculate largest candidate for each country

screen of code2