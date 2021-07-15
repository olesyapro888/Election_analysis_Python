# ELECTION_ANALYSIS
## `-Indice-`

- [Overview of Election Audit](#Overview-of-Election-Audit)
- [Resources](#resources)
- [Election-Audit Results](#Election-Audit-Results)
  - [Candidate Results](#candidate-results)
  - [County vote Results](#county-vote-results)
  - [The Election winner and the largest county turnout](#the-election-winner-and)
- [Election-Audit Summary](#Election-Audit-Summary)

## `Overview of Election Audit`

A Colorado Board of Elections employee has given me the folLowing tasks to complete the election audit of a recent local congressional election.

The election commission has requested following data to complete the audit:

1. Calculate the total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout
## `Resources`
The audit was created using next resources:
  - Data Source: election_results.csv which be found in the [Resources](./Resources/election_results.csv)
  - Software: Python 3.9.6, Visual Studio Code 1.58.0
## `Election-Audit Results`

Full audit results can be found in the [Analysis](./Analysis/election_analysis.txt) folder.

The election analysis shows 369,711 total votes.
### `Candidate Results`

The Candidates were:
  - Charles Casper Stockham;
  - Diana DeGette;
  - Raymon Anthony Doane.

The Candidate results were:
  - Charles Casper Stockham received 23% of the votes and 85,213 votes;
  - Diana DeGette received 73.8% of the votes and 272,892 votes;
  - Raymon Anthony Doane received 3.1% of the and with 11,606 votes.
### `County vote results`

The Counties were:
  - Denver;
  - Jefferson;
  - Arapahoe.

The County vote results were:
  - Jefferson County received 10.5% of the votes with 38,855 votes;
  - Denver County received 82.8% of the votes with 306,055 votes;
  - Arapahoe County received 6.7% of the votes with 24,801 votes.

### `The election winner and the largest county turnout`

The winner of the election:
  - Diana DeGette, who received 73.8% of the votes and 272,892 number of votes;

The county with the largest voter turnout:
  - Denver county, who received 82.8% of the votes with 306,055 votes.
## `Election-Audit Summary`

This script could be used for any election with some easy script modification and additional data.

For instance, with added data it can be used to get result of budget, age, sex of candidates and so on. To analyse "budget" modification is place of counties by changing the index and renaming related variable. The change should be here:

![Other]("screen_code1")

Additionally, the script can be modified to select winner candidates in each county. A pseudocode of modification can be following: loop through counties and candidates with condition such as: if the most popular candidate in a county  then add to a new dictionary of county with candidate. Then, print results or print a winner as the most popular candidate in county by comparing elements of dictionary. The code should be modified in part of loop with condition in the attached screen:

![Other]("screen_code2")

and here modified or aded:

![Other]("screen_code3")