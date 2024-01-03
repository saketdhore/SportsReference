import json

# Read the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
teams = list(data.keys())
table = []

# Creating the header row
header_row = ['']
for team in teams:
    header_row.append(team)
table.append(header_row)

# Creating table rows
for team in teams:
    row = [team]
    for opponent in teams:
        if opponent != team:
            wins = data[team][opponent]['W']
            row.append(wins)
        else:
            row.append('-')
    table.append(row)

# Displaying the table
for row in table:
    print("".join(f"{cell:<5}" for cell in row))

