# Election_Analysis

Election Analysis with Python

## Overview of Election Audit: 

The purpose of this election audit analysis was to use Python to analyze the voting data in this Congressional election.  Using Python, we are able inform our employer who the winning candidate was, the total votes, the total votes for each candidate and the number of votes from each county.

## Election-Audit Results: 

- 369,711 votes were cast in this congressional election.
- The breakdown of county votes is:
    - Jefferson: 38,855 votes (10.5%)
    - Denver: 306,055 votes (82.8%)
    - Arapahoe: 24,801 votes ( 6.7%)

Sample code to determine county vote count:

<img width="460" alt="Screen Shot 2022-05-15 at 7 29 53 PM" src="https://user-images.githubusercontent.com/103215686/168505164-17a87a65-bdea-4a3a-bd71-3b5ae74a4729.png">

Sample code to determine the county that had the most votes:
<img width="661" alt="Screen Shot 2022-05-15 at 7 30 58 PM" src="https://user-images.githubusercontent.com/103215686/168505225-d8a9ba98-cc4d-453b-9bd7-beb33112d667.png">


- Denver county had the largest number of votes.
- The breakdown of candidate votes is:
    - Charles Casper Stockham: 85,213 votes (23%)
    - Diana DeGette: 272,892 votes (73.8%)
    - Raymon Anthony Doane: 11,606 votes (3.1%)
  
Sample code to determine candidate vote counts:
<img width="541" alt="Screen Shot 2022-05-15 at 7 29 18 PM" src="https://user-images.githubusercontent.com/103215686/168505122-218b82bf-f4d6-4cd0-b25e-254a68e266f3.png">

  
- Diana DeGette won the election with 272,892 votes which was 73.8% of the total vote count.

Sample code to determine the winning candidate:
<img width="565" alt="Screen Shot 2022-05-15 at 7 34 47 PM" src="https://user-images.githubusercontent.com/103215686/168505292-51d2719d-a91d-4f65-8e47-634e7fcd87ad.png">


## Election-Audit Summary: 

The Python script we have created for this election can be reused for future elections. When reusing this script in the future, ensure that the rows are corrected for the format of the csv file to ensure the correct data is being pulled to the right places. This script could also be used in larger scale, national elections. In this case, another for loop can be created to count votes for states. 
