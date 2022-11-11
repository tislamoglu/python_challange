import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

# # Open and read csv
with open(budget_data) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")

     # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    
    print(f"Header: {csv_header}")

     # Read through each row of data after the header
    
    date=[]
    profit=[]
    total=0
    total_months=[]
    revenue_change=[]
    
    profit_losses_net=[]
    months = []

#Printing titles

    print("Financial Analysis")
    print("-------------------------------------------")
    
    for rows in csv_reader:
         profit.append(int(rows[1]))
         date.append(rows[0])
         total = sum((profit))
    print(f"Total Months: {len(profit)}")
    print(f"Total:$ {total}")


    for i in range(1, len(profit)):
            revenue_change.append((int(profit[i]) - int(profit[i-1])))

            revenue_average_change = sum(revenue_change) / len(revenue_change)


    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)

    
    
    datemax=int(revenue_change.index(greatest_increase))
    datemin=int(revenue_change.index(greatest_decrease))


    print(f"Average Change: ${round(revenue_average_change,2)}")

    print(f"Greatest Increase in Profits:  {date[datemax+1]}, (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {date[datemin+1]}, (${(greatest_decrease)})")
    

#Exproting the results to a text file  

analysis_results = os.path.join("..", "Resources", "analysis_results.txt")
with open(analysis_results, "w") as text_file:
    text_file.write(f"Total Months: {len(date)}")
    text_file.write(f"Total: ${sum(revenue_change)}")
    text_file.write(f"Average Change: ${round(revenue_average_change,2)}")
    text_file.write(f"Greatest Increase in Profits:  {date[datemax+1]}, (${greatest_increase})")
    text_file.write(f"Greatest Decrease in Profits: {date[datemin+1]}, (${(greatest_decrease)})")