# Election_Analysis

## Overview

The purpose of this project was to write a program that could sort through each row of election data and return the desired data points that would declare a winner of the local election. A few of the deliverables include: Who won  the election, the total vote count per county and per candidate, as well as county turnout data. 

## Election-Audit Results: 

  - 369,711 Total Votes Cast 
  
  - County Votes: 
    - Jefferson 10.5% (38,855) 
    - (*largest county turnout*) **Denver: 82.8% (306,055)** 
    - Arapahoe: 6.7% (24,801).
  
  
  - Candidate Votes: 
    - Charles Casper Stockham: 23.0% (85,213), 
    - (*winner*) **Diana DeGette: 73.8% (272,892)**, 
    - Raymon Anthony Doane: 3.1% (11,606)

 <img width="400" alt="Election_Analysis_Winning_Results" src="https://user-images.githubusercontent.com/106042900/174914112-ae83f5bc-5724-4d7c-943b-100c12aea59d.png">


## Election-Audit Summary 

This python script has a few maluable pieces in which new rows can be iterated through for deeper analysis. 

  1. The initial analysis was focused on finding the winning candidate from the election data. I first gather the candidate name, then iterated through each row to tally one vote every time the candidate name was identified. 
```python. 

    candidate_name = row[2] 

    candidate_votes[candidate_name] += 1 

```

    I was able to duplicate the same script to return the county information. 
    First I used the for loop to iterate though each row but pulled the county name first.     
    Then counted one vote for each county when the county name was recognized. 
  
  ```python. 
    county_name = row[1]
  
    county_votes[county_name] += 1
  
  ``` 
  
If you use the current code you could use it to expand your analysis and iterate through another column of data. For example, if there was demographical data             regarding voter age. We could create a list then determine the age for each voter which would give insight as to which age range is voting per county. Also, which     age  ranges are voting for which candidate. 
  
 
 2. The image above is the rusult of a output function built into the script. The code is simple enough that another user could change the wording of the output if needed. If we are continuing with the example of analyzing voter demographical data, we could edit the script from, 

```python. 
election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)
    
    To 
    
election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f" _Voter Age_: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"Average Voter Age:\n")  
    print(election_results, end="")

    txt_file.write(election_results)
    
    This is another simple way another user could make simple, easy changes to adapt the script to a specific need. 
    
    



