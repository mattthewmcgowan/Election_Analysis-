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

## Election-Audit Summary 

This python script has a few maluable pieces in which new rows can be iterated through for deeper analysis. 

  1. The initial analysis was performed to find the candidates and the winner based on majority vote. Later, we took a look at the county turnout. This script could be    modified to look at a larger data set. For example, if demographical data was provided it would be relatively painless to edit the script to iderate though each row collecting voter age information. We could then turn around and give each candidate the average age of who voted for them. 
  2. Because we have our base code established, after the next election the user can create a new directory linking the CSV file to thier computer and easily import the new CSV data. 


