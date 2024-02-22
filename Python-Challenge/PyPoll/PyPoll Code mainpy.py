import csv

# Create path to the csv file
file_path = "election_data.csv"

# Define Output path
output_file_path = "election_results.txt"

# Initialize variables so we can store a electoral anaysis
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Ignore the header row
    # Iterate through each row in the CSV file
    for row in reader:
        total_votes += 1
        candidate_name = row[2]
        # Update candidate's votes count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Print Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print individual candidate's results in the Terminal
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Open the output file for writing results to an external text file
with open(output_file_path, 'w') as output_file:
    # Write Election Results to the output file
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Calculate and write individual candidate's results into an external file
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        # Determine the winner
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")