import csv

# Create path to the CSV file
file_path = "budget_data.csv"

# Initialize the variables so we can store a financial analysis
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Ignore the the header row
    header = next(csv_reader)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Extract data from the current row
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months
        total_months += 1
        
        # Calculate the total profit and losses
        total_profit_losses += profit_loss
        
        # Calculate the change in profit and loss
        if previous_profit_loss != 0:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(date)
        
        # Store the current profit and loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit and loss
average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)

# Find the greatest increase and decrease in profit and loss
greatest_increase = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_increase_date = months[greatest_increase_index]

greatest_decrease = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_date = months[greatest_decrease_index]

# Print the financial analysis in the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write the financial analysis to a text file
with open("financial_analysis.txt", 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
