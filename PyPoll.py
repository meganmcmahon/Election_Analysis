# The data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Hello World")
import csv
import os
# Assign variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "Election_analysis.txt")

# initialize total vote counter
total_votes = 0 

# candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# county list and county votes
county_names = []
county_votes = {}

# track the winning candidate vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# the largest county votes
largest_county_turnout = ""
largest_county_vote = 0




with open(file_to_load) as election_data:
   #read the file object with the reader function
    reader = csv.reader(election_data)
    #read the header, this will skip the first row
    header = next(reader)
# print each row in the CSV file
    for row in reader:
        # add the total vote counts
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]


        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

    print(candidate_options)
    print(candidate_votes) 
    
for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
# Determine winning vote count and candidate

if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


winning_candidate_summary = (
    f"----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------------------\n")
print(winning_candidate_summary)

with open(file_to_save, 'w') as txt_file:
    election_results = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------

    County Votes:
  
       
    """
    print(election_results, end = "")
    txt_file.write(election_results)