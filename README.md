Objective :
   The code aims to read match data between various teams from a JSON file and create a table showing the number of wins each team has against the others.

Code Explanation :
   The code starts with reading the JSON file and storing it in a dictionary so that the data is easier to manipulate and draw concclusions from. 
   Our code then easily extracts the team names from the created dicitonary and create our initially empty head-to-head table
   Our code then creates the header row which contains all the team names.
   Now comes the main which is to populate our head-to-head table. 
   The code iterates through each team, creating a row for each team that represents their wins against other teams. For every team, it checks its wins against all opponents, adding the number of wins to the row. If the 
   team is compared against itself, it marks the cell with a dash to indicate no match. This process fills the table with each team's wins against others.
   Finally, the code prints the generated table row by row, formatting each cell to have a width of 5 characters.

Usage :
   Just replace the 'data.json' with your own file path.






