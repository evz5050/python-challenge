# Read in CSV
import os
import csv
csvpath = os.path.join('budget_data.csv')


with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

# calculate Total Months, net Profit/Losses, Avg Change, Greatest Inc/Dec/dates
    profit = []
    months = []
    revenue_change = []

    for row in csvreader:
        months.append(row[0])   
        profit.append(int(row[1]))
    
    total_months = len(months)
    total_profit = sum(profit)
    
    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))

    
    revenue_average = sum(revenue_change) / len(revenue_change)
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
    
    print("Financial Analysis")
    print("__________________________")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(revenue_average, 2)))
    print("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))
    
# Export to txt file
output_file = os.path.join("PyBank.txt")
with open(output_file, "w+") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("__________________________\n")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_profit))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(revenue_average, 2)))
    txt_file.write("\n")
    txt_file.write("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    txt_file.write("\n")
    txt_file.write("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))