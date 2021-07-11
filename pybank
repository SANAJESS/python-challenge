import os 
import csv

months = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
net_change_list =[]
average_change = 0
budget_csv = os.path.join("Resources", "budget_data.csv")

# Reading data from csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    prev_total = int(first_row[1])
    months += 1
    net_total += int(first_row[1])

    # Iterating through csv to get the number of months and net change
    for row in csvreader:
        months += 1
        net_total += int(row[1])
        net_change = int(row[1]) - prev_total
        prev_total = int(row[1])
        net_change_list += [net_change]
        
        # Determining the monthly greatest increase and decrease
        if net_change > greatest_increase:
            greatest_increase_month = row[0]
            greatest_increase = net_change

        if net_change < greatest_decrease:
            greatest_decrease_month = row[0]
            greatest_decrease = net_change
    
# Calculating the average of the monthly changes over the period
average_change = round(sum(net_change_list) / len(net_change_list), 2)

# Print results to terminal 
print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(net_total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")

# Export analysis to text file 
output_path = os.path.join("analysis", "bank_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.writelines(["Financial Analysis \n",
    "--------------------------- \n",
    "Total Months: " + str(months) + "\n", 
    "Total: $" + str(net_total) + "\n",
    "Average Change: $" + str(average_change) + "\n",
    "Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ") \n",
    "Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ") \n",
     ])
txtfile.close()