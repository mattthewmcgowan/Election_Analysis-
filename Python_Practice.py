#print("Hello World")

#print((5+2)*3)

from cgi import print_arguments
from pickle import APPEND


counties = ["Arapahoe", "Denver", "Jefferson"]

my_list = counties

#print (counties[2])

#print(len(counties))

#print(list(my_list[0:2]))

#my_list.append("El Paso")

#my_list.insert(2, "El Paso")

#my_list.remove("El Paso")

#my_list.pop(3)

#my_list[2] = "El Paso"

#my_list.insert(1, "El Paso")

#my_list.remove("Arapahoe")

 


#Creating a Dictionary 
#with county population count


my_dictionary = {
"Arapahoe": 422829,
"Denver": 463353,   
"Jefferson": 432438}

#print(my_dictionary.values())

#print(my_dictionary.get("Denver"))

#Inserting, Removing & Appending dictionary code 

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.insert(1,{"county": "El Paso", "registered voters": 461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})


# Algorithm that calculates the percentage of voes for a canidate receives in an election 

    # How many votes did you get?
    #my_votes = int(input("How many votes did you get in the election? "))
    #  Total votes in the election
    #total_votes = int(input("What is the total votes in the election? "))
    # Calculate the percentage of votes you received.
    #percentage_votes = (my_votes / total_votes) * 100
    #print("I received " + str(percentage_votes)+"% of the total votes.")

# IF STATEMENTS! 
#if my_list[1] == 'Denver':

   # print(my_list[1])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
   # print("Turn on the AC.")
#else:
    #print("Open the windows.")

#Nested If-Else Statements 

#What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
    #print('Your grade is an A.')
#else:
    #if score >= 80:
        #print('Your grade is a B.')
    #else:
        #if score >= 70:
            #print('Your grade is a C.')
        #else:
            #if score >= 60:
                #print('Your grade is a D.')
           # else:
                #print('Your grade is an F.')
#Membership Operators are used to test if an object, like a string, integer, or data type is present in an express, list, or dictionary.
    #in & not in 

#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
   # print("El Paso is in the list of counties.")
#else:
   # print("El Paso is not the list of counties.")

#Logical Operators: allow us to connect mulitple comparison expressions to create a compound expression. 
    #The three logical operators are and, or, and not. 
#if "Arapahoe" in counties and "El Paso" in counties:
    #print("Arapahoe and El Paso are in the list of counties.")
#else:
    #print("Arapahoe or El Paso is not in the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
    ##print("Arapahoe or El Paso is in the list of counties.")
#lse:
    #print("Arapahoe and El Paso are not in the list of counties.")

#if "Arapahoe" in counties and "El Paso" not in counties:
   #print("Only Arapahoe is in the list of counties.")
#else:
    #print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#Loops (repetition statements): tells the computer to loop an algorithm for a task over and over again. 
    #There are two types of loops, condition-controlled loops and count-controlled loops. 
        #A condition-controlled loop uses a true or false condition to control the number of times that it repeats, like asking a user
        #if they want to continue with their onlin shoping after they add something to their "basket". This is a while loop. 
        #This ype of condidtion has two parts . 
            #1. A condition that is tested for a ture or false value. 
            #2. A statement or statements that are repeated as long as the condition is true. 
        #A count-controlled loop, repeats a specific number of times depending on the conditions, such as getting all the items in a list.
        # This type of loop is also called a for loop. Python has a built-in function, range () that simplifies the process of writing a for loop. 
        #The range() function creates an iterable object or a list. 
        #Indexing can also be used to iterate througha list. If the list containers strings, we'll need to get the length of the list as an iteger 
        #for the range() function. 
        #To get only the keys from a dictionary using a for loop, the loop can be written like we are iterating over a list or tuple. 
        #WHEN ITERATING OVER A DICTIONARY THE FIRST VARIABLE IS DECLARED AS THE KEY 
        #THE SECOND VARIABLE IS ASSIGNED TO THE VALUES. 


#x = 0
#while x <= 5:
    #print(x)
    #x = x + 1

#for county in counties:
    #print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
    #print(num)

#for num in range(5):
    #print(num)

#for i in range(len(counties)):
    
    #print(counties[i])

#for county in my_dictionary:
    #print(county)

#for county in my_dictionary.keys():
    #print(county)

#for voters in my_dictionary.values():
    #print(voters)

#for key, value in my_dictionary.items():
    #print(key, value)

#if "Arapahoe" in my_dictionary
    #print("Arapahoe county has 422829 registered voters")
#if "Denver" in my_dictionary:
    #print("Denver county has 463353 registered voters")
#f "Jefferson" in my_dictionary:
    #print("Jefferson county has 432438 registered voters.")

#for county_dict in voting_data:
   # print(county_dict)

#for county_dict in voting_data:
 #   for value in county_dict.values():
  #      print(value)

## The print() function
# F-strings: Formatted string literals: the f-string begins with an f followed by a string contained within quotes.
#The term f-string comes from the leading F character preceding the string literal.
# in the f-string curly braces are used to add variables or expressions to the f-string. 

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []

county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""

winning_count = 0

winning_county_percentage = 0 



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0 


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if ( votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_county = county_name
            winning_county_percentage = vote_percentage
        

    # 7: Print the county with the largest turnout to the terminal.
    winning_counting_summary = (
             f"-------------------------\n"
             f"Largest County Turnout: {winning_county}\n"
             f"County Vote Count: {winning_count:,}\n"
             f"Largest county turnout percentage: {winning_county_percentage: .1f}%\n"
             f"-------------------------\n")
    print(winning_counting_summary)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_counting_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)